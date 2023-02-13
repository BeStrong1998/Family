#Генератор списка
"""a = [x ** 2 for x in range(6)]
print(a)"""


# Пример генератора - можно получить один объект за раз 
"""a = (x ** 2 for x in range(6))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(list(a))
print(list(a))"""


# Пример итерируемого объекта
"""s = [1,2,3]
d = iter(s)
print(next(d))
"""



"""
def test():
    for i in range(10):
        yield i

t = test()
r = iter(t)
print(next(t))
print(next(t))
print(next(t))
print(next(t))

print(t)
print(r)

for x in test():
    print(x)


a = iter("1,2,3,4")
print(a)
print(next(a))
"""



def generate_ints(N):
   for i in range(N):
       yield i


gen = generate_ints(3)
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))