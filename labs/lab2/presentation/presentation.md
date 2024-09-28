---
## Front matter
lang: ru-RU
title: Шифры перестановки
author:
  - Тагиев Б. А.
institute:
  - Российский университет дружбы народов, Москва, Россия
date: 28 сентябр 2024

## i18n babel
babel-lang: russian
babel-otherlangs: english

## Formatting pdf
toc: false
toc-title: Содержание
slide_level: 2
aspectratio: 169
section-titles: true
theme: metropolis
mainfont: DejaVu Serif
romanfont: DejaVu Serif
sansfont: DejaVu Sans
monofont: DejaVu Sans Mono
header-includes:
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
---

## Цель работы

Целью данной работы является изучение алгоритмов шифрования перестановки,
принцип его работы, реализация на Julia.


## Маршрутное шифрование

Реализация:

```julia
message = filter(!isspace, message)
matrix = fill('_', rows, cols)
index = 1
new_message = ""
for i = 1:rows
        for j = 1:cols
                if index != rows * cols
                        matrix[i, j] = message[index]
                        index += 1
                end
        end
end
for j in sort(collect(key))
        for i = 1:rows
                new_message *= (matrix[i, (findfirst(j, key))])
        end
end
return new_message
```

## Маршрутное шифрование

Выполнение:

```
$ julia route.jl 
hamgses!iss_iteetsta
```

## Шифрование с помощью решеток

Выполнение:

```
$ julia ./rails.jl 
,lr!HNdwoeolle W
```

## Таблица Вижинера

Реализация:

```julia
alphabet = 'a':'z'
output = ""
key_index = 1

for i in text
        if isletter(i)
                offset = findfirst(isequal(key[key_index]), alphabet) - 1
                index = findfirst(isequal(i), alphabet) + offset
                index > 26 && (index -= 26)
                output *= alphabet[index]
                key_index += 1
                key_index > length(key) && (key_index = 1)
        else
                output *= i
        end
end

return output
```

## Таблица Вижинера

Выполнение:

```
$ julia vigener.jl 
rijvs uyvjn
```

## Выводы

В данной лабораторной работе были изучены три шифра перестановки, все алгоритмы были реализованы на языке Julia и работают корректно.
