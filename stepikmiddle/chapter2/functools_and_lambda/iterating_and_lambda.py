x = input("Provide 2 numbers:\n").split()
print(x)  # ['1', '2']

# first argument of map is function (constructor of type int is also function int.__init__(str) -> int),
# second argument is iterable.
# n, k - unpacking of iterable object. if iterable is more or less than 2 elements, it throws error
n, k = map(int, x)
print(n + k)

# the same as `n, k = map(int, x)` but using generator instead
n, k = (int(i) for i in x)
print(n + k)

xs = (int(i) for i in input("Provide numbers for filter by even:\n").split())
iterator = filter(lambda num: num % 2 == 0, xs)
print(list(iterator))  # converts iterator (that was returned by filter) to list

x = [
    ("Guido", "van", "Rossum"),
    ("Haskell", "Curry"),
    ("John", "Backus")
]
x.sort(key=lambda tuple_: len(" ".join(tuple_)))
print(x)
