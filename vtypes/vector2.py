import math

class Vector2():
    def __str__(self): return f"<{self.x},{self.y}>"
    def __init__(self, x, y): self.x = x; self.y = y
    def __add__(self, op): return Vector2(self.x + op.x, self.y + op.y)
    def __sub__(self, op): return Vector2(self.x - op.x, self.y - op.y)

    def __mul__(self, op):
        if isinstance(op, float) or isinstance(op, int):
            return Vector2(self.x * op, self.y * op)
        else:
            return Vector2(self.x * op.x, self.y * op.y)

    def __truediv__(self, op):
        if isinstance(op, float) or isinstance(op, int):
            return Vector2(self.x / op, self.y / op)
        else:
            return Vector2(self.x / op.x, self.y / op.y)
    
    def __floordiv__(self, op):
        if isinstance(op, float) or isinstance(op, int):
            return Vector2(self.x // op, self.y // op)
        else:
            return Vector2(self.x // op.x, self.y // op.y)

    def __abs__(self):
        return Vector2(abs(self.x), abs(self.y))

    def __neg__(self):
        return self.__mul__(-1)

    def __pow__(self, op):
        return Vector2(pow(self.x, op), pow(self.x, op))

    def floor(self):
        return Vector2(math.floor(self.x), math.floor(self.y))

    def magnitude(self):
        return math.sqrt( pow(self.x, 2) + pow(self.y, 2) )
    
    def sqrt(self):
        return Vector2(math.sqrt(max(0,self.x)), math.sqrt(max(0,self.y)))

    def normalize(self):
        return self / self.magnitude()

    def min(self, op):
        if isinstance(op, float) or isinstance(op, int):
            return Vector2(min(self.x, op), min(self.y, op))
        else:
            return Vector2(min(self.x, op.x), min(self.y, op.y))

    def max(self, op):
        if isinstance(op, float) or isinstance(op, int):
            return Vector2(max(self.x, op), max(self.y, op))
        else:
            return Vector2(max(self.x, op.x), max(self.y, op.y))

    def sign(self):
        return Vector2( self.x/abs(self.x), self.y/abs(self.y) )

    def sum(self):
        return self.x + self.y

    def direction(self, obj):
        dx = self.x - obj.x
        dy = self.y - obj.y
        angle = math.atan2(dy, dx)
        return Vector2(math.cos(angle), math.sin(angle))

    def distance(self, obj):
        dx = self.x - obj.x
        dy = self.y - obj.y
        return math.sqrt(pow(dx, 2) + pow(dy, 2))

    def tuple(self):
        return (self.x, self.y)

    def list(self):
        return [self.x, self.y]

if __name__ == "__main__":
    a = Vector2(1,5)
    b = Vector2(3,3)
    print(a.normalize().list())
