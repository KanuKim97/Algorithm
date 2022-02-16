def solution(s):
    Sheet = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i in Sheet :
        s = s.replace(i, str(Sheet.index(i)))
        
    return int(s)