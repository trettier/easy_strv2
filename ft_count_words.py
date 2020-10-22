def ft_count_words(str_):
    a = 1
    t = False
    for i in str_:
        if i != " ":
            t = True
        if i == " " and t:
            a += 1
            t = False
    return a
