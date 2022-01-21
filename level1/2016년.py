def solution(a, b):
    list_DATE = ['FRI', 'SAT', 'SUN', 'MON','TUE','WED','THU']
    list_DAY = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sum_Day = 0
    
    for i in range(a-1):
        sum_Day += list_DAY[i]
    sum_Day += b
    
    return list_DATE[(sum_Day-1) % 7]