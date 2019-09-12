from Bio import SeqIO
import argparse
import random


def main():
    parse = argparse.ArgumentParser(description='Shuffle fastq file into random parts')
    parse.add_argument('-f1', dest='fastq1', required=True, help='fastq file 1')
    parse.add_argument('-f2', dest='fastq2', required=True, help='fastq file 2')
    parse.add_argument('-n', dest='num', required=True, help='number of parts')
    parse.add_argument('-o', dest='out', required=True, help='output path')
    args = parse.parse_args()
    out = args.out
    f1 = args.fastq1
    f2 = args.fastq2
    n = int(args.num)

    fq1 = SeqIO.parse(f1, 'fastq')
    fq2 = SeqIO.parse(f2, 'fastq')
    tank = []
    name = []
    for i in range(n):
        tank.append([])
        name.append(i)

    try:
        for i in zip(fq1, fq2):
            random.choice(tank).append(i)
    except ValueError:
        pass

    for list_1 in tank:
        list_2 = [i for j in list_1 for i in j]
        SeqIO.write(list_2, '{}reault_{}'.format(out + '/', name.pop()), 'fastq')

    print('Finashed!')


if __name__ == '__main__':
    main()
