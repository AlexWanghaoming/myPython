def lastStoneWeight(stones):
    count = len(stones)
    # print(stones[len(stones)-2:len(stones)])
    while count>1:
        stones.sort(reverse=True)
        max_2 = stones[0:2]
        stones.pop(0)
        stones.pop(0)
        left = max_2[0] - max_2[1]
        if left != 0:
            count = count - 1
            stones.append(left)
        else:
            count = count - 2
        print(stones)
    try:
        return stones[0]
    except:
        return 0


if __name__ == '__main__':
    stones = [2,2]
    print(lastStoneWeight(stones))
