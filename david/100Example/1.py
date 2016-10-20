for x in range(1, 5):
    for y in range(1, 5):
        if (x != y):
            for z in range(1, 5):
                if ((x != z) & (y != z)):
                    print str(x)+str(y)+str(z)
