__author__ = 'stephenosullivan'

import time
from Priority_Queue import Priority_Queue

class Graph:
    def __init__(self, directed=False):
        self.vertexList = dict()
        self.edgeList = Priority_Queue()
        self.directed = directed

    class Node:
        def __init__(self, value):
            self.value = value

    class Vertex(Node):
        def __init__(self, value):
            super().__init__(value)
            self.neighbors = set()

        def addneighbor(self, vertex, weight):
            self.neighbors.add((vertex, weight))

        def removeneighbor(self, label):
            for neighbor in self.neighbors:
                if neighbor[0] == label:
                    self.neighbors.remove(neighbor)

    class Edge:
        def __init__(self, vertex1, vertex2, weight=0):
            self.vertex1 = vertex1
            self.vertex2 = vertex2
            self.weight = weight

        def __lt__(self, other):
            return self.weight < other.weight

    def addVertex(self, label, value=None):
        self.vertexList[label] = self.Vertex(value)

    def removeVertex(self, label):
        self.vertexList.pop(label)
        for vertex in self.vertexList.keys():
            if label in vertex.neighbors:
                vertex.neighbors.remove(label)

    def addEdge(self, edge):
        (v1, v2, w) = edge
        self.edgeList.enqueue((w, self.Edge(v1, v2, w)))
        if v1 not in self.vertexList:
            self.addVertex(v1)
        if v2 not in self.vertexList:
            self.addVertex(v2)

        self.vertexList[v1].addneighbor(v2, w)
        if self.directed is False:
            self.vertexList[v2].addneighbor(v1, w)

    def removeedge(self, label1, label2):
        for item in self.edgeList:
            w, edge = item
            if edge[0] == label1 and edge[0] == label2:
                self.edgeList.dequeue(item)
                if self.directed is False:
                    self.removeedge(label2, label1)

    def __repr__(self):
        return "Vertices" + repr(__dict__[self.vertexList]) + '\n' \
               + "Edge"

    def dijkstra2(self, start):
        unvisited = Priority_Queue()
        unvisited.enqueue((0, start))
        visited = set()
        distance = dict()
        infinity = 10000
        prev = dict()
        for label in self.vertexList:
            distance[label] = infinity
            prev[label] = None
        distance[start] = 0
        prev[start] = start
        while unvisited:
            initial_cost, label = unvisited.dequeue()
            visited.add(label)
            for neighbor, weight in self.vertexList[label].neighbors:
                if neighbor not in visited:
                    cost = initial_cost + weight
                    if cost < distance[neighbor]:
                        distance[neighbor] = cost
                        prev[neighbor] = label
                        if neighbor not in unvisited:
                            unvisited.enqueue((cost, neighbor))
                        else:
                            unvisited[neighbor] = cost

        return distance, prev


    def dijkstra(self, start, end):
        distance = dict()
        infinity = 10000
        for label in self.vertexList:
            distance[label] = infinity
        distance[start] = 0
        visited = set()
        minQueue = Priority_Queue()
        minQueue.enqueue((0, (start, start)))
        while minQueue:
            w, edge = minQueue.dequeue()
            if distance[edge[1]] > distance[edge[0]] + w:
                distance[edge[1]] = distance[edge[0]] + w
            if edge[1] not in visited:
                for label, weight in self.vertexList[edge[1]].neighbors:
                    #print(label, weight, edge[1])
                    minQueue.enqueue((weight, (edge[1], label)))
                visited.add(edge[1])
            # if distance[end] < infinity:
            #     shorterpath = False
            #     for weight, item in minQueue:
            #         if item[0] < 12:
            #             print(item[0], distance[item[0]])
            #         if distance[item[0]] < distance[end]:
            #             shorterpath = True
            #             break
            #     if not shorterpath:
            #         return distance[end]
        if distance[end] < infinity:
            return distance[end]
        else:
            return False

    def bfs(self, start, end):
        SENTINEL = object()
        nodes_to_visit = [self.vertexList[start], SENTINEL]
        cnt = 0
        while nodes_to_visit:
            node = nodes_to_visit.pop(0)
            if node is SENTINEL:
                cnt += 1
                nodes_to_visit.append(SENTINEL)
            elif node == self.vertexList[end]:
                return cnt
            else:
                for vertex, _ in node.neighbors:
                    nodes_to_visit.append(self.vertexList[vertex])
        return False

    def bfs1(self, start, end):
        SENTINEL = object()
        nodes_to_visit = [start, SENTINEL]
        cnt = 0
        while nodes_to_visit:
            node = nodes_to_visit.pop(0)
            if node is SENTINEL:
                cnt += 1
                nodes_to_visit.append(SENTINEL)
            elif node == end:
                return cnt
            else:
                for vertex, _ in node.neighbors:
                    nodes_to_visit.append(vertex)
        return False

if __name__ == '__main__':
    g = Graph(directed=False)
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
    g.addEdge((15, 16, 8.81))
    g.addEdge((15, 17, 1.24))
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

    print(g.vertexList[0].value)
    print([i.weight for w, i in g.edgeList])
    print(len(g.edgeList))
    print(g.vertexList[9].value)
    print(g.bfs(9, 29))
    start = time.time()
    print(g.bfs(6, 29))
    mid = time.time()
    print(g.bfs(6, 29))
    end = time.time()
    print("Version 2: %.8f" % (end-mid))
    print("Version 1: %.8f" % (mid-start))

    print(g.dijkstra2(0))
    # for i in range(30):
    #     distance = g.dijkstra(0, i)
    #     if distance is False:
    #         print('Cannot go from %d to %d' % (0, i))
    #     else:
    #         print('Distance from %d to %d is %.2f' % (0, i, distance))

#[(0, Decimal('0')), (1, Decimal('2.02')), (2, Decimal('9.98')), (3, Decimal('4.45')), (4, Decimal('3.72')), (5, Decimal('7.00')), (6, Decimal('13.4')), (7, Decimal('11.3')), (8, Decimal('14.6')), (9, Decimal('8.52')), (10, Decimal('6.20')), (11, Decimal('7.87')), (12, Decimal('10.0')), (13, Decimal('23.0')), (14, Decimal('27.6')), (15, Decimal('23.7')), (16, Decimal('23.9')), (17, Decimal('14.9')), (18, Decimal('19.0')), (19, Decimal('20.5')), (20, Decimal('22.0')), (21, Decimal('28.2')), (22, Decimal('27.7')), (23, Decimal('25.5')), (24, Decimal('23.3')), (25, Decimal('25.2')), (26, Decimal('25.2')), (27, Decimal('28.0')), (28, Decimal('31.3')), (29, Decimal('35.5'))]
