def rotate_left(list_numbers,k):
    # move the first k items to the end of the array
    i = 0
    while i < k:
        # pop off the value and append it to the end
        move_val = list_numbers.pop(0)
        list_numbers.append(move_val)
        i += 1
        print(list_numbers)
    return list_numbers

fun_list = [1,2,3,4,5,6,7,8,9]
rotate_left(fun_list, 14)
