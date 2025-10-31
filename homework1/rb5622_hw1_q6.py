class Vector:

    def __init__(self, d):
        if str(d).isdigit():
            self.coords = [0] * d
        else:
            self.coords = d

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, j):
        return self.coords[j]

    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")

        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")

        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        lst = []
        for i in range(len(self.coords)):
            lst.append(-self.coords[i])
        return Vector(lst)

    def __mul__(self, other):
        lst = []
        if str(other).isdigit():
            for el in self.coords:
                lst.append(int(el) * int(other))
            return Vector(lst)

        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        for i in range(len(self.coords)):
            lst.append(int(self.coords[i]) * int(other.coords[i]))
        return sum(lst)

    def __rmul__(self, other):
        lst = []
        for el in self.coords:
            lst.append(int(el) * int(other))
        return Vector(lst)

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return "<" + str(self.coords)[1:-1] + ">"

    def __repr__(self):
        return str(self)