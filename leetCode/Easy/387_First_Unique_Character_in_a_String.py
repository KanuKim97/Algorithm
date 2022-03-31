class Solution:
    def firstUniqChar(self, s: str) -> int:
        answer = -1 
        pointer = 0
        lst = list(s)
        cnt_dict = Counter(lst)
        
        for word in lst :
            if cnt_dict[word] == 1 :
                answer = pointer
                break 
            pointer += 1
        
        return answer