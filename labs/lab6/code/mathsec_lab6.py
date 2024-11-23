# -*- coding: utf-8 -*-
"""mathsec_lab6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RhtlVaBr3WdtzNiH5kK2CdkLwlEXRwyZ
"""

from math import gcd

def f(x, n):
    return (x*x+5)%n

def fu(n, a, b, d):
    a = f(a, n)
    b = f(f(b, n), n)
    d = gcd(a-b, n)
    if 1 < d < n:
        print(a, b, d, sep="\t")
        print()
        print("result: ", d)
        exit()
    if d == n:
        print("doesn't exist")
    if d == 1:
        print(a, b, d, sep="\t")
        fu(n, a, b, d)

if __name__ == "__main__":
    n = 1359331
    c = 1
    a = f(c, n)
    b = f(a, n)
    d = gcd(a-b, n)
    if 1 < d < n:
        print(d)
        exit()
    if d == n:
        pass
    if d == 1:
        print(a, b, d, sep="\t")
        fu(n, a, b, d)

