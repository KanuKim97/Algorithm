import heapq

def solution(scoville, K):
    answer = 0
    heap = []

    for i in range(len(scoville)):
        heapq.heappush(heap, scoville[i])

    while(heap[0] <= K):
        if len(heap) < 2:
            return -1

        Element1 = heapq.heappop(heap)
        Element2 = heapq.heappop(heap)
        heapq.heappush(heap, Element1 + (Element2*2))
        answer += 1

    return answer