__author__ = 'stephenosullivan'

import xml.etree.ElementTree as ET
from decimal import getcontext, Decimal
tree = ET.parse('graph.xml')
root = tree.getroot()

getcontext().prec = 3

class Vertex:
    def __init__(self, label):
        #self.vertexId = vertexId
        self.label = label
        self.adjacent = set()
        self.previous = None

class Edge:
    def __init__(self, v1, v2, weight=0):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = set()

    def build_adjacency_list(self, vertices, edges):
        for vertex in vertices:
            self.addvertex(vertex)
        for edge in edges:
            self.addedge(edge)

    def addvertex(self, v):
        if v not in self.vertices:
            #print(repr(v))
            self.vertices[v] = Vertex(v)
            #print(self.vertices[v].adjacent)

    def addedge(self, edge):
        (v1, v2, w) = edge
        self.edges.add(Edge(v1, v2, w))
        if v1 not in self.vertices:
            self.addvertex(v1)
        if v2 not in self.vertices:
            self.addvertex(v2)
        self.vertices[v1].adjacent.add((v2, w))

    def bfs(self, start, end):
        queue = [(start, 1)]
        visited = set()
        while queue:
            current, count = queue.pop(0)
            for neighbor, w in current.adjacent:
                if neighbor == end.label:
                    return count
                if neighbor not in visited:
                    queue.append((self.vertices[neighbor], count + 1))
                visited.add(neighbor)
        return None

    def dijkstra(self, start):
        queue = [(start, Decimal(0))]
        self.vertices[start].previous = Decimal(0)
        while queue:
            print(queue)
            current, weight = queue.pop(0)
            #print(type(self.vertices[current]))
            #print("test", current)
            for (neighbor, edge_weight) in self.vertices[current].adjacent:
                #print(neighbor.label)
                if self.vertices[neighbor].previous is None:
                    self.vertices[neighbor].previous = weight + Decimal(edge_weight)
                    queue.append((neighbor, self.vertices[neighbor].previous))
                elif self.vertices[neighbor].previous > weight + Decimal(edge_weight):
                    self.vertices[neighbor].previous = weight + Decimal(edge_weight)
                    queue.append((neighbor, self.vertices[neighbor].previous))

        return [(label, vertex.previous) for (label, vertex) in self.vertices.items()]

    #def kruskal(self):
        # sort edges

    #def shortest_path(self, start, end):



if __name__ == '__main__':
    directed = False
    """Load data from XML file"""
    Vertices = set()
    Edges = set()
    V_map = {}
    for child in root:
        for grandchild in child:
            if grandchild.tag == 'Vertex':
                Vertices.add(int(grandchild.attrib['label']))
                V_map[grandchild.attrib['vertexId']] = grandchild.attrib['label']
            if grandchild.tag == 'Edge':
                Edges.add((int(V_map[grandchild.attrib['tail']]), int(V_map[grandchild.attrib['head']]), float(grandchild.attrib['weight'])))
                if directed is False:
                    Edges.add((int(V_map[grandchild.attrib['head']]), int(V_map[grandchild.attrib['tail']]), float(grandchild.attrib['weight'])))

    graph = Graph()
    for vertex in Vertices:
        graph.addvertex(vertex)

    for edge in Edges:
        graph.addedge(edge)

    """Need to make some adjustments to match graph in Fig.7.9"""
    if directed:
        graph.vertices[2].adjacent = {(8, 4.64)}
        graph.vertices[8].adjacent = {(13, 8.45)}
        graph.vertices[13].adjacent = {(14, 4.61), (16, 7.32)}
        graph.vertices[17].adjacent = {(3, 10.81), (6, 11.6), (23, 11.76), (24, 8.42)}
        graph.vertices[18].adjacent = {(17, 4.07)}
        graph.vertices[19].adjacent = {(18, 1.54)}
        graph.vertices[23].adjacent = {(24, 2.18)}



    print(graph.bfs(graph.vertices[9], graph.vertices[16]))
    print(graph.dijkstra(0))
    #print(graph.vertices[29].adjacent)
    #print(graph.vertices[28].adjacent)
