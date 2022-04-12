class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sum_arr = []
        
        for i in range(len(mat)):
            sum_arr.append((i, sum(mat[i])))
        
        sorted_arr = sorted(sum_arr, key = lambda x:x[1])
        
        answer = [i[0] for i in sorted_arr[:k]]
        
        return answer