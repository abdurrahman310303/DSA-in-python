class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                # Move the left pointer to the right of the duplicate character
                left = char_index[s[right]] + 1
            
            # Update the last seen index of the character
            char_index[s[right]] = right
            
            # Update the maximum length found
            max_length = max(max_length, right - left + 1)
        
        return max_length