#!/usr/bin/python3.5
# -*- coding:utf-8 -*-
# Author: wanghm
import time
from Bio import Seq
from Bio import SeqIO
import regex

def search_motif(str, motif):
    match = regex.finditer(motif, str, overlapped=True)
    position = [(x.start()+1, x.end()) for x in match]
    return position

if __name__ == "__main__":
    # print(range(2))
    # time.sleep(50)
    positive_motif = "GAG[GT]C"
    negative_motif = "G[CA]CTC"
    targetMotif = (positive_motif, negative_motif)
    fg_genome = SeqIO.parse("/home/wanghm/whm/1FG/35genome/Fusarium_graminearum.RR1_with_mito.fa", format="fasta")
    with open("/home/wanghm/whm/pacbio_data/Pacbio/PH-1/6mA/official_methylationResult/6mAmotifPos.bed","w+") as f:
        for chr in fg_genome:
            for index,motif in enumerate(targetMotif):
                for i in search_motif(str(chr.seq), motif):
                    start = i[0]
                    end = i[1]
                    if index == 0:
                        output = chr.id+"\t"+str(start)+"\t"+str(end)+"\t"+"*"+"\t"+"*"+"\t"+"+"+"\t"+"\n"
                        f.write(output)
                        print(output)
                    else:
                        output = chr.id+"\t"+str(start)+"\t"+str(end)+"\t"+"*"+"\t"+"*"+"\t"+"-"+"\t"+"\n"
                        f.write(output)
                        print(output)


    # positive_motif = "GAG[GT]C"
    # negative_motif = "G[CA]CTC"

