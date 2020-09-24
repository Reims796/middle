import ft_pow as pw 
import ft_len_num as num


def ft_rev_bin_num(a):
    bc = f.ft_len_num(a)
    b = 0
    for i in range(bc):
        b += a % 10 *pw.ft_pow(2, i)
        a //= 10
    return b
