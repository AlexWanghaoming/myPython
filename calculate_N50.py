from Bio import SeqIO
import argparse

def calculate_N50(fasta_file):
    seqs = SeqIO.parse(fasta_file,"fasta")
    seqs_length = []
    for seq in seqs:
        seqs_length.append(len(seq))
    sum_length = sum(seqs_length)
    goal_length = 0
    i = 0
    while (goal_length >= sum_length / 2):
        i += 1
        goal_length = goal_length + sorted(seqs_length)[i]
    return seqs_length[i]


parse = argparse.ArgumentParser(description="wanghm haha")
parse.add_argument('-fa', '--fasta_file', dest='fasta', help="please use contig/scaffold fasta file")
options = parse.parse_args()

if __name__ == "__main__":
    print("N50 is {0}".format(calculate_N50(options.fasta)))


