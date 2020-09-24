def ft_min_num(a):
    b = (a % 10)
    while a > 0:
        if b < (a % 10):
            b = (a % 10)
        a //= 10
    return b
