# Пример использования магических методов __getattr__ и __setattr__

class Point:
    def __init__(self, a=1, b=1):
        self.a = a
        self.b = b

    def __getattr__(self, name: str):
        return self.__dict__[f"_{name}"]

    def __setattr__(self, name, value):
        if name == '_a':
            raise AttributeError('Значение атрибута a поменять нельзя')
        if name == '_b':
            print('Значение атрибута изменилось на новое')
        self.__dict__[f"_{name}"] = value

point = Point()
#point._a = 1
point._b = 1
print(point.a, ':', point.__b)
print(point.__dict__)



# Пример использования @property
"""class Employee:
    def __init__(self, a, b):
        self._a = a
        self._b = b
        
    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if self._a != value:
            print('Значение атрибута a изменилось на новое!')

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if self._b != value:
            raise AttributeError('Значение атрибута b нельзя изменить!')

pt = Employee(1,2)
pt.a = 2
pt.b = 3
print(pt.a, ':', pt.b)"""

