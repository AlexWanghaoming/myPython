from Bio import SeqIO
from  Bio import Seq
import re
import time

genome = SeqIO.parse("/home/wanghm/whm/1FG/35genome/correctGenome_ph1.fa",format="fasta")
def replace_str_index(text,index,replacement):
    return '%s%s%s'%(text[:index], replacement, text[index+1:])

seqList = []
for chr in genome:
    print(chr.id,len(chr.seq))
    # offset = 0
    sequence = str(chr.seq)
    with open("/home/wanghm/whm/resequence/correctionResult_withLength", "r+") as f:
        for linenumber,line in enumerate(f):
            if linenumber > 322 and chr.id == line.split()[0] and line.split()[4] == "all":
                index = int(line.split()[1]) - 1
                replacement = line.split()[3] if line.split()[3] != "-" else ""
                sequence = replace_str_index(sequence, index, replacement)
                replace_length = len(replacement)
                # offset = offset + replace_length-1
    result = SeqIO.SeqRecord(id=chr.id, description="length=%d"%(len(sequence)), seq=Seq.Seq(sequence))
    seqList.append(result)

SeqIO.write(seqList, "/home/wanghm/whm/1FG/35genome/ph1_final.fasta", format="fasta")
