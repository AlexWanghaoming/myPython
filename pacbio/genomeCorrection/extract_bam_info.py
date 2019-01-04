#!/usr/bin/python3.5
# -*- coding:utf-8 -*-
# Author: wanghm

import pysam
import os
import time
import pandas as pd
import pickle
import collections
import utils

os.chdir("/home/wanghm/whm/resequence")
print("Workdir:", os.getcwd())

pure_bam = pysam.Samfile("official_resequence_sorted.bam", "rb")

rf_interval = pd.read_table("/home/wanghm/whm/pacbio_data/Pacbio/PH-1/check_genome/interval/mummer_interval_overlap",
                            sep="\t", header=None, usecols=[0, 1, 2, 5],
                            names=["chr", "ref_interval_start", "ref_interval_end", "intervalOrOverlap"])

fg_interval = pd.read_table("/home/wanghm/whm/pacbio_data/Pacbio/PH-1/check_genome/interval/mummer_interval_overlap",
                            sep="\t", header=None, usecols=[0, 3, 4, 5],
                            names=["chr", "fg_interval_start", "fg_interval_end", "intervalOrOverlap"])


"""
for each region in row of interval dataframe, we make a dict to record every reads that overlap with the interval:
"""

# pysam.AlignedSegment
interval_info_dict = utils.DefaultOrderedDict(list) # define a defaultdict to store list
def extract_interval_info(chr_num, start, end):
    for i in range(start, end):
        for pileupcolumn in pure_bam.pileup("%s"%chr_num, start, end):
            if pileupcolumn.pos == i:
                tmp_list = []
                for pileupread in pileupcolumn.pileups:
                    print(pileupread.query_position)
                    try:
                        base = pileupread.alignment.query_sequence[pileupread.query_position]
                    except TypeError:
                        continue
                    print(base)
                    tmp_list.append(base)
                    print("*************")
                print(chr_num,start,end,tmp_list)
                try:
                    unique_trueBase = collections.Counter(tmp_list).most_common(1)[0][0]
                    print("{0} base appear most in position {1}".format((collections.Counter(tmp_list).most_common(1)[0][0]), i))
                except IndexError:
                    unique_trueBase = "N"
                # time.sleep(4)
                interval_info_dict["{0}_{1}_{2}".format(chr_num, start, end)].append(unique_trueBase)

if __name__ == "__main__":

    st = time.clock()
    rf_interval.apply(lambda row: extract_interval_info(row["chr"], row["ref_interval_start"] - 1, row["ref_interval_end"]),
                      axis=1)  # named a method row: to use extract_interval_info(), axis=1 means aim to each rows
    # fg_interval.apply(lambda row: extract_interval_info(row["chr"], row["fg_interval_start"] - 1, row["fg_interval_end"]),
    #                   axis=1)
    finish = time.clock()
    print("Time consuming: {0} seconds".format(finish-st))
    # connect all bases to a interval sequence
    interval_seqs = list(map(lambda x:"".join(interval_info_dict[x]), interval_info_dict))
    interval_name = list(interval_info_dict.keys())
    interval_df = pd.DataFrame([interval_name,interval_seqs], index=["name", "seq"])
    df1 = interval_df.T
    df1.to_csv("rf_intervalSeqs", sep="\t", header=False, index=False)


    """
    Serialization with pickle
    """
    # pickle_out3 = open("pickle_out3", "wb")
    # pickle.dump(df1, pickle_out3)
    # pickle_out3.close()


"""
fetch method start/end base site is 0-based
use method: pysam.AlignmentFile

"""

# pure_bam = pysam.AlignmentFile("official_resequence_sorted.bam", "rb")
# iter = pure_bam.fetch("1", start, end)
# for read in iter:
#     print(read.pos, read.query, read.mapping_quality)






















