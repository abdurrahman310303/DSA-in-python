def minOperations(logs):

    depth = 0

    for log in logs:
        if log =='../':
            if depth > 0:
                depth -= 1
        elif log == './':
            continue
        else:
            depth += 1
    return depth
logs = ['d11/','../','d2/','./','../','d4/']

print(minOperations(logs))