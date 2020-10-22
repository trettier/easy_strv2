def ft_find_second_char(a, b):
    c = -2
    d = 0
    fin = False
    for i in b:
        d += 1
    for i in range(d):
        if b[i] == a and not fin:
            fin = True
            c = -1
        elif b[i] == a and fin:
            c = i
            break
    return c

# ft_reverse_between_char
