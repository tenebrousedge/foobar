# level 3 task 1
def xor_rot(a, b):
    if not a % 2:
        rot = [b, 1, b + 1, 0]
    else:
        rot = [a, a ^ b, a - 1, (a - 1) ^ b]
    return rot[(b - a) % 4]

def solution(start, length):
    return reduce(lambda m, i: m ^ xor_rot(start + length * i, start + length * i + (length - i) - 1), range(0, length), 0)

assert solution(0, 3) == 2
assert solution(17, 4) == 14
