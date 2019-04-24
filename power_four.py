def is_power_of_four(number):
    # keep dividing by 4 until it equals 1
    # if its any non-zero modulus, its not a power of four
    if number == 0:
        return False
    while number != 1:
        if number%4 != 0:
            return False
        number /= 4
    return True