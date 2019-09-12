from heapq import heapify, heappush, heappop
from itertools import count

def huffman(seq, frq):
    num = count()
    trees = list(zip(frq, num, seq))
    # print(trees)
    heapify(trees)
    while len(trees) > 1:
        fa, _, a = heappop(trees)
        fb, _, b = heappop(trees)
        print("tree:",trees)
        print(num)
        n=next(num)
        print("n:",n)
        heappush(trees, (fa+fb, n, [a, b]))
        print(trees)
    return trees[0][-1]

if __name__ == '__main__':
    seq = "abcdefgi"
    frq = [4,5,6,9,11,12,15,16,20]
    print(huffman(seq, frq))
