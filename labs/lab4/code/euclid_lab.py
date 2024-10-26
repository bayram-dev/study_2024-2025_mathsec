
a, b = 12345, 54321
print(a,b)

def euclid(a: int, b: int) -> int:
    """Классический алгоритм Евклида"""
    while a != 0 and b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
    return a or b

euclid(a, b)

def euclid_bin(a: int, b: int) -> int:
    """Бинарный алгоритм Евклида"""
    g = 1
    while a % 2 == 0 and b % 2 == 0:
        a /= 2
        b /= 2
        g *= 2
    u, v = a, b
    while u != 0:
        if u % 2 == 0:
            u /= 2
        if v%2 == 0:
            v /= 2
        if u>=v:
            u -= v
        else:
            v -= u
    return g*v

euclid_bin(a, b)

def euclid_ext(a: int, b: int) -> tuple[int]:
    """Расширенный алгоритм Евклида"""
    if a == 0:
        return (b, 0, 1)
    else:
        div, x, y = euclid_ext(b % a, a)
    return (div, y - ( b // a ) * x, x)

euclid_ext(a, b)

def euclid_bin_ext(a: int, b: int) -> tuple[int]:
    """Расширенный бинарный алгоритм Евклида"""
    g = 1
    while a % 2 == 0 and b % 2 == 0:
        a /= 2
        b /= 2
        g *= 2
    u, v = a, b
    A, B, C, D = 1, 0, 0, 1
    while u != 0:
        if u % 2 == 0:
            u /= 2
            if A % 2 == 0 and B % 2 == 0:
                A /= 2
                B /= 2
            else:
                A = (A + b)/2
                B = (B - a)/2
        if v % 2 == 0:
            v /= 2
            if C % 2 == 0 and D % 2 == 0:
                C /= 2
                D /= 2
            else:
                C = (C + b)/2
                D = (D - a)/2
        if u>=v:
            u -= v
            A -= C
            B -= D
        else:
            v -= u
            C -= A
            D -= B
    return (g * v, C, D)

euclid_bin_ext(a, b)

