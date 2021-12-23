def solution(lottos, win_nums):
    answer = []
    ranking = [6, 6, 5, 4, 3, 2, 1]
    collection = 0

    for i in range(len(lottos)) : 
        if lottos[i] in win_nums :
            collection += 1
    
    answer.append(ranking[collection + lottos.count(0)])
    answer.append(ranking[collection])
    
    return answer