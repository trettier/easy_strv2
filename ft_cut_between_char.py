def ft_cut_between_char(a, b):
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
        return -2
    elif y == 0:
        return -1
    fin = ""
    for i in range(c):
        if i < x:
            fin += b[i]
        elif i > y:
            fin += b[i]
    return fin


#print(ft_cut_between_char())