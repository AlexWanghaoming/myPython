from Bio import SeqIO
from Bio import Seq
import time
import re

ref_genome = SeqIO.parse("/home/wanghm/whm/1FG/35genome/Fusarium_graminearum.RR1_with_mito.fa", 'fasta')
fg_genome = SeqIO.parse("/home/wanghm/whm/1FG/35genome/fg_polished.fasta","fasta")

corrected_chrom_seq = []
for ref,fg in zip(ref_genome,fg_genome):
    with open("/home/wanghm/whm/resequence/correctionResult") as f:
        for linenumber,interval in enumerate(f):
            # if interval.split()[0] == "1" and ref.id == "1":
            #     if linenumber == 2:  # first line
            #         flag = 0
            #     elif linenumber == 115:
            #         ref_mappingSeq_end = int(interval.split()[1].split("-")[0]) - 1
            #         mappingSeq = ref.seq[flag:ref_mappingSeq_end]
            #         tailing_start = int(interval.split()[1].split("-")[0]) - 1
            #         tailing_end = int(interval.split()[1].split("-")[1])
            #         tailingSeq = ref.seq[tailing_start:tailing_end]
            #         corrected_chrom_seq.append(str(mappingSeq))
            #         corrected_chrom_seq.append(str(tailingSeq))
            #     elif interval.split()[3] == "ref":
            #         print(interval)
            #     elif interval.split()[3] == "fg" and "*" not in interval.split():
            #         ref_mappingSeq_end = int(interval.split()[1].split("-")[0]) -1
            #         # print(flag,ref_mappingSeq_end)
            #         mappingSeq = ref.seq[flag:ref_mappingSeq_end]
            #         interval_start = int(interval.split()[2].split("-")[0]) -1
            #         interval_end = int(interval.split()[2].split("-")[1])
            #         intervalSeq = fg.seq[interval_start:interval_end]
            #
            #         corrected_chrom_seq.append(str(mappingSeq))
            #         corrected_chrom_seq.append(str(intervalSeq))
            #         flag = int(interval.split()[1].split("-")[1])
            #     elif interval.split()[3] == "fg" and "*" in interval.split():
            #         errorsite = int(interval.split()[6]) - 1
            #         if interval.split()[7] == "DEL":
            #             seq1 = ref.seq[flag:errorsite]
            #             corrected_chrom_seq.append(str(seq1))
            #             flag = errorsite + 1
            #         else:
            #             seq1 = ref.seq[flag:errorsite + 1]
            #             corrected_chrom_seq.append(str(seq1))
            #             insertion = "C"
            #             corrected_chrom_seq.append(insertion)
            #             flag = errorsite + 1
            # if interval.split()[0] == "2" and ref.id == "2":
            #     if linenumber == 116:  # first line
            #         interval_start = int(interval.split()[1].split("-")[0]) -1
            #         interval_end = int(interval.split()[1].split("-")[1])
            #         intervalSeq = ref.seq[interval_start:interval_end]
            #         corrected_chrom_seq.append(str(intervalSeq))
            #         flag = 653
            #     elif linenumber == 182:
            #         ref_mappingSeq_end = int(interval.split()[1].split("-")[0]) - 1
            #         mappingSeq = ref.seq[flag:ref_mappingSeq_end]
            #         tailing_start = int(interval.split()[1].split("-")[0]) - 1
            #         tailing_end = int(interval.split()[1].split("-")[1])
            #         tailingSeq = ref.seq[tailing_start:tailing_end]
            #         corrected_chrom_seq.append(str(mappingSeq))
            #         corrected_chrom_seq.append(str(tailingSeq))
            #     elif interval.split()[3] == "ref":
            #         print(interval)
            #     elif interval.split()[3] == "fg" and "*" not in interval.split():
            #         ref_mappingSeq_end = int(interval.split()[1].split("-")[0]) -1
            #         # print(flag,ref_mappingSeq_end)
            #         mappingSeq = ref.seq[flag:ref_mappingSeq_end]
            #         interval_start = int(interval.split()[2].split("-")[0]) -1
            #         interval_end = int(interval.split()[2].split("-")[1])
            #         intervalSeq = fg.seq[interval_start:interval_end]
            #
            #         corrected_chrom_seq.append(str(mappingSeq))
            #         corrected_chrom_seq.append(str(intervalSeq))
            #         flag = int(interval.split()[1].split("-")[1])
            #     elif interval.split()[3] == "fg" and "*" in interval.split():
            #         errorsite = int(interval.split()[6]) - 1
            #         if interval.split()[7] == "DEL":
            #             seq1 = ref.seq[flag:errorsite]
            #             corrected_chrom_seq.append(str(seq1))
            #             flag = errorsite + 1
            #         else:
            #             seq1 = ref.seq[flag:errorsite + 1]
            #             corrected_chrom_seq.append(str(seq1))
            #             insertion = "C"
            #             corrected_chrom_seq.append(insertion)
            #             flag = errorsite + 1
            # if interval.split()[0] == "3" and ref.id == "3":
            #     if linenumber == 183:  # first line
            #         # interval_start = int(interval.split()[1].split("-")[0]) -1
            #         # interval_end = int(interval.split()[1].split("-")[1])
            #         # intervalSeq = ref.seq[interval_start:interval_end]
            #         # corrected_chrom_seq.append(str(intervalSeq))
            #         flag = 0
            #     elif linenumber == 235:
            #         ref_mappingSeq_end = int(interval.split()[1].split("-")[0]) - 1
            #         mappingSeq = ref.seq[flag:ref_mappingSeq_end]
            #         tailing_start = int(interval.split()[1].split("-")[0]) - 1
            #         tailing_end = int(interval.split()[1].split("-")[1])
            #         tailingSeq = ref.seq[tailing_start:tailing_end]
            #         corrected_chrom_seq.append(str(mappingSeq))
            #         corrected_chrom_seq.append(str(tailingSeq))
            #     elif interval.split()[3] == "ref":
            #         print(interval)
            #     elif interval.split()[3] == "fg" and "*" not in interval.split():
            #         ref_mappingSeq_end = int(interval.split()[1].split("-")[0]) -1
            #         # print(flag,ref_mappingSeq_end)
            #         mappingSeq = ref.seq[flag:ref_mappingSeq_end]
            #         interval_start = int(interval.split()[2].split("-")[0]) -1
            #         interval_end = int(interval.split()[2].split("-")[1])
            #         intervalSeq = fg.seq[interval_start:interval_end]
            #
            #         corrected_chrom_seq.append(str(mappingSeq))
            #         corrected_chrom_seq.append(str(intervalSeq))
            #         flag = int(interval.split()[1].split("-")[1])
            #     elif interval.split()[3] == "fg" and "*" in interval.split():
            #         errorsite = int(interval.split()[6]) - 1
            #         if interval.split()[7] == "DEL":
            #             seq1 = ref.seq[flag:errorsite]
            #             corrected_chrom_seq.append(str(seq1))
            #             flag = errorsite + 1
            #         if interval.split()[7] == "DEL9":
            #             seq1 = ref.seq[flag:errorsite]
            #             corrected_chrom_seq.append(str(seq1))
            #             flag = errorsite + 9
            #         if interval.split()[7] == "DEL8":
            #             seq1 = ref.seq[flag:errorsite]
            #             corrected_chrom_seq.append(str(seq1))
            #             flag = errorsite + 8
            #         if interval.split()[7] == "DEL11":
            #             seq1 = ref.seq[flag:errorsite]
            #             corrected_chrom_seq.append(str(seq1))
            #             flag = errorsite + 11
            #         elif linenumber == 191:
            #             seq1 = ref.seq[flag:errorsite + 1]
            #             corrected_chrom_seq.append(str(seq1))
            #             insertion = "GGG"
            #             corrected_chrom_seq.append(insertion)
            #             flag = errorsite + 3
            #         elif linenumber == 220:
            #             seq1 = ref.seq[flag:errorsite + 1]
            #             corrected_chrom_seq.append(str(seq1))
            #             insertion = "TTTAATACT"
            #             corrected_chrom_seq.append(insertion)
            #             flag = errorsite + 9
            print(interval.split()[0],ref.id)
            if interval.split()[0] == "4" and ref.id == "4":
                if linenumber == 236:  # first line
                    # interval_start = int(interval.split()[1].split("-")[0]) -1
                    # interval_end = int(interval.split()[1].split("-")[1])
                    # intervalSeq = ref.seq[interval_start:interval_end]
                    corrected_chrom_seq.append("C")
                    flag = 1
                elif linenumber == 320:
                    ref_mappingSeq_end = int(interval.split()[1].split("-")[0]) - 1
                    mappingSeq = ref.seq[flag:ref_mappingSeq_end]
                    tailing_start = int(interval.split()[1].split("-")[0]) - 1
                    tailing_end = int(interval.split()[1].split("-")[1])
                    tailingSeq = ref.seq[tailing_start:tailing_end]
                    corrected_chrom_seq.append(str(mappingSeq))
                    corrected_chrom_seq.append(str(tailingSeq))
                elif interval.split()[3] == "ref":
                    print(interval)
                elif interval.split()[3] == "fg" and "*" not in interval.split():
                    ref_mappingSeq_end = int(interval.split()[1].split("-")[0]) -1
                    # print(flag,ref_mappingSeq_end)
                    mappingSeq = ref.seq[flag:ref_mappingSeq_end]
                    interval_start = int(interval.split()[2].split("-")[0]) -1
                    interval_end = int(interval.split()[2].split("-")[1])
                    intervalSeq = fg.seq[interval_start:interval_end]

                    corrected_chrom_seq.append(str(mappingSeq))
                    corrected_chrom_seq.append(str(intervalSeq))
                    flag = int(interval.split()[1].split("-")[1])
                elif interval.split()[3] == "fg" and "*" in interval.split():
                    errorsite = int(interval.split()[6]) - 1
                    if interval.split()[7] == "DEL":
                        seq1 = ref.seq[flag:errorsite]
                        corrected_chrom_seq.append(str(seq1))
                        flag = errorsite + 1
                    if interval.split()[7] == "DEL2":
                        seq1 = ref.seq[flag:errorsite]
                        corrected_chrom_seq.append(str(seq1))
                        flag = errorsite + 2
                    if interval.split()[7] == "DEL3":
                        seq1 = ref.seq[flag:errorsite]
                        corrected_chrom_seq.append(str(seq1))
                        flag = errorsite + 3
                    if interval.split()[7] == "DEL15":
                        seq1 = ref.seq[flag:errorsite]
                        corrected_chrom_seq.append(str(seq1))
                        flag = errorsite + 15
chromosome4 = "".join(corrected_chrom_seq)
f2 = open("/home/wanghm/whm/1FG/35genome/chromosome4.fa","w+")
f2.write(">correct_chr4 Length={0}".format(len(chromosome4))+"\n"+chromosome4)
f2.close()














