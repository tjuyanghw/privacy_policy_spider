#!/usr/bin/env python

import math

def is_prime(n):
    if n==2: return True
    k = int(math.sqrt(n)) + 1
    while k >= 2:
        if n % k == 0:
            return False
        k -= 1
    return True


def next_prime():
    yield 2
    k = 3
    while True:
        if is_prime(k):
            yield k
        k += 2

def next_prime2():
    yield 2
    memo = set([2])
    k = 3
    while True:
        for p in memo:
            if k % p == 0:
                k += 2
                continue
        memo.add(k)
        k += 2

def main():
    for i,pi in enumerate(next_prime2()):
        print(i,pi)
        if i > 100:
            break

if __name__ == '__main__':
    main()
