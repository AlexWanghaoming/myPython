#!/usr/bin/python3.5
# -*- coding:utf-8 -*-
# Author: wanghm
"""
calculate fasta sequences length
"""
# from Bio import SeqIO
# seqs = SeqIO.parse("/home/wanghm/whm/ngs/Morimp1/Morimp1_MitochondrionScaffolds.fasta", "fasta")
# l = 0
# for seq in seqs:
#     print(seq.id+":"+str(len(seq)))
#     l = l + len(seq)
# print("Total:",l)


# rf_seqs = SeqIO.parse("/home/wanghm/whm/pacbio_data/Pacbio/PH-1/check_genome/Fusarium_graminearum.RR1_with_mito.fa","fasta")
# for seq in rf_seqs:
#     if seq.id == "1":
#         print(seq.seq[144838:144844])
#
# fg_seqs = SeqIO.parse("/home/wanghm/whm/pacbio_data/Pacbio/PH-1/check_genome/fg_polished.fasta", "fasta")
# for seq in fg_seqs:
#     if seq.id == "1":
#         print(seq.seq[73:573])
# ss = "sdadasdas"
# ss = " "
# if ss:
#     print("Good!")

# ss = {}
# if ss["dd"] == None:
#     ss["dd"] = [].append("whm")
# if ss["dd"]

# i = {}
# i["sdsd"].append("sdsds")
# print(i)

# ss = {}
# for i in range(4):
#     try:
#         ss["dd"].append("wanghm%d"%i)
#     except KeyError:
#        ss["dd"] = []
#        ss["dd"].append("wanghm%d"%i)
#
# print(ss.keys(), ss.values(), ss.items())




#!/usr/bin/python3.5
# -*- coding:utf-8 -*-
# Author: wanghm
"""
calculate fasta sequences length
"""
# from Bio import SeqIO
# seqs = SeqIO.parse("/home/wanghm/whm/ngs/Morimp1/Morimp1_MitochondrionScaffolds.fasta", "fasta")
# l = 0
# for seq in seqs:
#     print(seq.id+":"+str(len(seq)))
#     l = l + len(seq)
# print("Total:",l)


# rf_seqs = SeqIO.parse("/home/wanghm/whm/pacbio_data/Pacbio/PH-1/check_genome/Fusarium_graminearum.RR1_with_mito.fa","fasta")
# for seq in rf_seqs:
#     if seq.id == "1":
#         print(seq.seq[144838:144844])
#
# fg_seqs = SeqIO.parse("/home/wanghm/whm/pacbio_data/Pacbio/PH-1/check_genome/fg_polished.fasta", "fasta")
# for seq in fg_seqs:
#     if seq.id == "1":
#         print(seq.seq[73:573])
# ss = "sdadasdas"
# ss = " "
# if ss:
#     print("Good!")

# ss = {}
# if ss["dd"] == None:
#     ss["dd"] = [].append("whm")
# if ss["dd"]

# i = {}
# i["sdsd"].append("sdsds")
# print(i)

# ss = {}
# for i in range(4):
#     try:
#         ss["dd"].append("wanghm%d"%i)
#     except KeyError:
#        ss["dd"] = []
#        ss["dd"].append("wanghm%d"%i)
#
# print(ss.keys(), ss.values(), ss.items())


from functools import reduce


# a = ["a", "t", "t", "t", "t"]
# b = pd.DataFrame(a)
# print(b.iloc[:,0])

import itertools
import operator

#
# def most_common(L):
#     #g
#     groups = itertools.groupby(sorted(L))
#     # auxiliary func to get "quality" for an item
#     def _auxfun(item, iterable):
#         return len(list(iterable)), -L.index(item)
#     return max(groups, key=_auxfun)[0]
#
# from collections import Counter
# print(Counter(Ll).most_common(1)[0])
#
# import collections
# a = collections.defaultdict(list)
# print(a["3434_334"])
# i = ["a", "sd", "sd"]
# ii = pd.Series(i)
# b = {343:[],454:[],5557:[]}
# bb = pd.Series(list(b.keys()))
# df = pd.DataFrame([i, list(b.keys())], index=["a", "seqs"])
# dff = pd.DataFrame([ii,bb],)
# print(df.T)
# print(dff.T)

# ref_tmpList = []
# for read1 in bamFile1.fetch("%s"%chr_num, ref, 144844):
#     ref_tmpList.append(read1.qname)
# fg_tmpList = []
# for read2 in bamFile2.fetch("1", 144911, 144917):
#     fg_tmpList.append(read2.qname)
#
# intersectionList = [val for val in ref_tmpList if val in fg_tmpList]
#
# # mapping_quality comparison!
# ref_mappingQuality = []
# fg_mappingQuality = []
# for i in intersectionList:
#     for read1 in bamFile1.fetch("1", 144838, 144844):
#         if read1.qname == i:
#             ref_mappingQuality.append(read1.mapping_quality)
#
#     for read2 in bamFile2.fetch("1", 144911, 144917):
#         if read2.qname == i:
#             fg_mappingQuality.append(read2.mapping_quality)
# print(levene(ref_mappingQuality, fg_mappingQuality))  # homegeneity of variance test
# print(ttest_ind(ref_mappingQuality, fg_mappingQuality, equal_var=False))  # t-test





