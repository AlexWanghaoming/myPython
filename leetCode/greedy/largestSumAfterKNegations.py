def largestSumAfterKNegations(A, K):
    for i in range(K):
        idx = A.index(min(A))
        A[idx] = -A[idx]
    return sum(A)
if __name__ == '__main__':
    A= [4,2,3]

    K=2
    print(largestSumAfterKNegations(A,K))