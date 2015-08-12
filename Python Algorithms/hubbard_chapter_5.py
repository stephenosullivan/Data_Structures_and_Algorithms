__author__ = 'stephenosullivan'

class HashSet:
    def __init__(self, contains=[]):
        self.items = [None]*10
        self.numItems = 0

        for item in contains:
            self.add(item)

    def __add(item, items):
        idx = hash(item) % len(items)
        loc = -1

        while items[idx] is not None:
            if items[idx] == item:
                # item already in set
                return False

            if loc < 0 and type(items[idx]) == HashSet.__PlaceHolder:
                loc = idx

            idx = (idx + 1) % len(items)

        if loc < 0:
            loc = idx

        items[loc] = item

        return True

    def __rehash(oldList, newList):
        for x in oldList:
            if x is not None and type(x) != HashSet.__Placeholder:
                HashSet.__add(x, newList)
        return newList

    def add(self, item):
        if HashSet.__add(item, self.items):
            self.numItems += 1
            load = self.numItems / len(self.items)
            if load >= 0.75:
                self.items = HashSet.__rehash(self.items, [None]*2*len(self.items))

    def remove(self, item):
        if HashSet.__remove(item, self.items):
            self.numItems -= 1
            load = max(self.numItems, 10) / len(self.items)
            if load <= 0.25:
                self.items = HashSet.__rehash(self.items, [None]*int(len(self.items)/2))
        else:
            raise KeyError("Item not in HashSet")

    def discard(self, item):
        if HashSet.__remove(item, self.items):
            self.numItems -= 1
            load = max(self.numItems, 10) / len(self.items)
            if load <= 0.25:
                self.items = HashSet.__rehash(self.items, [None]*int(len(self.items)/2))


    def __contains__(self, item):
        idx = hash(item) % len(self.items)
        while self.items[idx] is not None:
            if self.items[idx] == item:
                return True

            idx = (idx + 1) % len(self.items)

        return False

    def __iter__(self):
        for i in range(len(self.items)):
            if self.items[i] is not None and type(self.items[i]) != HashSet.__PlaceHolder:
                yield self.items[i]

    def __remove(item, items):
        idx = hash(item) % len(items)

        while items[idx] is not None:
            if items[idx] == item:
                nextIdx = (idx + 1) % len(items)
                if items[nextIdx] is None:
                    items[idx] = None
                else:
                    items[idx] = HashSet.__Placeholder()
                return True

            idx = (idx + 1) % len(items)

        return False

    def difference_update(self, other):
        for item in other:
            self.discard(item)

    def difference(self, other):
        result = HashSet(self)
        result.difference_update(other)
        return result

    class __Placeholder:
        def __init__(self):
            pass

        def __eq__(self, other):
            return False

    def __getitem__(self, item):
        idx = hash(item) % len(self.items)
        while self.items[idx] is not None:
            if self.items[idx] == item:
                return self.items[idx]

            idx = (idx + 1) % len(self.items)
        return None




if __name__ == '__main__':
    myHashSet = HashSet()
    print(myHashSet.items)
    myHashSet.add(1)
    myHashSet.add(2)
    myHashSet.add(3)
    myHashSet.add(4)
    myHashSet.add(5)
    print(myHashSet.items)
    myHashSet.remove(4)
    print(myHashSet.items)
