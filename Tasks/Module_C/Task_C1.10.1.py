class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Triangle ({self.a}, {self.b}, {self.c})'

T = Triangle(5, 10, 15)
print(T)