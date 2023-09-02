
def get_century(year):
    century = year // 100
    century += 1

    if century > 10 and century < 20:
        century_str = f'{century}th'
    else:
        if century % 10 == 1:
            century_str = f'{century}st'
        elif century % 10 == 2:
            century_str = f'{century}nd'
        elif century % 10 == 3:
            century_str = f'{century}rd'
        else:
            century_str = f'{century}th'
    return century_str

print(get_century(1221))
