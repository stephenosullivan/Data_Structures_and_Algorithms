__author__ = 'stephenosullivan'

import xml.etree.ElementTree as ET
tree = ET.parse('graph.xml')
root = tree.getroot()

class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    def path(self, start, end):
        vertices_to_visit = [start]
        visited = []
        output = [start]
        visited.append(start)
        outputs = []

        while output:
            pop = True
            for edge in self.edges:

                if edge[0] == output[-1] and edge[1] not in visited:
                    print(output)
                    output.append(edge[1])
                    pop = False
                    if edge[1] == end:
                        outputs.append(output[:])
                        output.pop()
                        pop = True
                    else:
                        visited.append(edge[1])
                    break

            if pop:
                backpoint = output.pop()
                print("v1", visited)
                while len(visited) > 1 and visited[-1] != backpoint and visited[-2] != backpoint:
                        visited.pop()
                print('v2',visited)

        if outputs:
            return outputs
        else:
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
