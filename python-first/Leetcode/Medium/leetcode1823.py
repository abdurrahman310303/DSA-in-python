class Solution:
    def findTheWinner(self,n,k):
        people = list(range(1,n+1))

        index = 0

        while len(people) > 1:
            index = (index+k-1) %len(people)

            people.pop(index)

        return people[0]

sol = Solution()

print(sol.findTheWinner(5,2))