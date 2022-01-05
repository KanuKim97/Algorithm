def solution(s):
    L = list(s)
    L.sort(reverse=1)
    S = "".join(L)
    return S