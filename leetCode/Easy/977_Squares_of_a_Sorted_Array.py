class Solution(object):
    def sortedSquares(self, nums):
        answer = list(map(lambda x : x**2, nums))
        answer.sort()
        return answer