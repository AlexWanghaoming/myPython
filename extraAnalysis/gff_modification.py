#!/usr/bin/python3.5
# -*- coding:utf-8 -*-
# Author: Wang Haoming

import pandas as pd
import re
import multiprocessing
import subprocess
import time
import os, sys
'''
df.iloc[] is Series Objects
'''
# each_lineNumber = int(
#     int(os.popen(r"wc -l /home/wanghm/whm/1FG/FG-fix_ORF-fix_nofusion5-rm_repeat.gff | cut -d' ' -f 1").read()) / 4)
# print(each_lineNumber)
# subprocess.Popen(r"split -l {0} /home/wanghm/whm/1FG/FG-fix_ORF-fix_nofusion5-rm_repeat.gff.bak -d splitGFF_".format(
#     each_lineNumber), shell=True)

def worker(splited_gff_file):
    df = pd.read_table(splited_gff_file, header=None, sep="\t",
                       low_memory=False)
    gene_element = df.iloc[:, 2]
    info = df.iloc[:, 8]
    for index, i in enumerate(gene_element):
        if i == "mRNA":
            df.iloc[:, 8][index] = "ID=transcript:{0};Parent=gene:{1};biotype=protein_coding;transcript_id={2}".format(
                re.split('=|;', info[index])[1], re.split(';|=', info[index])[3], re.split(';|=', info[index])[1])
        if i == "CDS":
            print(info[index])
            df.iloc[:, 8][index] = "ID=CDS:{0};Parent=transcript:{1}".format(re.split('=', info[index])[1],
                                                                             re.split('=', info[index])[1])
        elif i == "exon":
            df.iloc[:, 8][index] = "Parent=transcript:{0};Name={1};exon_id={2}".format(re.split('=', info[index])[1],
                                                                                       re.split('=', info[index])[1],
                                                                                       re.split('=', info[index])[1])
    df.to_csv('/home/wanghm/whm/1FG/newGffOut/%s.csv'%(splited_gff_file.split("/")[6]), index=False, header=False, sep="\t")
    print("A part of work finished!")


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4)
    for i in range(4):
        splited_gff_file = os.path.abspath("splitGFF_0%d"%(i))
        pool.apply_async(worker, (splited_gff_file, ))
    pool.close()
    pool.join()
    print("finished!")

