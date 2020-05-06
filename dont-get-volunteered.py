from collections import deque

MOVES = (
  (-1, 2),
  (-2, 1),
  (-2, -1),
  (-1, -2),
  (1, -2),
  (2, -1),
  (2, 1),
  (1, 2)
)
def is_legal(x, y):
    return 0 <= x <= 7 and 0 <= y <= 7

def distance(x1, y1, x2, y2):
    dist = [[-1 for _ in range(8)] for _ in range(8)]
    dist[x1][y1] = 0
    q = deque([(x1, y1)])
    while len(q):
        i, j = q.popleft()
        if i == x2 and j == y2:
            return dist[i][j]
        for delta_i, delta_j in MOVES:
            new_i = i + delta_i
            new_j = j + delta_j
            if is_legal(new_i, new_j) and dist[new_i][new_j] == -1:
                dist[new_i][new_j] = dist[i][j] + 1
                q.append((new_i, new_j))

def solution(start, fin):
    x1, y1 = divmod(start, 8)
    x2, y2 = divmod(fin, 8)
    return distance(x1, y1, x2, y2)


assert(solution(0, 1) == 3)
assert(solution(19, 36) == 1)
assert(solution(0, 9) == 4)
assert(solution(9, 43) == 2)
assert(solution(0, 63) == 6)
assert(solution(0, 62) == 5)
