from math import log, sqrt

def stingy(n):
    phi = (1+sqrt(5))/2
    tau = (1-sqrt(5))/2
    epsilon = pow(10, -10)

    max_h = int(round(log((n + 1) * sqrt(5) + epsilon, phi))) - 2
    fib_num = int(round((pow(phi, max_h + 2) - pow(tau, max_h + 2))/sqrt(5)))
    if n + 1 < fib_num:
        max_h -= 1
    return max_h

def generous(n):
    return int(log(n + 1, 2))

def solution(n):
    max_s = generous(n)
    min_s = stingy(n)
    return min_s - max_s
