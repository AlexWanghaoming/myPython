# 冒泡排序 O(n^2)
def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


#选择排序 O(n^2)
def selectionSort(arr):

    for i in range(len(arr) - 1):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


# 插入排序 O(n^2)

def insertionSort(arr):
    for i in range(len(arr)):
        print(i)
        preIndex = i-1
        print("preIndex:", preIndex)

        current = arr[i]
        print("current:", current)

        while preIndex >= 0 and arr[preIndex] > current:
            print("preIndex:", preIndex)

            arr[preIndex+1] = arr[preIndex]
            preIndex-=1
            print("preIndex:", preIndex)

        arr[preIndex+1] = current
        print("current:", current)

    return arr


if __name__ == '__main__':
    print(insertionSort([1,7,3,5,4]))