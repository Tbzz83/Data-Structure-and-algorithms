def quicksort(array):
    length = len(array)
    if length <= 1:
        return array
    else:
        pivot = array.pop() # Pops the original array until

    items_greater = []
    items_lower = []
    for item in array:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quicksort(items_lower) + [pivot] + quicksort(items_greater)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quicksort(test))