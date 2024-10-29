for i in range(3, 21):
    s = ''
    for o in range(1, i):
        for g in range(o + 1, i):
            if i % (o + g) == 0:
                s += str(o) + str(g)
    print(i, s)