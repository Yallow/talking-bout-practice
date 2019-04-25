def merge_ranges(input_range_list):
    # create a new list to hold merged Range objects
    out_l = []
    u_bound = -1
    l_bound = -1
    
    for i in input_range_list:
        if u_bound == -1 and l_bound == -1:
            # initialize these variables with i
            l_bound = i.lower_bound
            u_bound = i.upper_bound
        if i.lower_bound > u_bound:
            out_l.append("["+str(l_bound)+","+str(u_bound)+"]")
            u_bound = i.upper_bound
            l_bound = i.lower_bound
            continue
        u_bound = i.upper_bound
    out_l.append("["+str(l_bound)+","+str(u_bound)+"]")
    return out_l
            
            