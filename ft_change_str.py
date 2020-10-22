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
                    print(i, x)
                    for j in range(i, x):
                        print(j, a[j - i], c[j])
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
    if fin == a:
        return False
    return fin
