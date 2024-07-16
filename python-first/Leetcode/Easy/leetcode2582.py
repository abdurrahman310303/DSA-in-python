def passThePillow(n,time):

    index = 1
    direction = 1

    for i in range(time):
        if direction == 1:
            index += 1
            if index == n:
                direction = -1
        else:
            if direction == -1:
                index -=1
                if index == 1:
                    direction = -1
    return index

print(passThePillow(4,6))