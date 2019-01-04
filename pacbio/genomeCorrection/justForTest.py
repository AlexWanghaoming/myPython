#!/usr/bin/python3.5
# -*- coding:utf-8 -*-
# Author: wanghm
import pandas as pd
import os
import pysam

# os.chdir("/home/wanghm/whm/resequence")
# print("Workdir:", os.getcwd())
# pure_bam = pysam.Samfile("official_resequence_sorted.bam", "rb")
# rf_interval = pd.read_table("/home/wanghm/whm/pacbio_data/Pacbio/PH-1/check_genome/interval/mummer_interval_overlap",
#                             sep="\t", header=None, usecols=[0, 1, 2, 5],
#                             names=["chr", "ref_interval_start", "ref_interval_end", "intervalOrOverlap"])
#
# # for pileupcolumn in pure_bam.pileup("1", 38901, 38902):
#     for pileupread in pileupcolumn.pileups:
#         ss = []
#         if pileupcolumn.pos == 38901:
#             if not pileupread.is_del and not pileupread.is_refskip:
#                 base = pileupread.alignment.query_sequence[pileupread.query_position]
#                 # ss.append(str(base))
#                 print(str(base))
#                 ss.append("T")
#                 print(ss)
from collections import Counter
# a = ["T", "C", "T", "A", "A"]
# print(Counter(a).most_common(1)[0][0])
# while 38901 <= 38902:
import time
# tmp = []
# tmp2 = []


# for pileupcolumn in pure_bam.pileup("1", 360794, 360830):
#     print(pileupcolumn)
#     time.sleep(2)
#     for pileupread in pileupcolumn.pileups:
#         # for each base we calculate the counts and choose the most one to be the truth
#         for _ in range(360830-360794):
#             print("we are identify reads ... ... ...")
#             tmp = []
#             if i<=360830 and pileupcolumn.pos == i:
#                 base = pileupread.alignment.query_sequence[pileupread.query_position]
#                 tmp.append(base)
#                 find_most_in_list(tmp)
#                 i = i+1
# rf_interval_info_dict = {}
# for i in range(2,100):
#     for pileupcolumn in pure_bam.pileup("1", 2, 100):
#         if pileupcolumn.pos == i:
#             tmp_list = []
#             for pileupread in pileupcolumn.pileups:
#                 if not isinstance(pileupread.query_position, int):
#                     base = pileupread.alignment.query_sequence[pileupread.query_position]
#                     print(base)
#                     time.sleep(50)
#                 # tmp_list.append(base)
#                 print("*************"
#                       "*************")
            # print(tmp_list)
            # print("{0} base appear most in position {1}".format((Counter(tmp_list).most_common(1)[0][0]), i))
            # time.sleep(4)
            # try:
            #     rf_interval_info_dict["{0}_{1}_{2}".format(chr_num, start, end)].append(unique_trueBase)
            # except KeyError:
            #     rf_interval_info_dict["{0}_{1}_{2}".format(chr_num, start, end)] = []
            #     rf_interval_info_dict["{0}_{1}_{2}".format(chr_num, start, end)].append(unique_trueBase)
from Bio import SeqIO
from Bio.Seq import Seq
import time
fg_genome = SeqIO.parse("/home/wanghm/whm/pacbio_data/Pacbio/PH-1/6mA/fg_polished.fasta", format="fasta")
official_genome = SeqIO.parse("/home/wanghm/whm/1FG/35genome/Fusarium_graminearum.RR1_with_mito.fa", format="fasta")
for of,fg in zip(official_genome,fg_genome):
    if of.id == fg.id == "1":
        print(of.seq[466777-20:466777+3])
        print(fg.seq[466850-20:466850+3])
        print(of.seq[360830:360830+10])
        print(fg.seq[360903:360903+10])
    if of.id == fg.id == "2":
        print(of.seq[2650251-20:2650251+5])
        print(fg.seq[2649650-20:2649655])
    #     print()
# ss = "A"*49+"C"+"A"*50
# aa = "A"*100
# ssseq = SeqIO.SeqRecord(seq=Seq(ss),id="ss")
# aaseq = SeqIO.SeqRecord(seq=Seq(aa),id="aa")
# SeqIO.write(aaseq,"sdad",format="fasta")
# SeqIO.write(ssseq,"ssss",format="fasta")
