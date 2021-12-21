def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        myList = array[commands[i][0]-1 : commands [i][1]]
        myList.sort()
        answer.append(myList[commands[i][2]-1])
          
    return answer