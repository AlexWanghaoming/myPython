#!/usr/bin/python3.5
# -*- coding:utf-8 -*-
# Author: wanghm
from Bio.Blast import NCBIXML
from Bio import SearchIO
from Bio import SeqIO
import time
result_handle=open('/home/wanghm/whm/pacbio_data/Pacbio/YDJ-3/blast_result.xml', 'r')


"""
record has three attribute: 
descriptions(list:[sequence name in database,score,e-value,num_alignment])
alignments(list:[sequence_name in database, length, hasps])
multilple_alignment:alignment info
"""
# blast_records = NCBIXML.parse(result_handle)  # methods one
# for blast_record in blast_records:
#     for alignment in blast_record.alignments:
#         for hsp in alignment.hsp:
#             if hsp.expect < 0.00001
#                 print("****alignment****")
#                 print('sequence:'+ alignment.title)
#                 print('length:'+ alignment.length)
#                 print(hsp.query[0:75] + '...')
#                 print(hsp.match[0:75] + '...')
#                 print(hsp.sbjct[0:75] + '...')

# method 2
query_list = []
blast_qresults = SearchIO.parse(result_handle, 'blast-xml')
for blast_qresult in blast_qresults:
    print(type(blast_qresult))
    # for index, hsp in enumerate(blast_qresult):

        # print(index, hsp.query_id)
        # if index == 0:
        #     query_list.append(hsp.query_id)
        # else:
        #     pass
        # elif hsp.query_id in query_list:
        #     pass
        # else:
        #     query_list.append(hsp.query_id)
print(len(query_list))


# blast_hsp = blast_qresult[2]
# print(blast_hsp)
# print(blast_hsp.query_id)
