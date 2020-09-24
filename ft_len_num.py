def ft_len_num(a):
    b = 0
    if a < 0:
        a = -a
    while a > 0:
        b += 1
        a //= 10
    return b
