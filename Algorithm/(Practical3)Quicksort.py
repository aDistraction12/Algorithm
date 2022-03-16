def quicksort (arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop()

    high_list = []
    low_list = []

    for item in arr:
        if item > pivot:
            high_list.append(item)
        else:
            low_list.append(item)


    return quicksort(low_list) + [pivot] + quicksort(high_list)

print(quicksort([5,9,3,8,1,0,2]))
