def solution(numbers):
    return numbers.pop(numbers.index(max(numbers))) * numbers.pop(numbers.index(max(numbers)))