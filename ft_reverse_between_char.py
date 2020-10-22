def ft_reverse_between_char(a, b):
    c = -2
    d = 0
    x = 0
    y = 0
    fin2 = ''
    fin = False
    for i in b:
        d += 1
    for i in range(d):
        if b[i] == a and not fin:
            fin = True
            c = -1
            x = i
        elif b[i] == a and fin:
            c = i
            y = i
    if c < 0:
        return c
    for i in range(x):
        fin2 += b[i]
    for i in range(y, x, -1):
        fin2 += b[i]
    for i in range(y, d):
        fin2 += b[i]
    return fin2
