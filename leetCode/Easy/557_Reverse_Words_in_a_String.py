'''
Solution 1
RunTime : 38ms, faster than 83.89%
Memory Usage : 14.7MB less than 62.99%

'''
class Solution:
    def reverseWords(self, s: str) -> str:
        answer = []
        s_Split = s.split()
        
        for i in range(len(s_Split)):
            Reversed_List = list(reversed(s_Split[i]))
            answer.append(''.join(Reversed_List))
        
        return ' '.join(answer)