from functools import partial
from collections import defaultdict
from itertools import product, groupby
from operator import itemgetter

# utility methods
last = itemgetter(-1)
first = itemgetter(0)
pow2 = partial(pow, 2)

def pow2r(n):
    return range(pow2(n))

def gather(iterable, keyfunc):
    return groupby(sorted(iterable, key=keyfunc), keyfunc)

# real code
def generate(c1,c2,bitlen):
    a = c1 & ~pow2(bitlen)
    b = c2 & ~pow2(bitlen)
    c = c1 >> 1
    d = c2 >> 1
    return (a&~b&~c&~d) | (~a&b&~c&~d) | (~a&~b&c&~d) | (~a&~b&~c&d)

def build_map(n, nums):
    r = pow2r(n + 1)
    filtered = [e for e in [(i, j, generate(i,j,n)) for i,j in product(r,r)] if e[2] in nums]
    def reducer(m, e):
        m[(e[2], e[0])].add(e[1])
        return m
    return reduce(reducer, filtered, defaultdict(set))

def solution(graph):
    t = list(zip(*graph))
    ncols = len(t[0])
    nums = [sum([pow2(i) if col else 0 for i, col in enumerate(row)]) for row in t]
    nmap = build_map(ncols, set(nums))
    def reducer(pre, row):
        next_row = [(c2,pre[c1]) for c1 in pre for c2 in nmap[(row, c1)]]
        return {k: sum(map(last, v)) for k, v in gather(next_row, first)}
    return sum(reduce(reducer, nums, {i: 1 for i in pow2r(ncols + 1)}).values())
    
print solution([[True, False, True], [False, True, False], [True, False, True]])
print solution(
        [[True, True, False, True, False, True, False, True, True, False],
        [True, True, False, False, False, False, True, True, True, False],
        [True, True, False, False, False, False, False, False, False, True],
        [False, True, False, False, False, False, True, True, False, False]])
