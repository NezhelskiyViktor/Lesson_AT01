# Введение в автоматическое тестирование и написание модульных тестов с unittest

## Задание
Написать функцию для вычисления остатка от деления и тесты 
для проверки её работы, включая обработку деления на ноль.

## Описание

Этот проект представляет собой набор простых математических 
функций, реализованных в файле `main.py`, а также тестов для 
этих функций, написанных с использованием библиотеки `unittest`
в файле `test.py`. Основные функции включают арифметические 
операции, проверку четности и вычисление остатка от деления.

## Функции

В файле `main.py` реализованы следующие функции:

1. **add(a, b)**: Возвращает сумму двух чисел.
2. **subtract(a, b)**: Возвращает разность двух чисел.
3. **multiply(a, b)**: Возвращает произведение двух чисел.
4. **divide(a, b)**: Делит `a` на `b`. Если `b` равно 0, 
вызывается ошибка `ValueError` с сообщением "На ноль делить нельзя".
5. **check(number)**: Проверяет, является ли число четным.
6. **remainder(a, b)**: Возвращает остаток от деления 
`a` на `b`. Если `b` равно 0, вызывается ошибка `ValueError` 
с сообщением "На ноль делить нельзя".
