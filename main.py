#1 тема переменные в Python
a = input()
b = int(input())
c = float(input())
d = bool(input()) #True или False

#2 тема списки и кортежи в Python
s1 = [1, 'papa', 3.40]
s2 = (1,)

#3 тема циклы в Python
for i in range(1, 10 + 1):
    print('tecnikum')

while b != 0:
    print(b)
    b = b - 1

#4 тема list comprehesion
s3 = [i for i in range(1, 10 + 1) if i % 2 == 0]
print(s3)

#5 тема работа со словарями
d = {'name': None}
d['name'] = a
print(d)

#6 тема Лямда функции
from math import pow
z = lambda t: pow(t, 3)
print(z(5))

#7 тема функции
def do_smth(g):
    return g

print(do_smth('привет'))

#8 тема классы и объекты
class Human:
    def __init__(self, name):
        self.name = name
    def did_smth(self):
        print('NOT EZ')

humanity = Human(name = input())

#9 тема наследования
class Personality(Human):
    def did_smth(self):
        print('EZ')

personal.did_smth()



