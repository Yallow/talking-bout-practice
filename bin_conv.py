"""
By increasing the mult_c variable by 10x, we can keep incrementing forward
The number modulus 2 will always either return a 0 or a 1
When dividing by 2, we are replicating how binary notation is setup
"""
def main():
    dec_to_bin(5)

def dec_to_bin(number):
    mult_c = 1
    bin_ret = 0
    while number >= 2:
        bin_ret += (number%2)*mult_c
        number = int(number/2)
        mult_c *= 10
    bin_ret += (number%2)*mult_c
    return bin_ret

main()
