def ft_multi_num(a):
    b = 1
    if a < 0:
        a = -a

    while a > 0:
        b *= (a % 10)
        a //= 10
    return b
