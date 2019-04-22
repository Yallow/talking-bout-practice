def unique_chars_in_string(input_string):
    # loop through string
    # create a dictionary entry for each letter
    # check if any letter has more than 1
    
    str_dict = {}
    # init the dictionary
    for i in range(len(input_string)):
        str_dict[input_string[i]] = 0
    for i in range(len(input_string)):
        str_dict[input_string[i]] += 1
        if str_dict[input_string[i]] > 1:
            return False
    return True