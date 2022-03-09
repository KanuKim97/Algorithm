class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        Index_I ,Index_II = 0, len(numbers)-1
        answer_List = []
        
        while Index_I < Index_II:
            
            if numbers[Index_I] + numbers[Index_II] == target :
                answer_List.append(Index_I + 1)
                answer_List.append(Index_II + 1)
                return answer_List    
            
            elif numbers[Index_I] + numbers[Index_II] < target :
                Index_I += 1
            else :
                Index_II -= 1
