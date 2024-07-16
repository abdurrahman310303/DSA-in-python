class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        sign = (dividend < 0) ^ (divisor < 0)

        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        
        while dividend >= divisor:
     
            multiple = 1
            temp = divisor
            while temp <= dividend:
                temp <<= 1
                multiple <<= 1

            dividend -= temp >> 1
            quotient += multiple >> 1

        return -quotient if sign else quotient



sol = Solution()

result = sol.divide(200,2)

print (str(result))