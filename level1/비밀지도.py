def solution(n, arr1, arr2):
    answer = []
    ListA = []
    
    for i in range(n) : 
        binary = list(bin(arr1[i] | arr2[i])[2:].zfill(n))
        
        for j in range(n) :
            if '1' in binary[j] :
                ListA.append('#')
            else : 
                ListA.append(' ')
                
        answer.append("".join(ListA))    
        ListA.clear()
