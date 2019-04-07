def is_palindrome(input_string):
    # save the reverse input string in a new list for later comparison
    r_pal = []
    for l in list(input_string):
        r_pal.insert(0,l)
    if "".join(r_pal) is input_string:
        return True
    else:
        return False