def ft_rev_num(a):
    b = a
    c = 0
    if a < 0:
        a = -a
        while a > 0:
            d = a % 10
            c = c * 10 + d
            a //= 10
        return -c

    while a > 0:
        d = a % 10
        c = c * 10 + d
        a //= 10
    return c



