class Solution:
    '''
    CASE 0
    nums = [4,5,2,1]
    quries = [3,10,21]
    output = [2,3,4]

    CASE 1
    nums = [2,3,4,5]
    quries = [1]
    output = [0]

    Runtime: 339 ms, faster than 52.03% 
    Memory Usage: 14.2 MB, less than 41.46%
     '''
    
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        answer = []
        
        def subQueries(q: int) -> int:
            sum = 0
            for i in range(len(nums)):
                sum += nums[i]
                if q < sum :
                    return i
            return len(nums)
            
        for elements in queries:
            answer.append(subQueries(elements))

        return answer