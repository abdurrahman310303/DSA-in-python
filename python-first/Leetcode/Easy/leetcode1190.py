
class Solution:
    def reverseParentheses(self, s: str) -> str:

        stack = []
        for ch in s:
            if ch == ')':
                temp =[]
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()
                stack.extend(temp)
            else:
                stack.append(ch)
        return ''.join(stack)
                        
s = "(ed(et(oc))el)"

sol = Solution()

print(sol.reverseParentheses(s))


