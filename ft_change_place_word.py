def ft_change_place_word(a):
    b = True
    c, d = "", ""
    for i in a:
        if i != " " and b:
            c += i
        elif i != " " and not b:
            d += i
        else:
            b = False
    d += " "
    return d + c
