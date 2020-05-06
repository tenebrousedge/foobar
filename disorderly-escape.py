from math import factorial as f
from collections import Counter
from fractions import gcd
from itertools import starmap, product

def cycle_count(cycle, n):
    return reduce(lambda cc, e: cc // (e[0]**e[1] * f(e[1])), Counter(cycle).items(), f(n))

def partitions(n, i = 1):
    yield [n]
    for i in range(i, n//2 + 1):
        for j in partitions(n - i, i):
            yield [i] + j


def solution(width, height, numStates):
    def burnside(cpw, cph):
        m = cycle_count(cpw, width) * cycle_count(cph, height)
        return m * numStates**sum(starmap(gcd, product(cpw, cph)))

    grid = sum(starmap(burnside, product(*map(partitions, [width, height]))))
    return str(grid // (f(width) * f(height)))
    
print solution(2,3,4)
print solution(2,2,2)
print solution(12,12,20)
