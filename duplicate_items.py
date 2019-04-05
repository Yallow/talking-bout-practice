def duplicate_items(list_numbers):
    """
    sort the original list
    loop through the original list
    setup a separte list containing duplicates
    """
    dup_list = []
    list_numbers.sort()
    for x in list_numbers:
        if list_numbers.count(x) > 1 and x not in dup_list:
            dup_list.append(x)
    return dup_list
