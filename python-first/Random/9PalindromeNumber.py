def palindrom(x:int) :

    xstr = str(x)

    return xstr == xstr[::-1]


print(palindrom(-123))