def maxArea(height: list[int]) -> int:
    i = 0
    j = len(height) - 1
    res = []
    while (i < j):
        if height[i] < height[j]:
            aera = height[i] * (j - i)
            i = i + 1
            res.append(aera)
        else:
            aera = height[j] * (j - i)
            j = j - 1
            res.append(aera)

    return max(res)

if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(maxArea(height))