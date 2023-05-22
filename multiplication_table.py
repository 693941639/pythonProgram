for i in range(1, 10):
    j = 1
    while j <= i :
        print("{} * {} = {} ".format(j, i, i * j), end = "")
        j += 1        
    print()