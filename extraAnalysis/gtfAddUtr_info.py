#!/usr/bin/python3.5
# -*- coding:utf-8 -*-
# Author: Wang Haoming

"""
pandas !
"""

import re
import pandas as pd
import time

def make_five_prime_utr():
    chrom = []
    source = []
    element = []
    five_primerStart = []
    five_primerEnd = []
    noName = []
    strand = []
    phrase = []
    info = []
    for tra_name in list(set(transcriptName_list)):
        df_tmp = df[df.iloc[:, 8].str.contains(tra_name) == True]
        if len(df_tmp) >= 3:
            if df_tmp.iloc[:, 6].values[0] == "+":
                try:
                    chrominfo = df_tmp.iloc[:, 0].unique()[0]
                    sourceinfo = df_tmp.iloc[:, 1].unique()[0]
                    elementinfo = "five_prime_UTR"
                    five_primer_utr_startSite = sorted(df_tmp[df_tmp.iloc[:, 2] == "exon"].iloc[:, 3])[0]
                    five_primer_utr_endSite = sorted(df_tmp[df_tmp.iloc[:, 2] == "CDS"].iloc[:, 3])[0] - 1
                    noNameinfo = "."
                    strandinfo = "+"
                    phraseInfo = "."
                    complexInfo = "Parent=transcript:%s" % (tra_name)
                except IndexError:
                    pass
            elif df_tmp.iloc[:, 6].values[0] == "-":
                try:
                    chrominfo = df_tmp.iloc[:, 0].unique()[0]
                    sourceinfo = df_tmp.iloc[:, 1].unique()[0]
                    elementinfo = "five_prime_UTR"
                    five_primer_utr_startSite = sorted(df_tmp[df_tmp.iloc[:, 2] == "CDS"].iloc[:, 4], reverse=True)[0] + 1
                    five_primer_utr_endSite = sorted(df_tmp[df_tmp.iloc[:, 2] == "exon"].iloc[:, 4], reverse=True)[0]
                    noNameinfo = "."
                    strandinfo = "-"
                    phraseInfo = "."
                    complexInfo = "Parent=transcript:%s" % (tra_name)
                except IndexError:
                    pass
            if five_primer_utr_startSite < five_primer_utr_endSite:
                chrom.append(chrominfo)
                source.append(sourceinfo)
                element.append(elementinfo)
                five_primerStart.append(five_primer_utr_startSite)
                five_primerEnd.append(five_primer_utr_endSite)
                noName.append(noNameinfo)
                strand.append(strandinfo)
                phrase.append(phraseInfo)
                info.append(complexInfo)
    print(len(five_primerStart))
    df_five_primer = pd.DataFrame([chrom, source, element, five_primerStart, five_primerEnd, noName, strand, phrase, info])
    return df_five_primer
def make_three_prime_utr():
    chrom = []
    source = []
    element = []
    three_primerStart = []
    three_primerEnd = []
    noName = []
    strand = []
    phrase = []
    info = []
    for tra_name in list(set(transcriptName_list)):
        df_tmp = df[df.iloc[:, 8].str.contains(tra_name) == True]
        if len(df_tmp) >= 3:
            if df_tmp.iloc[:, 6].values[0] == "+":
                """
                may be there are some transcripts without exon or CDS, so use try-except.
                """
                try:
                    chrominfo = df_tmp.iloc[:, 0].unique()[0]
                    sourceinfo = df_tmp.iloc[:, 1].unique()[0]
                    elementinfo = "three_prime_UTR"
                    three_primer_utr_startSite = sorted(df_tmp[df_tmp.iloc[:, 2] == "CDS"].iloc[:, 4], reverse=True)[0] + 1
                    three_primer_utr_endSite = sorted(df_tmp[df_tmp.iloc[:, 2] == "exon"].iloc[:, 4], reverse=True)[0]
                    noNameinfo = "."
                    strandinfo = "+"
                    phraseInfo = "."
                    complexInfo = "Parent=transcript:%s" % (tra_name)
                except IndexError:
                    pass
            elif df_tmp.iloc[:, 6].values[0] == "-":
                try:
                    chrominfo = df_tmp.iloc[:, 0].unique()[0]
                    sourceinfo = df_tmp.iloc[:, 1].unique()[0]
                    elementinfo = "three_prime_UTR"
                    three_primer_utr_startSite = sorted(df_tmp[df_tmp.iloc[:, 2] == "exon"].iloc[:, 4])[0]
                    three_primer_utr_endSite = sorted(df_tmp[df_tmp.iloc[:, 2] == "CDS"].iloc[:, 3])[0] - 1
                    noNameinfo = "."
                    strandinfo = "-"
                    phraseInfo = "."
                    complexInfo = "Parent=transcript:%s" % (tra_name)
                except IndexError:
                    pass
            if three_primer_utr_startSite < three_primer_utr_endSite:
                chrom.append(chrominfo)
                source.append(sourceinfo)
                element.append(elementinfo)
                three_primerStart.append(three_primer_utr_startSite)
                three_primerEnd.append(three_primer_utr_endSite)
                noName.append(noNameinfo)
                strand.append(strandinfo)
                phrase.append(phraseInfo)
                info.append(complexInfo)
    print(len(three_primerStart))
    df_three_primer = pd.DataFrame([chrom, source, element, three_primerStart, three_primerEnd, noName, strand, phrase, info])
    return df_three_primer
if __name__== "__main__":
    df = pd.read_table("/home/wanghm/whm/1FG/newGffOut/FG_fixORF_nofusion_new.gff", header=None, sep="\t",
                   low_memory=False)
    transcriptName_list = []

    """
    Filter!!
    """
    df2 = df.iloc[:, 8][df.iloc[:, 2] == "exon"]
    """
    df2 is Series.
    """
    print(type(df2))
    for i in df2:
        transcriptName_list.append(re.split(":|;", i)[1])

    """
    pd.concat() Add UTR infomation to raw gff3
    """

    df_3 = pd.concat([df, make_five_prime_utr().T, make_three_prime_utr().T], ignore_index=True)
    df_3.to_csv("/home/wanghm/whm/1FG/withUTR.gff", index=False, header=False, sep="\t")
