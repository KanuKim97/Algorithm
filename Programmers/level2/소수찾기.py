from itertools import permutations
import math

def solution(numbers):
    answer = []
    per_List = []
    num_List = list(numbers)
    
    for i in range(1, len(num_List)+1):
        per_List += list(map(''.join, permutations(num_List, i)))
    
    new_List = [int(('').join(p)) for p in per_List]
    
    for nums in new_List :
        if nums < 2 :
            continue

        check_nums = True
        for i in range(2, int(math.sqrt(nums))+1):
            if nums % i == 0:
                check_nums = False
                break
        
        if check_nums :
            answer.append(nums)
            
    return len(set(answer))

'''
permutation : 순열
'''
