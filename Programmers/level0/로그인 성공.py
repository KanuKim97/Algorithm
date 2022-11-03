def solution(id_pw, db):
    row = -1
    
    for i in range(len(db)):
        if id_pw[0] == db[i][0]:
            row = i
    
    if row == -1 :
        return 'fail'
    
    if id_pw[1] == db[row][1] : 
        return 'login'
    else :
        return 'wrong pw'