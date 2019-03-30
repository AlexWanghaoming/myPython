from Bio import SeqIO
from Bio import Seq

genome = SeqIO.parse("/home/wanghm/whm/1FG/35genome/ph1_final.fasta",format="fasta")
fg = SeqIO.to_dict(SeqIO.parse("/home/wanghm/whm/1FG/35genome/fg_polished.fasta",format="fasta"))
# print(fg["3"].seq[4808938])
new_list = []
for seq in genome:
    sequence = seq.seq
    if seq.id == "correct_chr1":
        # print(sequence[2265575:2265630]) # del
        new_chr1 = sequence[:2265575] + sequence[2265630:]
        ss=SeqIO.SeqRecord(seq=Seq.Seq(str(new_chr1)),description="length=%d"%(len(new_chr1)),id="correct_chr1")
        new_list.append(ss)
    if seq.id == "correct_chr2":
        new_list.append(seq)
    if seq.id == "correct_chr3":
        # print(seq.description)
        new_chr3 = sequence[:4808089] + fg["3"].seq[4808392:4808939] + sequence[4808089:]
        ss=SeqIO.SeqRecord(seq=Seq.Seq(str(new_chr3)),description="length=%d"%(len(new_chr3)),id="correct_chr3")
        new_list.append(ss)
    if seq.id == "correct_chr4":
        new_chr4 = sequence[:5049039] + sequence[5049062:5061325] + sequence[5061354:6970430] + fg["4"].seq[6970454:6970578] + sequence[6970430:]
        print(sequence[5049039],sequence[5049061],sequence[5061325], sequence[5061353],sequence[6970429], fg["4"].seq[6970454], fg["4"].seq[6970577])
        ss=SeqIO.SeqRecord(seq=Seq.Seq(str(new_chr4)),description="length=%d"%(len(new_chr4)),id="correct_chr4")
        new_list.append(ss)
    if seq.id == "Mt":
        new_list.append(seq)
SeqIO.write(new_list,"/home/wanghm/whm/resequence/wanghm_ph1.fasta", "fasta")
