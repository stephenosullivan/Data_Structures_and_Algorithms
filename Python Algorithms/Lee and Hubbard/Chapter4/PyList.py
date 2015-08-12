__author__ = 'stephenosullivan'


class PyList:
    def __init__(self, contents=[], size=10):
        self.items = [None] * size
        self.numItems = 0  # number of locations used
        self.size = size

        for e in contents:
            self.append(e)

    def __getitem__(self, index):
        try:
            return self.items[index]
        except:
            raise IndexError("PyList index out of range")

    def __setitem__(self, index, val):
        try:
            self.items[index] = val
        except:
            raise IndexError("PyList assignment index out of range")

    def __add__(self, other):
        output = PyList(size=self.numItems + other.numItems)

        for i in range(self.numItems):
            output.append(self.items[i])

        for i in range(other.numItems):
            output.append(other.items[i])

        return output

    def __makeroom(self):
        addsize = self.size // 4 + 1
        self.size += addsize
        self.items += [None] * addsize

    def append(self, item):
        if self.numItems == self.size:
            self.__makeroom()

        self.items[self.numItems] = item
        self.numItems += 1

    def insert(self, index, value):
        if self.numItems == self.size:
            self.__makeroom()

        if index < self.numItems:
            for i in range(self.numItems, self.numItems - index, -1):
                self.items[i] = self.items[i - 1]
            self.items[index] = value
            self.numItems += 1

        else:
            self.append(value)

    def __delitem__(self, index):
        for i in range(index, self.numItems):
            self.items[i] = self.items[i+1]
        self.numItems -= 1

    def __eq__(self, other):
        # Type check
        if type(self) != type(other):
            return False

        # size check
        if self.numItems != other.numItems:
            return False

        # values check
        for i in range(self.numItems):
            if self.items[i] != other.items[i]:
                return False

        return True

    def __iter__(self):
        for i in range(self.numItems):
            yield self.items[i]

    def __len__(self):
        return self.numItems

    def __contains__(self, item):
        for i in range(self.numItems):
            if self.items[i] == item:
                return True
        return False

    def __str__(self):
        s = "["
        for i in range(self.numItems):
            s += repr(self.items[i])
            if i < self.numItems - 1:
                s += ", "
        s += "]"
        return s

    def __repr__(self):
        s = "PyList(["
        for i in range(self.numItems):
            s += repr(self.items[i])
            if i < self.numItems - 1:
                s += ", "
        s += "])"
        return s


if __name__ == '__main__':
    a = PyList([5, 6, 7])
    print(a)
