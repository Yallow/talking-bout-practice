def merge_sort(l):
    if len(l) == 1:
        return l

    result = []

    mid = int(len(l)/2)
    # move all the way down the list
    x = merge_sort(l[:mid])
    y = merge_sort(l[mid:])

    # loop through the new lists and pop/append the smaller numbers
    while (len(x) > 0) and (len(y) > 0):
        if x[0] > y[0]:
            result.append(y[0])
            y.pop(0)
        else:
            result.append(x[0])
            x.pop(0)
    # append the final items of the lists
    result += x
    result += y
    return result

l = [4, 3, 10, 17, 1, 4, 99, 0]
print(merge_sort(l))