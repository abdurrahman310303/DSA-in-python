def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    return arr

nums = [12,42,12,-4,23,-5,-12,43,93,56,25,64,2,56,3,2,45,2,2,2,]

print("Orignal Array:",end=" ")
print(nums)
print("Sorted Array:",end=" ")
print(bubble_sort(nums))