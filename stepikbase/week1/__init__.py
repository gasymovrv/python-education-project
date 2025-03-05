import sys

print("======== Возведение в степень ** =========")
print(9 ** 2 - int(float(9 ** 2)))  # 0
print(9 ** 19 - int(float(9 ** 19)))  # 89 - Большие float теряют точность
print(9 ** 50)
print(2 ** 3)
print(int(9. ** 19))
print(type(1350851717672992089.))
print(1350851717672992189568.)
print("======== Целочисленное деление // =========")
print(205 // 200)
print("======== Дробное деление // =========")
print(205 / 200)

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

print("======== Операции с boolean =========")
print(True - True)  # 0
print(True - False)  # 1
print(False - False)  # 0
print(False - True)  # -1
print(True + True)  # 2
print((True + True) * 2)  # 4
print(True * True)  # 1

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
