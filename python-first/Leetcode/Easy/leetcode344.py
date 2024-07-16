class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()  # Reverses the list in-place
        print(s)

sol = Solution()

x = ["h", "e", "l", "l", "o"]

sol.reverseString(x)
