def solution(sizes):
    length, width = [], []
    
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1] : 
            length.append(sizes[i][1])
            width.append(sizes[i][0])
        else : 
            length.append(sizes[i][0])
            width.append(sizes[i][1])

    return max(length) * max(width)