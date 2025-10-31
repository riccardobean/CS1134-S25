import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self, iterable = None):
        if iterable is None:
            self.data_arr = make_array(1)
            self.capacity = 1
            self.n = 0
        else:
            length = len(iterable)
            self.data_arr = make_array(length)
            self.capacity = length
            self.n = length
            for i in range(length):
                self[i] = iterable[i]


    def __len__(self):
        return self.n


    def append(self, val):
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1


    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data_arr[i]
        self.data_arr = new_array
        self.capacity = new_size


    def __getitem__(self, ind):
        if not (-self.n <= ind <= self.n - 1):
            raise IndexError('invalid index')
        if ind < 0:
            ind += self.n
        return self.data_arr[ind]


    def __setitem__(self, ind, val):
        if not (-self.n <= ind <= self.n - 1):
            raise IndexError('invalid index')
        if ind < 0:
            ind += self.n
        self.data_arr[ind] = val


    def __iter__(self):
        for i in range(len(self)):
            yield self.data_arr[i]  #could also yield self[i]


    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)

    def __repr__(self):
        if self.n >= 1:
            ret_str = "["
            for i in range(self.n - 1):
                ret_str += f"{self.data_arr[i]}, "
            ret_str += f"{self.data_arr[self.n - 1]}]"
            return ret_str
        return "[]"

    def __add__(self, other):
        added = ArrayList()
        added.extend(self)
        added.extend(other)
        return added

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __mul__(self, other):
        mult = ArrayList()
        for i in range(other):
            mult.extend(self)
        return mult

    def __rmul__(self, other):
        mult = ArrayList()
        for i in range(other):
            mult.extend(self)
        return mult

    def remove(self, val):
        found = False
        i = 0
        while not found and i < self.n:
            if self[i] == val:
                found = True
                ind = i
            i += 1
        if found:
            for i in range(ind, self.n - 1):
                self[i] = self[i + 1]
            self.n -= 1

    def remove_odds(self):
        j = 0
        counter = 0
        for i in range(self.n):
            if self[i] % 2 == 0:
                self[j] = self[i]
                j += 1
            else:
                counter += 1
        self.n -= counter

    def insert(self, index, val):
        if not (-self.n <= index <= self.n - 1):
            raise IndexError('invalid index')
        old_n = self.n - 1
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        self.n += 1
        for i in range(old_n, index - 1, -1):
            self[i+1] = self[i]
        self[index] = val

    def pop(self, index = -1):
        if len(self) == 0 or not (-self.n <= index <= self.n - 1):
            raise IndexError('invalid index')
        ret = self[index]
        self[index] = None
        if index >= 0:
            for i in range(index, self.n - 1):
                self[i] = self[i+1]
        else:
            for i in range(len(self) + index, self.n-1):
                self[i] = self[i+1]
        self.n -= 1
        if self.n < 1/4 * self.capacity:
            self.resize(self.capacity // 2)
        return ret