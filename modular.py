class Modular:
    def __init__(self, p):
        self.p = p

    def ord(self, x):
        p = self.p
        x %= p
        if x == 0:
            return 0
        y = x
        for i in range(1, (p-1) // 2 + 1):
            if y == 1:
                return i
            y *= x
            y %= p
        return p - 1

    def is_primitive_root(self, x):
        return self.ord(x) == self.p - 1

    def pow(self, x, n):
        p = self.p
        x %= p
        n %= p - 1
        y = 1
        for _ in range(n):
            y *= x
            y %= p
        return y
