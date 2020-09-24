def ft_null_count(a):
    b = 0
    if a < 0:
        a = -a

    while a > 0:
        if a % 10 == 0:
            b += 1
        a //= 10
    return b
