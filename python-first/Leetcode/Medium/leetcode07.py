class Solution:
    def reverse(self, x: int) -> int:

        negative = 0

        if x < 0:

            negative = x
        
        xstr = str(abs(x))

        xstr = xstr[::-1]

        xint = int(xstr)

        if negative:
            xint = -xint
        if xint < -2**31 or xint > 2**31 - 1:
            return 0
        return xint
        