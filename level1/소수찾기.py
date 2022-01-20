def solution(number):
    numbers = [True] * (number + 1)
    answer = 0

    for num in range(2,int(math.sqrt(number))+1):
        if numbers[num] == False:
            continue;

        for i in range(num+num,number+1,num):
            numbers[i] = False

    for i in range(2,number+1):
        if numbers[i] == True:
            answer+=1

    return answer