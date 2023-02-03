def binary_search(input_array, value):

    l = 0
    u = len(input_array) - 1

    while l <= u:
        mid = (l+u) // 2
        if input_array[mid] == value:
            return True

        else:
            if input_array[mid] < value:
                l = mid + 1
            else:
                u = mid - 1

    return False


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15


print(binary_search(test_list, test_val1))
print
binary_search(test_list, test_val2)