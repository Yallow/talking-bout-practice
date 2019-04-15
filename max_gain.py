def max_gain(input_list):    
    max = input_list[1] - input_list[0]
    min = input_list[0]
    i = 1
    while i < len(input_list):
        if (input_list[i] - min > max):
            max = input_list[i] - min
        if (input_list[i] < min):
            min = input_list[i]
        i = i+1
    return 0 if max < 0 else max