class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        lenOfHayStack = len(haystack)
        lenOfNeedle = len(needle)

        for i in range(lenOfHayStack - lenOfNeedle +1):

            if haystack[i:i + lenOfNeedle] == needle:
                print(haystack[i:i + lenOfNeedle])
                return i
        
        return -1


sol = Solution()

index = sol.strStr("butsadsad","sad")

print("The index of the first occurence is : " + str(index))