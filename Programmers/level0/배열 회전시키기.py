def solution(numbers, direction):
    if direction == "right":
        return numbers[len(numbers)-1:] + numbers[:len(numbers)-1]
    else :
        return numbers[-(len(numbers)-1):] + numbers[:-(len(numbers)-1)]