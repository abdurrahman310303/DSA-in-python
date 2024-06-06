class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        lenofHaystack = len(haystack)
        lenofNeedle = len(needle)

        if not needle:
            return 0

        for i in range(lenofHaystack - lenofNeedle + 1):

            if haystack[i:i + lenofNeedle] == needle:
                return i
        
        return -1


sol = Solution()

index = sol.strStr("butsadsad","sad")

print("The index of the first occurence is : " + str(index))