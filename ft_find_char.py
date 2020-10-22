def ft_find_char(a, b):
    d = False
    x, y = 0, 0
    c = 0
    for i in b:
        c += 1
    for i in range(c):
        if b[i] == a and not d:
            x = i
            d = True
        elif b[i] == a:
            y = i
    if not d:
        return False
    elif y == 0:
        return x
    return x, y
