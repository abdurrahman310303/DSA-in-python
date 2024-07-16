from collections import Counter

def common_chars(words):

    if not words:
        return []
    
    chars_count = Counter(words[0])

    for word in words:

        chars_count &= Counter(word)

    return list(chars_count.elements())


words = ['bella','hello','cello']
common_elements = common_chars(words)

print(common_elements)