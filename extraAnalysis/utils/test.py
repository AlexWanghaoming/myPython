from Bio import SeqIO

seqs = SeqIO.parse("/home/wanghm/Desktop/ge.fasta", format="fasta")
records = SeqIO.to_dict(seqs)
# for i in records.values():
#     print(i)
from itertools import islice
def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)),())
# print(list(chunk(records.values(), 5000))[1][1])

# print(list(chunk(range(10),4)))

# print(tuple(islice(range(10), 4)))
print([i for i in zip([1,2,3],[1,2,3])])
# print(list(map(lambda x:x[0]+x[1], zip())))
181410.0, 183881.0, 183825.0, 184248.0, 184196.0, 185491.0,
