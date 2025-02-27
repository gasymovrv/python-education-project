import sys

print(9 ** 19 - int(float(9 ** 19)))
print(9 ** 50)
print(2 ** 3)
print(int(9. ** 19))
print(type(1350851717672992089.))
print(1350851717672992189568.)

a1 = 1
a1 = "235"
a1 = True

print(type(a1))

print("1 is = ", bool(1))
print("not 1 is = ", bool(not 1))
print("2.75 is = ", bool(2.75))
print("0 is = ", bool(0))
print("0.0 is = ", bool(0.0))
print("empty str is = ", bool(""))
print("str is = ", bool("str"))

a2 = 50
print("Classic comparisons: ", 10 <= a2 and a2 < 100)
print("Chain of comparisons: ", 10 <= a2 < 100)

print("sys.getsizeof(42) =", sys.getsizeof(42))  # Integer
print("sys.getsizeof(3.14) =", sys.getsizeof(3.14))  # Float
print("sys.getsizeof(True) =", sys.getsizeof(True))  # Boolean
print("sys.getsizeof('Hello') =", sys.getsizeof("Hello"))  # String
print(sys.getsizeof([]))  # Empty list
print(sys.getsizeof(()))  # Empty tuple
print(sys.getsizeof({}))  # Empty dict
print(sys.getsizeof(set()))  # Empty set


for i in range(5):
    y = i

print(y)
