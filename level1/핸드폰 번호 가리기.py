import re

def solution(phone_number):
    last = phone_number[-4:]
    front = phone_number[:-4]
    blind = re.sub('[0-9]', '*', front)
    
    return blind + last