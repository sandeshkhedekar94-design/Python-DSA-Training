class Graphs:
    def __init__




if __name__ == '__main__':
    obj = Graphs()
    
    print("\n 1. (Insertion) add a node using adjaceny matrix represent")
    print("2. (Insertion) add a edge using adjaceny matrix representation")
    print("3. (Insertion) add a edge undirected weighted graph")
    print("4. (Insertion) add a edge directed weighted graph")
    print("5. Print Graph")
    print("6. Delete Operation")
    print("0. Exit\n")
    n = int(input("Enter any choice:"))
    if n==1:
        obj.addNode()
    elif n==2:
        obj.addEdge_Undirected_Unweighted()
    elif n == 3:
        obj.addEdge_Undirected_Weighted()
    elif n == 4:
        obj.addEdge_Directed_Weighted()

    elif n == 5:
            obj.printGraph()

    elif n == 6:
            obj.deleteGraph()

    elif n == 0:
            sys.exit(0)
            