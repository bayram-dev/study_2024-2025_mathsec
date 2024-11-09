---
## Front matter
title: "Вероятностные алгоритмы проверки чисел на простоту"
author: "Тагиев Байрам Алтай оглы"

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: false # List of figures
lot: false # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: IBM Plex Serif
romanfont: IBM Plex Serif
sansfont: IBM Plex Sans
monofont: IBM Plex Mono
mathfont: STIX Two Math
mainfontoptions: Ligatures=Common,Ligatures=TeX,Scale=0.94
romanfontoptions: Ligatures=Common,Ligatures=TeX,Scale=0.94
sansfontoptions: Ligatures=Common,Ligatures=TeX,Scale=MatchLowercase,Scale=0.94
monofontoptions: Scale=MatchLowercase,Scale=0.94,FakeStretch=0.9
mathfontoptions:
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

## Тест Ферма

* Вход. Нечетное целое число $n \geq 5$.
* Выход. «Число n, вероятно, простое» или «Число n составное».

1. Выбрать случайное целое число $a, 2 \leq a \leq n-2$.
2. Вычислить $r=a^{n-1} (mod n)$
3. При $r=1$ результат: «Число n, вероятно, простое». В противном случае результат: «Число n составное».

## Тест Соловэя-Штрассена

* Вход. Нечетное целое число $n \geq 5$.
* Выход. «Число n, вероятно, простое» или «Число n составное».

1. Выбрать случайное целое число $a, 2 \leq a \leq n-2$.
2. Вычислить $r=a^{(\frac{n-1}{2})} (mod n)$
3. При $r \neq 1$ и $r \neq n-1$ результат: «Число n составное».
4. Вычислить символ Якоби $s = (\frac{a}{n})$
5. При $r=s (mod n)$ результат: «Число n, вероятно, простое». В противном случае результат: «Число n составное».

## Тест Миллера-Рабина.

* Вход. Нечетное целое число $n \geq 5$.
* Выход. «Число n, вероятно, простое» или «Число n составное».

1. Представить $n-1$ в виде $n-1 = 2^sr$, где r - нечетное число
2. Выбрать случайное целое число $a, 2 \leq a \leq n-2$.
3. Вычислить $y=a^r (mod n)$
4. При $y \neq 1$ и $y \neq n-1$ выполнить действия
	- Положить $j=1$
	- Если $j \leq s-1$ и $y \neq n-1$ то
		* Положить $y=y^2 (mod n)$
		* При $y=1$   результат: «Число n составное».
		* Положить $j=j+1$
	- При $y \neq n-1$ результат: «Число n составное».
5. Результат: «Число n, вероятно, простое».

# Выполнение работы

## Реализация алгоритмов на языке Python

```python
import random

def Ferma(n, count):
    for i in range(count):
        a = random.randint(2, n-1)
        if ( a**(n-1)%n != 1 ):
            print("Complex")
            return False
    print("Simple")
    return True
```

```python
def modulo(base, exponent, mod):
    x = 1
    y = base
    while (exponent > 0):
        if (exponent%2 == 1):
            x = (x*y)%mod
        y = (y*y)%mod
        exponent = exponent//2
    return x%mod

def calculateJacobian(a, n):
    if (a == 0):
        return 0
    ans = 1
    if (a < 0):
        a = -a
        if (n%4 == 3):
            ans = -ans
    if ( a == 1):
        return ans
    while (a):
        if (a < 0):
            a = -a
            if (n%4 == 3):
                ans = -ans
        while (a%2 == 0):
            a = a//2
            if (n%8 == 3 or n%8 == 5):
                ans = -ans
        a, n = n, a
        if (a%4 == 3 and n%4 == 3):
            ans = -ans
        a = a%n
        if (a > n//2):
            a = a - n
    if (n == 1):
        return ans
    return 0

def SoloveiStrassen(p, iterations):
    if (p < 2):
        print("Complex")
        return False
    if (p!=2 and p%2==0):
        print("Complex")
        return False
    for i in range(iterations):
        a = random.randrange(p-1) + 1
    jacobian = (p + calculateJacobian(a, p))%p
    mod = modulo(a, (p-1)/2, p)
    if (jacobian == 0 or mod != jacobian):
        print("Complex")
        return False
    return True
```

```python
def MillerRabin(n):
    if n != int(n):
        print("Complex")
        return False
    n = int(n)
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        print("Complex")
        return False
    if n==2 or n==3 or n==5 or n==7:
        print("Simple")
        return True
    s = 0
    d = n-1
    while d%2 == 0:
        d >>= 1
        s += 1
    assert(2**s*d == n-1)
    
    def trial_compose(a):
        if pow(a, d, n) == 1:
            print("Complex")
            return False
        for i in range(s):
            if pow(a, 2**i*d, n) == n-1:
                print("Complex")
                return False
        print("Simple")
        return True
    
    for i in range(8):
        a = random.randrange(2, n)
        if trial_compose(a):
            print("Complex")
            return False
    print("Simple")
    return True
```

## Результаты выполнения

```python
n = 101
print(Ferma(n, 25))
print("==========")
print(Ferma(n+1, 25))
```

```
Simple
True
==========
Complex
False
```

```python
print(SoloveiStrassen(n, 25))
print("==========")
print(SoloveiStrassen(n+1, 25))
```

```
True
==========
Complex
False
```

```python
print(MillerRabin(n))
print("==========")
print(MillerRabin(n+1))
```

```
Complex
Complex
Complex
Complex
Complex
Complex
Complex
Complex
Simple
True
==========
Simple
Complex
False
```

# Выводы

Изучили алгоритмы Ферма, Соловэя-Штрассена, Миллера-Рабина.
