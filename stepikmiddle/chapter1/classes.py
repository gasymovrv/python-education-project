class MyClass:
    tags = []  # атрибут класса
    a = 10  # атрибут класса

    def func(self):  # self - ссылка на экземпляр класса
        print('Hello')

    def change_a(self, a):
        # self.a добавит новую переменную в экземпляр self, переменная 'а' класса не изменится
        self.a = a

    def wrong_change_tags(self, a):
        # self.tags будет сначала искать в экземпляре, потом в классе.
        # т.к. в экземпляре нет переменной 'tags', то в итоге мы меняем состояние переменной 'tags' в классе
        self.tags.append(a)


x = MyClass()
print(type(x))
print(type(MyClass))
print(type(MyClass.func))
MyClass.func(x)
x.func()
print(MyClass.a)
print(x.a)
x.b = 222
print(x.b)

x2 = MyClass()
x.change_a(99)
print('MyClass.a =', MyClass.a)  # 10
print('x.a =', x.a)  # 99
print('x2.a =', x2.a)  # 10

x.wrong_change_tags(100)
print('x.tags =', x.tags)  # 100
print('x2.tags =', x2.tags)  # 100


class Counter:
    def __init__(self):
        self.count = 0

    def inc(self):
        self.count += 1

    def reset(self):
        self.count = 0


counter = Counter()
counter.inc()
print(type(counter.inc))  # <class 'method'>
print(counter.count)
Counter.inc(counter)
print(counter.count)
counter.reset()
print(counter.count)
