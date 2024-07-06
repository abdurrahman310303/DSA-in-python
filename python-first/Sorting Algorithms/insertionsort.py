def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:

            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

nums=[1,3,23,5423,363,43,-2,424312,0,3,5]

print(insertionSort(nums))