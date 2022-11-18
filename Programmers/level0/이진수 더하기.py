def solution(bin1, bin2):
    decimal_1, decimal_2 = 0, 0
    l_bin1 = list(bin1)
    l_bin2 = list(bin2)
    
    for i in range(len(l_bin1)):
        decimal_1 += int(l_bin1.pop()) * 2 ** i
    
    for i in range(len(l_bin2)):
        decimal_2 += int(l_bin2.pop()) * 2 ** i
        
    return format(decimal_1 + decimal_2, 'b')