#!/usr/bin/python3.5
# -*- coding:utf-8 -*-
# Author: wanghm
"""
calculate fasta sequences length
"""
# from Bio import SeqIO
# seqs = SeqIO.parse("/home/wanghm/whm/ngs/Morimp1/Morimp1_MitochondrionScaffolds.fasta", "fasta")
# l = 0
# for seq in seqs:
#     print(seq.id+":"+str(len(seq)))
#     l = l + len(seq)
# print("Total:",l)


# rf_seqs = SeqIO.parse("/home/wanghm/whm/pacbio_data/Pacbio/PH-1/check_genome/Fusarium_graminearum.RR1_with_mito.fa","fasta")
# for seq in rf_seqs:
#     if seq.id == "1":
#         print(seq.seq[144838:144844])
#
# fg_seqs = SeqIO.parse("/home/wanghm/whm/pacbio_data/Pacbio/PH-1/check_genome/fg_polished.fasta", "fasta")
# for seq in fg_seqs:
#     if seq.id == "1":
#         print(seq.seq[73:573])
# ss = "sdadasdas"
# ss = " "
# if ss:
#     print("Good!")

# ss = {}
# if ss["dd"] == None:
#     ss["dd"] = [].append("whm")
# if ss["dd"]

# i = {}
# i["sdsd"].append("sdsds")
# print(i)

# ss = {}
# for i in range(4):
#     try:
#         ss["dd"].append("wanghm%d"%i)
#     except KeyError:
#        ss["dd"] = []
#        ss["dd"].append("wanghm%d"%i)
#
# print(ss.keys(), ss.values(), ss.items())


from functools import reduce


# a = ["a", "t", "t", "t", "t"]
# b = pd.DataFrame(a)
# print(b.iloc[:,0])



#
# def most_common(L):
#     #g
#     groups = itertools.groupby(sorted(L))
#     # auxiliary func to get "quality" for an item
#     def _auxfun(item, iterable):
#         return len(list(iterable)), -L.index(item)
#     return max(groups, key=_auxfun)[0]
#
# from collections import Counter
# print(Counter(Ll).most_common(1)[0])
#
# import collections
# a = collections.defaultdict(list)
# print(a["3434_334"])
# i = ["a", "sd", "sd"]
# ii = pd.Series(i)
# b = {343:[],454:[],5557:[]}
# bb = pd.Series(list(b.keys()))
# df = pd.DataFrame([i, list(b.keys())], index=["a", "seqs"])
# dff = pd.DataFrame([ii,bb],)
# print(df.T)
# print(dff.T)

# ref_tmpList = []
# for read1 in bamFile1.fetch("%s"%chr_num, ref, 144844):
#     ref_tmpList.append(read1.qname)
# fg_tmpList = []
# for read2 in bamFile2.fetch("1", 144911, 144917):
#     fg_tmpList.append(read2.qname)
#
# intersectionList = [val for val in ref_tmpList if val in fg_tmpList]
#
# # mapping_quality comparison!
# ref_mappingQuality = []
# fg_mappingQuality = []
# for i in intersectionList:
#     for read1 in bamFile1.fetch("1", 144838, 144844):
#         if read1.qname == i:
#             ref_mappingQuality.append(read1.mapping_quality)
#
#     for read2 in bamFile2.fetch("1", 144911, 144917):
#         if read2.qname == i:
#             fg_mappingQuality.append(read2.mapping_quality)
# print(levene(ref_mappingQuality, fg_mappingQuality))  # homegeneity of variance test
# print(ttest_ind(ref_mappingQuality, fg_mappingQuality, equal_var=False))  # t-test
"""
interval_info = pd.read_table(
    "/home/wanghm/whm/pacbio_data/Pacbio/PH-1/check_genome/interval/mummer_interval_overlap",
    sep="\t", header=None,
    names=["chr", "ref_interval_start", "ref_interval_end", "fg_interval_start",
           "fg_interval_end", "intervalOrOverlap"])
interval_info["priority"] = pd.Series([i for i in range(311)])
print(len(interval_info))
print(interval_info)
print([i for i in range(1,10,2)])

with open("/home/wanghm/whm/resequence/diff_interval", "r") as aim_interval:
    print(aim_interval.readlines())
"""
print(len(""))
