print("in")
print("abc" in "abcba")
print("abce" in "abcba")

print("\nfind")
print("cabcd".find("abc", 1))  # индекс первого вхождения или -1
print("abacaba".rfind("aba"))  # индекс последнего вхождения

print("cabcd"[1:].find("abc"))
# print(str.find.__doc__)

print("\nindex")
print("cabcd".index("abc"))  # индекс первого вхождения или ValueError
# print("cabcd".index("aec")) # ValueError

print("\nstartswith")
s = "The dog in black fled across the desert, and the gunslinger followed"
print(s.startswith(("The woman", "The dog", "The man in black")))
# print(s.startswith.__doc__)

print("\nendswith")
s = "image.png"
print(s.endswith(".png"))

print("\ncount")
s = "abacaba"
print(s.count("aba"))
# print(s.count.__doc__)

print("\nlower/upper")
s = "The man in black fled across the desert, and the gunslinger followed"
print(s.lower())
print(s.upper())
print(s.count("the"))
print(s.lower().count("the"))

print("\nreplace")
s = "1,2,3,4"
print(s)
print(s.replace(",", ", ", 2))  # заменить "," на ", " в строке s не более двух раз
# print(s.replace.__doc__)

print("\nsplit")
s = "1 2 3 4"
print(s.split(" ", 2))  # разбить строку s на части по пробелу не более двух раз

s = "1\t\t 2  3       4       "
print(s.split())
# print(s.split.__doc__)

print("\nstrip")
s = "       1, 2, 3, 4      \t"
print(repr(s.rstrip()))
print(repr(s.lstrip()))
print(repr(s.strip()))

s = "_*__1, 2, 3, 4__*_"
print(repr(s.rstrip("*!_")))  # удаляет перечисленные символы
print(repr(s.lstrip("*!_")))
print(repr(s.strip("*!_")))

numbers = map(str, [1, 2, 3, 4, 5])
print("\njoin")
# Возвращает строку, соединяя элементы списка через пробел. Элементы списка должны быть строками
print(repr(" ".join(numbers)))


print("\nformat")
capital = "London is the capital of Great Britain"
template = "{} is the capital of {}"
print(template.format("London", "Great Britain"))
print(template.format("Vaduz", "Liechtenstein"))
template = "{1} is the capital of {0}"
print(template.format("Vaduz", "Liechtenstein"))
# print(template.format.__doc__)

template = "{capital} is the capital of {country}"
print(template.format(capital="London", country="Great Britain"))
print(template.format(country="Liechtenstein", capital="Vaduz"))

import requests

print("\nformat with nested attributes")
template = "Response from {0.url} with code {0.status_code}"  # Обращение к атрибутам объекта
res = requests.get("https://docs.python.org/3.5/")
print(template.format(res))
res = requests.get("https://docs.python.org/3.5/random")
print(template.format(res))

from random import random

print("\nformat for rounding numbers")
x = random()
print(x)
print("{:.3}".format(x))  # Округление до трех знаков после запятой (только значимые цифры)

x = 0.000467653
print(x)
print("{:.3}".format(x))
