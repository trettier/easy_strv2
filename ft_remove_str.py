def ft_remove_str(a, b):
    c = ""
    for i in a:
        t = True
        for j in b:
            if j == i:
                t = False
        if t:
            c += i
    if c == a:
        return False
    return c
