def scoreOfString(s):

    if not s:
        return 0
    
    score = 0

    for i in range(len(s)-1):
        score += abs(ord(s[i])-ord(s[i+1]))
    return score

s = 'hello'
print(str(scoreOfString(s)))