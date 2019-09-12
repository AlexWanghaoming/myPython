def numberOfArithmeticSlices(A):
    a = []
    for i in range(len(A)-1):
        a.append(A[i+1] - A[i])

    start = a[0]
    count = 0
    conti = 0
    for j in range(1,len(a)):
        tmp = a[j]
        if start == tmp:
            count += 1
            conti += 1
        else:
            start = tmp
            for k in range(conti):
                count = count + k
            conti = 0
    for aa in range(conti):
        count = count + aa
    return count

if __name__ == '__main__':
    A = [1,2,3,5,6,7,8]
    print(numberOfArithmeticSlices(A))