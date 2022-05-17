from modular import Modular
from math import sqrt, floor


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
    p = 257
    m = Modular(p)
    for i in range(p):
        if m.is_primitive_root(i):
            print(i)


if __name__ == '__main__':
    mods()
