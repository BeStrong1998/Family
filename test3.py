class Point:
    def __init__(self, a=0, b=None):
        self.a = a
        self.__b = b

    def set_value_a(self, a):
        if self.a == a:
            print('Значение атрибута -a- не изменилось!')
        else:
            print('Значение атрибута -a- изменилось на новое!')

    def set_value_b(self, b):
        if self.__b == b:
            print('Значение атрибута -b- не изменилось!')
        else:
            raise ValueError('Значение атрибута -b- нельзя изменить!')
  
    def get_value_b(self):
        return self.__b

    def get_value_a(self):
        return self.a  

pt = Point()
pt.set_value_b(None)
pt.set_value_a(1)
print('b =', pt.get_value_b())
print('a =', pt.get_value_a())
