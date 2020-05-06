
def solution(x, y):
    if len(x) > len(y):
        return (set(x) - set(y)).pop()
    else:
        return (set(y) - set(x)).pop()
