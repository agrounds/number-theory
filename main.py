from modular import Modular
from math import sqrt, floor, gcd


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def fermat_primes():
    for n in range(10):
        x = 2**n + 1
        print(f'{x} is prime: {is_prime(x)}')


def mods():
    p = 11
    m = Modular(p)
    for i in range(p):
        if m.is_primitive_root(i):
            print(i)


def pows(primitives_only=False):
    p = 29
    m = Modular(p)
    a = 2
    for i in range(p):
        if not primitives_only or gcd(i, p-1) == 1:
            print(f'{a}^{i} = {m.pow(a, i)}')


if __name__ == '__main__':
    m = Modular(29)
    for x in [16, 24, 7, 25, 23, 20, 1]:
        print(f'{x}^7 = {m.pow(x, 7)}')
