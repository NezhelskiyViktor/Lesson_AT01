#  AT01. Введение в автоматическое тестирование
#  и написание модульных тестов с unittest

error = 'На ноль делить нельзя'

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError(error)
    return a / b


def check(number):
    return number % 2 == 0


def remainder(a, b):
    if b == 0:
        raise ValueError(error)
    return a % b
