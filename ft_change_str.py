def ft_change_str(a, b, c):
    d = 0
    for i in c:
        d += 1
    fin = ""
    x = 0
    for i in a:
        x += 1
    y = 0
    for i in range(d):
        if y == 0:
            if c[i] != a[0]:
                fin += c[i]
            else:
                t = True
                if x + 1 < d:
                    for j in range(i, x):
                        if a[j - i] != c[j]:
                            t = False
                            break
                if t:
                    fin += b
                    y = x - 1
                else:
                    fin += c[i]
        else:
            y -= 1
    if fin == c:
        return False
    return fin
