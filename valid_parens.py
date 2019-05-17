def valid_parentheses(string):
    left_par = right_par = 0
    # even number of open and close parens
    if string.count("(") != string.count(")"):
        return False
    for c in string:
        if c==")" : right_par+=1
        if c=="(" : left_par+=1
        
        if right_par > left_par:
            return False
    return True