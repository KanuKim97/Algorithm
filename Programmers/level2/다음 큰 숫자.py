def solution(n):
    list_bin = list(format(n, 'b'))
    
    for i in range(1000000 - n):
        n += 1
        list_no = list(format(n, 'b'))
        if list_no.count('1') != list_bin.count('1') :
            list_no.clear()
        else :
            s =  '0b'+ ''.join(list_no)
            return int(s,2)
            break