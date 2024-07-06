from collections import Counter

def common_chars(words):
    if not words:
        return []

    # Initialize the counter with the first word's characters
    common_count = Counter(words[0])
    
    # Update the counter with the intersection of the subsequent words
    for word in words[1:]:
        common_count &= Counter(word)
    
    # Expand the common characters according to their counts
    common_chars_list = list(common_count.elements())
    
    return common_chars_list

# Example usage:
words = ["bella", "label", "roller"]
print(common_chars(words))  # Output: ['l', 'l', 'e']
