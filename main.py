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


def pows_ai(a, p, primitives_only=False):
    m = Modular(p)
    for i in range(p):
        if not primitives_only or gcd(i, p-1) == 1:
            print(f'{a}^{i} = {m.pow(a, i)}')


def pows_ik(k, p):
    m = Modular(p)
    for i in range(p):
        print(f'{i}^{k} = {m.pow(i, k)}')


def gauss_lemma(a, p):
    """
    :param p: Odd prime
    """
    for i in range(1, (p+1)//2):
        b = (i * a) % p
        if b > (p-1)/2:
            b -= p
        print(f'{i} * {a} = {b}')


if __name__ == '__main__':
    pows_ik(2, 13)
