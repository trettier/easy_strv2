def ft_count_words(str_):
    a = 1
    for i in str_:
        if i == " ":
            a += 1
    return a
