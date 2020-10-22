def ft_division_str(a):
    b = 0
    for i in a:
        b += 1
    if b % 2 == 1:
        c = a[b // 2 + 1:] + a[:b // 2 + 1]
    else:
        c = a[b // 2:] + a[:b // 2]
    return c
