import time
from operator import itemgetter
def advantageCount(A,B):
    res_A = [0]*len(A)
    A.sort()
    print("A:",A)
    index_list = []
    for index,i in enumerate(A):   # 遍历列表A
        aa = [i - j for j in B]
        print(aa,"i:",i,"index:",index)
        positive = [mi for mi in aa if mi >0]
        if positive:
            idx = aa.index(min(positive))
            if idx in index_list:
                idx = aa.index(sorted(B)[1])
            print("idx:",idx)
            index_list.append(idx)
        else:
            tmpMaxIndex = B.index(max(B))
            index_list.append(tmpMaxIndex)
            print("tmpMaxIndex:",tmpMaxIndex)
        print("index_list:", index_list)
        res_A[index_list[index]] = i

    # print("index_list:",index_list)
    # ll = [k for k in zip(index_list, A)]
    # ll = sorted(ll, key=itemgetter(0))
    # return [s[1] for s in ll ]
    return "resA:",res_A
    # res = []

    # A.sort()
    # for b in B:
    #     if A[0] > b or A[-1] <= b:
    #         res.append(A[0])
    #         A.pop(0)
    #     else:  # 二分法查找大于b的最小值
    #         i, j = 0, len(A) - 1
    #         while i < j - 1:
    #             mid = (j + i) / 2
    #             if A[mid] > b:
    #                 j = mid
    #             elif A[mid] <= b:
    #                 i = mid
    #         res.append(A[j])
    #         A.pop(j)
    # return res


if __name__ == "__main__":
    A = [0,1,2,2,4]
    B = [1,3,0,0,2]
    # result: [2, 0, 2, 1, 4]
            # [2, 0, 1, 2, 4]
    print(advantageCount(A,B))
