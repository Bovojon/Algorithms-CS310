#!/usr/bin/env python
# -*- coding: utf-8 -*-

from glob import glob


class Edges():
    def __init__(self, value):
        self._value = value
        self._next = None

    def getName(self):
        return self._value

    def getNext(self):
        return self._next


class Nodes():
    def __init__(self, value):
        self._value = value
        self._pointer = None  # empty

    def name(self):
        return self._value

    def setName(self, newname):
        self._value = newname

    def firstEdge(self):
        return self._pointer

    def addEdge(self, value):
        temp = Edges(value)
        temp._next = self._pointer
        self._pointer = temp

    def travel(self):
        edges = []
        present = self.firstEdge()
        while present is not None:
            edges.append(present)
            present = present.getNext()
        return edges


class Graph():
    def __init__(self):
        self.graph = []

    def searchCity(self, value):
        if value not in self.graph:
            node = Nodes(value)
            self.graph.append(node)
        return self._index(value)

    def _index(self, value):
        for n in self.graph:
            if n.name() == value:
                return self.graph.index(n)


def buildGraph(filename):
    "Open and read graph from file"""
    f = open(filename, "r")
    value = set()
    edge_adj = []
    for line in f:
        line = line.strip('\n')
        line = line.split(" ")
        for edge in line:
            edge = edge.split('-')
            edge_adj.append(edge)
            value.add(edge[0])
            value.add(edge[1])
            f.close

    # Create instance of Graph class:
    G = Graph()

    # build the adj-list
    for i in value:
        index = G.searchCity(i)
        for x in edge_adj:
            if x[0] == i:
                G.graph[index].addEdge(x[1])

    return G


def graph_adt_test(G):
    """test graph abstract data type and print graph nodes"""
    for i in G.graph:
        node = i.name()
        index = G._index(node)
        print("Node:", index, ",", "Name:", node)
        edges = G.graph[index].travel()
        for e in edges:
            print(e.getName())
            print("#------------")


# --------------------------------------------------------------------------- #

def countEdges(G):
    """Count the number of edges in the graph data type"""
    E = []
    for node in G:
        for edge in node.travel():
            E.append(1)
    return sum(E) // 2


def connectedComponents(G):
    """Find connected components in undirected graph
    using simplified depth-first-search
    """

    components = []

    for node in G.graph:
        stack = []
        visited = set()

        stack.append(node)
        visited.add(node.name())

        while stack:
            connected = stack.pop()
            for edge in connected.travel():
                e = edge.getName()
                if e not in visited:
                    node = G.graph[G._index(e)]
                    stack.append(node)
                    visited.add(e)
        if visited not in components:
            components.append(visited)

    return components


def outputGraph(G):
    """Print output for project 2"""
    cities = len(G.graph)
    edges = countEdges(G.graph)
    components = connectedComponents(G)

    print("Read", cities, "cites and", edges, "edges")
    print("Number of connected components", len(components))
    count = 0
    cycle = False
    for c in components:
        count += 1
        C = [G.graph[G._index(x)] for x in c]
        v = len(c)
        e = countEdges(C)

        if v <= e:
            cycle = True

        print("  Connected Component", count)
        for node in c:
            print("    ", node)

    if cycle:
        print("Graph contains a cycle")
    else:
        "Graph does not contain a cycle"

# G = build_graph("input/graphSmall3.in")
# output_graph(G)

if __name__ == "__main__":
    input_files = glob("input/*")

    for f in input_files:
        G = buildGraph(f)
        print(f)
        outputGraph(G)
        print()
