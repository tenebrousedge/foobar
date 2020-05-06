from collections import deque

class Node:
    def __init__(self, x, y, distance, wallflag):
        self.x = x
        self.y = y
        self.distance = distance
        self.wallflag = wallflag

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(tuple(self))

    def __iter__(self):
        return iter([self.x, self.y])

    def isValid(self):
        True # assign this later

    def neighbors(self):
        points = [(self.x + xd, self.y + yd) for xd, yd in ((-1, 0), (1, 0), (0, -1), (0, 1))]
        return filter(Node.isValid, [Node(x, y, self.distance + 1, self.wallflag) for x, y in points])

def solution(maze):
    distances = [[-1 for _ in maze[0]] for _ in maze]
    distances[0][0] = 0
    max_x = len(maze[0]) - 1
    max_y = len(maze) - 1
    def _isValid(self):
        return 0 <= self.x <= max_x and 0 <= self.y <= max_y
    Node.isValid = _isValid
    queue = deque([Node(0, 0, 0, True)])
    while len(queue):
        node = queue.popleft()
        if node.x == max_x and node.y == max_y:
            return node.distance + 1
        for neighbor in node.neighbors():
            if distances[neighbor.y][neighbor.x] != -1:
                continue
            # if neighbor is not a wall, add
            elif maze[neighbor.y][neighbor.x] == 0:
                distances[neighbor.y][neighbor.x] = neighbor.distance
                queue.append(neighbor)
            # if neighbor is a wall and wallflag is not set, add
            elif neighbor.wallflag:
                distances[neighbor.y][neighbor.x] = neighbor.distance
                neighbor.wallflag = False
                queue.append(neighbor)


one = [
[0, 1, 1, 0],
[0, 0, 0, 1],
[1, 1, 0, 0],
[1, 1, 1, 0]]

assert solution(one) == 7

two = [
[0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0]]

assert solution(two) == 11

assert solution([[0,0,0],[1,1,1],[0,0,0]]) == 5
assert solution([[0]*16]*6 + [[1]*16] + [[0]*16]*9) == 31

four = [
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
[0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
[0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0]]

assert solution(four) == 66, str(solution(four))
