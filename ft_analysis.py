def ft_analysis(str_):
    print(str_[2])
    print(str_[-2])
    print(str_[:5])
    print(str_[:-2])
    print(str_[::2])
    print(str_[1::2])
    print(str_[::-1])
    print(str_[::-2])
    c = 0
    for i in str_:
        c += 1
    print(c)
