from Bio import SeqIO
import time

seqs1 = SeqIO.parse("/home/wanghm/whm/pacbio_data/Pacbio/YDJ-3/ydj_canu_result/ydj.contigs.fasta", "fasta")
f = open("/home/wanghm/whm/ngs/ydj_blast_E_value/contigs_name", "r").readlines()
print(len(f))
unplut_list = []
name_list = []
for i in f:
	name_list.append(i.strip("\n"))
for seq1 in seqs1:
	if seq1.id in name_list:
		unplut_list.append(seq1)
SeqIO.write(unplut_list, "/home/wanghm/yjd.contigs.fasta", "fasta")

# seq2 = SeqIO.parse("/home/wanghm/whm/pacbio_data/Pacbio/YDJ-3/ydj_canu_result/ydj.contigs.fasta","fasta")
# totalLength = 0
# for seq in seq2:
# 	print(len(seq.seq))
# 	totalLength = totalLength + len(seq.seq)
#
# print(totalLength)

# seqs2 = SeqIO.parse("/home/wanghm/whm/pacbio_data/Pacbio/PH-1/polish/canuRes_polish.fasta", "fasta")
# i = 0
# for seq2l in seqs2:
# 	print(seq2.id+":"+str(len(seq2)))
# 	i = i + len(seq2)
# print(i)
# seqs = SeqIO.parse("/home/wanghm/whm/pacbio_data/Pacbio/YDJ-3/ydj_canu_result/ydj.contigs.fasta", 'fasta')
# polluted_seqList = []
# for seq in seqs:
#     print(seq.id)

