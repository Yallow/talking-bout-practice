def main():
    reverse_string("madman")

def reverse_string(a_string):
    # new array for reversed string
    str_rev = []
    # walk through the string like an array
    for c in list(a_string):
        str_rev.insert(0, c)

    return "".join(str_rev)

main()
