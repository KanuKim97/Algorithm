def solution(brown, yellow):
    total = brown+yellow
    rows = [(total) // c for c in range(3,(total)//3 + 1) if (total) % c == 0]
    for row in rows:
        col = (total) // row
        if 2*(row+col-2) == brown:
            return [row, col]