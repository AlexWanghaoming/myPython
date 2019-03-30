#!/usr/bin/python3.5
# -*- coding:utf-8 -*-
# Author: wanghm

import subprocess
import time
import os
import pandas as pd
import numpy as np

os.chdir("/home/wanghm/whm/pacbio_data/Pacbio/PH-1/check_genome")
print("Workdir:", os.getcwd())
# subprocess.Popen("mummer -mum -l 100 -L Fusarium_graminearum.RR1_with_mito.fa rf_polished.fasta > mum_200.mums",shell=True)
# subprocess.Popen("awk '/>/{a=$2}{if($1==a){print$0}}' mum_200.mums | awk '{print$1\"\t\"$2\"\t\"$3\"\t\"$4\"\t\"}' > filter1.mums", shell=True)

df = pd.read_table("filter1.mums", sep="\t", header=None, usecols=[0, 1, 2, 3])
df.columns = ["chr", "rf_mapped_start", "fg_mapped_start", "mapped_length"]
# print(a.groupby("chr").groups.keys())
df_list = []
for i in df.groupby("chr"):
    grouped_df = i[1]
    # extract most of intervals:
    chr_num = list(grouped_df["chr"])[:-1]
    rf_interval_start = list(grouped_df["rf_mapped_start"] + grouped_df["mapped_length"][:-1])
    rf_interval_end = list((grouped_df["rf_mapped_start"] - 1)[1:])
    fg_interval_start = list(grouped_df["fg_mapped_start"] + grouped_df["mapped_length"][:-1])
    fg_interval_end = list((grouped_df["fg_mapped_start"] - 1)[1:])

    # extract first interval on each chromosomer:
    # a = grouped_df[grouped_df["rf_mapped_start"] == 1]
    # if a["fg_mapped_start"] == 1:
    #     pass
    # else:
    # b = grouped_df[grouped_df["fg_mapped_start"] == 1]
    #         chr_num.insert(0,pd.unique(grouped_df["chr"]))
    #         rf_interval_start.insert(0,0)
    #         rf_interval_end.insert(0,grouped_df["rf_mapped_start"])
    #         fg_interval_start.insert(0,0)
    #         fg_interval_end.insert(0,grouped_df["fg_mapped_start"])

    tmp_df = pd.DataFrame([chr_num, rf_interval_start, rf_interval_end, fg_interval_start, fg_interval_end],
                          index=["chr", "rf_interval_start", "rf_interval_end", "fg_interval_start",
                                 "fg_interval_end"])
    tmp_df = tmp_df.T.dropna(axis=0)
    tmp_df.iloc[:, 1:] = tmp_df.iloc[:, 1:].astype("int")
    # tmp_df["rf_interval_start","rf_interval_end"] = tmp_df["rf_interval_end", "rf_interval_start"].values
    df_list.append(tmp_df)
result = pd.concat(df_list, axis=0)
result.to_csv("mummer_interval", header=False, index=False, sep="\t")
# subprocess.Popen(
#     "awk '{if($2>$3){if($4>$5){print$1\"\t\"$3\"\t\"$2\"\t\"$5\"\t\"$4\"\t\"\"-\"}else{print$1\"\t\"$3\"\t\"$2\"\t\"$4\"\t\"$5\"\t\"\"-\"};next}{if($4>$5){print$1\"\t\"$2\"\t\"$3\"\t\"$5\"\t\"$4\"\t\"\"-\"}else{print$0\"\t\"\"+\"}}}' interval/mummer_interval > interval/mummer_interval_overlap",
#     shell=True)
