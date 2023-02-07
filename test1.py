class CLS:
    def __init__(self, x):
        self.x = x
    def __str__(self):
        return f"{self.x}"
    def __add__(self, other):
        x = str(self.x) + str(other.x)
        return CLS(x)

a = CLS("1")
b = CLS(1)

print(a + b)
