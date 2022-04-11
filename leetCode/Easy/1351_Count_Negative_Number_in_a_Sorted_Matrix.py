class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        answer = 0
        
        for i in range(len(grid)):
            if grid[i][-1] < 0 :
                for j in range(len(grid[0])):
                    if grid[i][j] < 0 :
                        answer += 1
        
        return answer