#!/usr/bin/python3.5
# -*- coding:utf-8 -*-
# Author: wanghm
import os
import pickle
import subprocess
import pysam
import pandas as pd
from scipy.stats import ttest_ind
from scipy.stats import levene
import time

os.chdir("/home/wanghm/whm/resequence")
print("Workdir:", os.getcwd())
bamFile1 = pysam.AlignmentFile('official_resequence_sorted.bam', "rb")
bamFile2 = pysam.AlignmentFile("fg_resequence_sorted.bam", "rb")

# subprocess.Popen("paste ref_intervalSeqs fg_intervalSeqs | awk '$2!=$4' | awk '{split($1,a,\"_\");print a[1],a[2]+1,a[3]}' > diff_interval", shell=TRUE)

#  I have try to find snps:
# awk '{print$1,$2-1,$3}' ~/whm/pacbio/PH1/check_genome/intercal/mummer_interval_overlap > callsnps.bed
# samtools mpileup -v -l callsnps.bed official_resequence_sorted.bam > interval_snps.variants
# bcftools call -vmO v -o snp.vcf interval_snps.variants

def judging_priority(chr_num, ref_start, ref_end, fg_start, fg_end):

    identifier = "{0} {1} {2}\n".format(chr_num, ref_start, ref_end)
    if identifier in diffseqInterval_list:
        print("Yes")

        # extract intersection!
        ref_tmpList = []
        for read1 in bamFile1.fetch("%s" % chr_num, ref_start, ref_end):
            ref_tmpList.append(read1.qname)
        fg_tmpList = []
        for read2 in bamFile2.fetch("%s" % chr_num, fg_start, fg_end):
            fg_tmpList.append(read2.qname)

        intersectionList = [val for val in ref_tmpList if val in fg_tmpList]

        # mapping_quality comparison!

        ref_mappingQuality = []
        fg_mappingQuality = []
        for i in intersectionList:
            for read1 in bamFile1.fetch("%s" % chr_num, ref_start, ref_end):
                if read1.qname == i:
                    ref_mappingQuality.append(read1.mapping_quality)

            for read2 in bamFile2.fetch("%s" % chr_num, fg_start, fg_end):
                if read2.qname == i:
                    fg_mappingQuality.append(read2.mapping_quality)
        homogeneity = levene(ref_mappingQuality, fg_mappingQuality)  # homogeneity of variance test
        if homogeneity[1] > 0.05:
            t_test_result = ttest_ind(ref_mappingQuality, fg_mappingQuality, equal_var=True)  # t-test
            if t_test_result[0] > 0:
                priority.append("refPriority")
                p_value.append(t_test_result[1])
        if homogeneity[1] < 0.05:
            t_test_result = ttest_ind(ref_mappingQuality, fg_mappingQuality, equal_var=False)
            if t_test_result[0] < 0:
                priority.append("fgPriority")
                p_value.append(t_test_result[1])
    else:
        print("No!")
        priority.append("Same")
        p_value.append("Na")

if __name__ == "__main__":

    with open("/home/wanghm/whm/resequence/diff_interval", "r") as aim_interval:
        diffseqInterval_list = aim_interval.readlines()

    priority = []
    p_value = []

    interval_info = pd.read_table(
        "/home/wanghm/whm/pacbio_data/Pacbio/PH-1/check_genome/interval/mummer_interval_overlap",
        sep="\t", header=None,
        names=["chr", "ref_interval_start", "ref_interval_end", "fg_interval_start",
               "fg_interval_end", "intervalOrOverlap"])

    st = time.clock()
    interval_info.apply(lambda row: judging_priority(row["chr"], row["ref_interval_start"] - 1, row["ref_interval_end"],
                                                     row["fg_interval_start"] - 1, row["fg_interval_end"]),axis=1)

    finish = time.clock()
    print("Time consuming: {0} seconds".format(finish-st))

    interval_info["priority"] = pd.Series(priority)
    interval_info["p_value"] = pd.Series(p_value)

    interval_info.to_csv("intervalPriority", sep="\t", header=False, index=False)
