def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

for i in range(5):
    print(i)

def selectionSort(arr):
    for i in range(len(arr) - 1):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if i!= minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr
