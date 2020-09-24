def ft_sum_num(a):
    b = 0
    while a > 0:
        b += (a % 10)
        a //= 10
    return b

