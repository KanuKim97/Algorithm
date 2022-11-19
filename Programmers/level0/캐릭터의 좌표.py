def solution(keyinput, board):
    row_max = (board[0]-1)//2 
    col_max = (board[1]-1)//2
    start = [0,0]
    
    for i in range(len(keyinput)):
        if keyinput[i] == "left" and start[0]-1 >= -(row_max):
            start[0] -= 1
        if keyinput[i] == "right" and start[0]+1 <= row_max:
            start[0] += 1
        if keyinput[i] == "up" and start[1]+1 <= col_max:
            start[1] += 1
        if keyinput[i] == "down" and start[1]-1 >= -(col_max):
            start[1] -= 1
        
    return start