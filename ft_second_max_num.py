def ft_second_max_num(a):
    b = 0
    c = 0
    d = a
    while d > 0:
        if b < d % 10:
            b = d % 10
        d //= 10

    while a > 0:
        if b >= c < a % 10:
            c = a % 10
        a //= 10

    return c
