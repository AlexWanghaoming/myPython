from Bio import SeqIO
import time

official_genome = SeqIO.parse("/home/wanghm/whm/1FG/35genome/Fusarium_graminearum.RR1_with_mito.fa", format="fasta")
fg_genome = SeqIO.parse("/home/wanghm/whm/pacbio_data/Pacbio/PH-1/6mA/fg_polished.fasta", format="fasta")
interval_pos = open("/home/wanghm/whm/pacbio_data/Pacbio/PH-1/check_genome/interval/mummer_interval", "r+")
handle = open("/home/wanghm/whm/pacbio_data/Pacbio/PH-1/check_genome/interval/intervalSeq.fasta", "w+")


def correct():
    if fg_interval_start > fg_interval_end:
        fg_interval_region = (fg_interval_end, fg_interval_start)
    else:
        fg_interval_region = (fg_interval_start, fg_interval_end)
    if rf_interval_start > rf_interval_end:
        official_interval_region = (rf_interval_end, rf_interval_start)
    else:
        official_interval_region = (rf_interval_start,rf_interval_end)

    print("fg_genome in IGV:{0}:{1}-{2}".format(chrom, fg_interval_region[0], fg_interval_region[1]))
    print("official in IGV:{0}:{1}-{2}".format(chrom, official_interval_region[0], official_interval_region[1]))
    print("Now interval sequences in official genome is {0};interval sequences in fg genome is {1}.".format(
        rf_chrom.seq[official_interval_region[0] - 1: official_interval_region[1]],
        fg_chrom.seq[fg_interval_region[0] - 1: fg_interval_region[1]]))
    choice2 = input("Please choose which is right: Official genome(a) or Ours fg(b)?\n")
    if choice2 == "a":
        sequence2 = rf_chrom.seq[official_interval_region[0] - 1: official_interval_region[1]]
        seq2 = SeqIO.SeqRecord(sequence2, id="rf_{0}:{1}-{2}".format(chrom, official_interval_region[0],
                                                                     official_interval_region[1]), description="")
    if choice2 == "b":
        sequence2 = fg_chrom.seq[fg_interval_region[0] - 1: fg_interval_region[1]]
        seq2 = SeqIO.SeqRecord(sequence2,
                               id="fg_{0}:{1}-{2}".format(chrom, fg_interval_region[0], fg_interval_region[1]),
                               description="")
    SeqIO.write(seq2, handle, "fasta")


i = 0
for rf_chrom, fg_chrom in zip(official_genome, fg_genome):
    i = i + 1
    j = 0
    for interval in interval_pos:
        chrom = interval.split("\t")[0]
        rf_interval_start = int(interval.split("\t")[1])
        rf_interval_end = int(interval.split("\t")[2])
        fg_interval_start = int(interval.split("\t")[3])
        fg_interval_end = int(interval.split("\t")[4])

        if chrom == rf_chrom.id == fg_chrom.id:
            j = j + 1
            print("Now:{0}-{1}".format(i, j))
            if j == 1:  # if chromosomes begining lack bases
                chromsomehead = fg_interval_start - rf_interval_start
                if chromsomehead > 0:
                    print("fg_genome in IGV:{0}:{1}-{2}".format(chrom, 1, chromsomehead))
                    choice = input("Please choose which is right: Official genome(a) or Ours fg(b)?\n")
                    if choice == "a": # if official is short at begining but fg's begining is wrong,write a blank fasta
                        SeqIO.write(SeqIO.SeqRecord(seq=fg_chrom.seq[0:0],id="NAN"),handle,"fasta")
                    if choice == "b":
                        sequence = fg_chrom.seq[0:fg_interval_start - rf_interval_start]
                        # SeqIO.SeqRecord(sequence)
                        # print(SeqIO.SeqRecord)
                        seq = SeqIO.SeqRecord(sequence, id="fg_{0}:{1}-{2}".format(chrom, 1, chromsomehead),
                                              description="")
                        SeqIO.write(seq, handle, "fasta")
                if chromsomehead < 0:
                    print("official in IGV:{0}:{1}-{2}".format(chrom, 1, abs(chromsomehead)))
                    choice = input("Please choose which is right: Official genome(a) or Ours fg(b)?\n")
                    if choice == "a": # if official is short at begining but fg's begining is wrong,write a blank fasta
                        sequence = rf_chrom.seq[0:rf_interval_start - fg_interval_start]
                        seq = SeqIO.SeqRecord(sequence, id="rf_{0}:{1}-{2}".format(chrom, 1, abs(chromsomehead)),
                                              description="")
                        SeqIO.write(seq, handle, "fasta")
                    if choice == "b":
                        SeqIO.write(SeqIO.SeqRecord(seq=rf_chrom.seq[0:0],id="NAN"),handle,"fasta")
                correct()
            if j != 1:  # for interval in mummer_interval2:
                correct()
        # if rf_chrom.id == fg_chrom.id
# SeqIO.write("TATNCNTG","/home/wanghm/whm/1FG/35genome/aa",format="fasta")
