# map the numbers first
num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
            (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def solution(n):
    rom_num = ''
    while n > 0:
        for i in num_map:
            q, n = divmod(n,i[0])
            if q >= 1:             
                rom_num += i[1]*q   
    return rom_num