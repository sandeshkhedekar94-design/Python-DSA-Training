import sys

class Graphs:
    def __init__(self):
        self.nodes = []
        self.graph = []
        self.nodeCount = 0

    def addNode(self, v):

        if v in self.nodes:
            print(v, "is already present")

        else:
            self.nodeCount += 1
            self.nodes.append(v)

            for x in self.graph:
                x.append(0)

            temp = []

            for x in range(self.nodeCount):
                temp.append(0)

            self.graph.append(temp)

            print(v, "is added")

    def addEdge_Undirected_Unweighted(self):

        v1 = input("Enter vertex1: ")
        v2 = input("Enter vertex2: ")

        if v1 not in self.nodes:
            print(v1, "not present")
            return

        if v2 not in self.nodes:
            print(v2, "not present")
            return

        index1 = self.nodes.index(v1)
        index2 = self.nodes.index(v2)

        self.graph[index1][index2] = 1
        self.graph[index2][index1] = 1

        print("Edge added")

    def addEdge_Undirected_Weighted(self):
        pass

    def addEdge_Directed_Weighted(self):
        pass

    def deleteGraph(self, v):

        if v not in self.nodes:
            print(v, "not present")

        else:
            self.nodeCount -= 1

            index1 = self.nodes.index(v)

            self.nodes.pop(index1)

            self.graph.pop(index1)

            for x in self.graph:
                x.pop(index1)

            print(v, "is deleted")

    def printGraph(self):

        print("  ", *self.nodes)

        for i in range(self.nodeCount):

            print(self.nodes[i], end=" ")

            for j in range(self.nodeCount):

                print(self.graph[i][j], end=" ")

            print()


obj = Graphs()

while True:

    print("\n1. Add Node")
    print("2. Add Edge")
    print("3. Print Graph")
    print("4. Delete Node")
    print("5. Exit")

    n = int(input("Enter choice: "))

    if n == 1:

        v = input("Enter vertex: ")

        obj.addNode(v)

    elif n == 2:

        obj.addEdge_Undirected_Unweighted()

    elif n == 3:

        obj.printGraph()

    elif n == 4:

        v = input("Enter vertex to delete: ")

        obj.deleteGraph(v)

    elif n == 5:

        sys.exit()

    else:

        print("Invalid choice")