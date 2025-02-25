print("start of lib.py")


def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)


def f3_func():
    print('Excluded from * imports because it is not in __all__')


# Exclude this execution from imports
if __name__ == "__main__":
    print(fib(35))

# Explicitly defined for * imports
__all__ = ["fib"]

print("end of lib.py")
