__author__ = 'stephenosullivan'

import heapq, queue

class Graph:
    class Vertex:
        def __init__(self, value=None):
            self.value = value
            self.adjacent = set()

        def addneighbor(self, vertex):
            self.adjacent.add(vertex)

    def __init__(self, directed=False):
        self.directed = directed
        self.vertexList = dict()
        self.edgeList = []

    def addVertex(self, label, value):
        self.vertexList[label] = self.Vertex(value)

    def addEdge(self, edge):
        v1, v2, w = edge
        heapq.heappush(self.edgeList,(w, edge))
        self.vertexList[v1].adjacent.add(v2)
        if not self.directed:
            heapq.heappush(self.edgeList,(w, (v2,v1,w)))
            self.vertexList[v2].adjacent.add(v1)

    def graphDFS(self, start, goal):
        stack = Stack()
        visited = set()
        stack.push([start])

        while not stack.isEmpty():
            path = stack.pop()
            #print(path)
            current = path[0]
            if current not in visited:
                visited.add(current)
                #print(current, goal)
                if current == goal:
                    return path

                for v in self.vertexList[current].adjacent:
                    if v not in path:
                        stack.push([v] + path)
        return []

    def graphBFS(self, start, goal):
        stack = Queue()
        visited = set()
        stack.push([start])

        while not stack.isEmpty():
            path = stack.pop()
            #print(path)
            current = path[0]
            if current not in visited:
                visited.add(current)
                #print(current, goal)
                if current == goal:
                    return path

                for v in self.vertexList[current].adjacent:
                    if v not in path:
                        stack.push([v] + path)
        return []

class Stack:
    def __init__(self):
        self.storage = []
        self.size = 0

    def pop(self):
        if self.size:
            self.size -= 1
            return self.storage.pop()
        else:
            raise IndexError

    def push(self, item):
        self.storage.append(item)
        self.size += 1

    def isEmpty(self):
        return not bool(self.size)

class Queue:
    def __init__(self):
        self.storage = []
        self.size = 0

    def pop(self):
        if self.size:
            self.size -= 1
            return self.storage.pop(0)
        else:
            raise IndexError

    def push(self, item):
        self.storage.append(item)
        self.size += 1

    def isEmpty(self):
        return not bool(self.size)

class Set:
    def __init__(self):
        pass



if __name__ == '__main__':
    g = Graph(directed=True)
    for i in range(30):
        g.addVertex(i, i)
    g.addEdge((0, 1, 2.02))
    g.addEdge((1, 4, 1.7))
    g.addEdge((4, 5, 3.28))
    g.addEdge((5, 7, 4.28))
    g.addEdge((5, 12, 3.3))
    g.addEdge((7, 22, 16.43))
    g.addEdge((12, 11, 2.16))
    g.addEdge((9, 10, 2.32))
    g.addEdge((9, 3, 5.02))
    g.addEdge((9, 17, 7.1))
    g.addEdge((10, 0, 6.2))
    g.addEdge((10, 1, 5.8))
    g.addEdge((10, 11, 1.67))
    g.addEdge((10, 17, 8.65))
    g.addEdge((3, 0, 4.45))
    g.addEdge((3, 2, 5.53))
    g.addEdge((17, 3, 10.81))
    g.addEdge((17, 6, 11.6))
    g.addEdge((17, 23, 11.76))
    g.addEdge((17, 24, 8.42))
    g.addEdge((2, 8, 4.64))
    g.addEdge((8, 13, 8.45))
    g.addEdge((6, 2, 3.41))
    g.addEdge((13, 14, 4.61))
    g.addEdge((13, 16, 7.32))
    g.addEdge((14, 15, 4.07))
    g.addEdge((14, 17, 13.47))
    g.addEdge((15, 16, 1.24))
    g.addEdge((16, 17, 9.01))
    g.addEdge((15, 17, 8.81))
    g.addEdge((23, 24, 2.18))
    g.addEdge((24, 27, 4.67))
    g.addEdge((27, 25, 3.51))
    g.addEdge((27, 29, 11.6))
    g.addEdge((25, 18, 6.17))
    g.addEdge((18, 17, 4.07))
    g.addEdge((25, 26, 1.86))
    g.addEdge((26, 19, 4.72))
    g.addEdge((19, 18, 1.54))
    g.addEdge((28, 20, 9.32))
    g.addEdge((28, 21, 6.66))
    g.addEdge((28, 29, 4.24))
    g.addEdge((20, 19, 1.53))
    g.addEdge((21, 20, 6.17))
    g.addEdge((21, 22, 4.66))

    print(g.graphDFS(9, 29))
    print(g.graphBFS(9, 29))
    print(g.edgeList)
    print(g.vertexList[1].adjacent)
    print(g.vertexList[9].adjacent)