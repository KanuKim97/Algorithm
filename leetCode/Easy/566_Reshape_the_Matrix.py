class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if mat == [] or r * c != len(mat) * len(mat[0]) :
            return mat 
        
        answer = [[0 for j in range(c)] for i in range(r)]
        k = 0
        
        for row in mat:
            for col in row:
                answer[k // c][k % c] = col
                k += 1

        return answer