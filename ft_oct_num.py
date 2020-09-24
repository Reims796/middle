def ft_oct_num(a):
    b = 1
    c = 0
    while a > 0:
        c += a % 8 * b
        b *= 10
        a //= 8
    return c
