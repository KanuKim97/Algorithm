class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran_cnt = dict(Counter(list(ransomNote)))
        mag_cnt = dict(Counter(list(magazine)))
        
        ran_key = ran_cnt.keys()
        mag_key = mag_cnt.keys()
        
        for keys in ran_key :
            if keys not in mag_key :
                return False 
                break
                
            if mag_cnt[keys] - ran_cnt[keys] < 0 :
                return False
                break
                
        return True