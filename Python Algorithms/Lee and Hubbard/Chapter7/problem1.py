__author__ = 'stephenosullivan'

import xml.etree.ElementTree as ET
tree = ET.parse('graph.xml')
root = tree.getroot()

class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    def path(self, start, end):
        def _path(self, start, end):
            vertices_to_visit = [start]
            visited = set()
            return start + _path()


        while vertices_to_visit:
            vertex = vertices_to_visit.pop()
            visited.add(vertex)
            output.append(vertex)
            pop = False
            for edge in self.edges:
                print(edge[0], edge[1], edge[2])
                if edge[0] == vertex and edge[1] not in visited:
                    vertices_to_visit.append(edge[1])
                    if edge[1] == end:
                        output.append(end)
                        return output
                    pop = True
            if pop is False:
                output.pop()
        return False

if __name__ == '__main__':
    Vertices = set()
    Edges = set()
    V_map = {}
    for child in root:
        for grandchild in child:
            if grandchild.tag == 'Vertex':
                Vertices.add(grandchild.attrib['label'])
                V_map[grandchild.attrib['vertexId']] = grandchild.attrib['label']
            if grandchild.tag == 'Edge':
                Edges.add((int(V_map[grandchild.attrib['tail']]), int(V_map[grandchild.attrib['head']]), float(grandchild.attrib['weight'])))

    # for item in Vertices:
    #     print(item)
    # for item in Edges:
    #     print(item)

    graph = Graph(Vertices, Edges)
    print(graph.path(9, 29))
