class Node:
    def __init__(self, value, nextnode):
        self.value = value
        self.next = nextnode


class Graph:
    def __init__(self):
        self.nodes = {}
        self.neighbors = {}

    def addnode(self, id, node):
        self.nodes[id] = node

    def addedge(self, id1, id2):
        #adding second node to the neightbro list of the first ndoe
        value1 = self.neighbors.get(id1, [])
        self.neighbors[id1] = value1.append(id2)
        #adding the frist node into the neigtbro list of the second node
        value2 = self.neighbors.get(id2, [])
        self.neighbors[id2] = value1.append(id1)





