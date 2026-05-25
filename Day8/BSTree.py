import sys

class BST:
    def __init__(self, key=None):
        self.leftChild = None
        self.data = key
        self.rightChild = None

    def insert(self, key):
        if self.data is None:
            self.data = key
            return

        if self.data == key:
            return

        if key < self.data:
            if self.leftChild:
                self.leftChild.insert(key)
            else:
                self.leftChild = BST(key)

        else:
            if self.rightChild:
                self.rightChild.insert(key)
            else:
                self.rightChild = BST(key)

    def preorder(self):
        if self.data is not None:
            print(self.data, end=" ")

        if self.leftChild:
            self.leftChild.preorder()

        if self.rightChild:
            self.rightChild.preorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()

        if self.rightChild:
            self.rightChild.postorder()

        if self.data is not None:
            print(self.data, end=" ")

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()

        if self.data is not None:
            print(self.data, end=" ")

        if self.rightChild:
            self.rightChild.inorder()
    
    def Search(self):
        pass 


if __name__ == '__main__':
    root = BST()

    while True:
        print("\n1. Insert")
        print("2. Preorder")
        print("3. Postorder")
        print("4. Inorder")
        print("5. Search")
        print("0. Exit")

        n = int(input("Select any choice: "))

        if n == 1:
            arr = [26, 26, 46, 57, 68, 79, 89, 51, 63, 77, 66]

            for i in range(len(arr)):
                root.insert(arr[i])

            print("Nodes inserted")

        elif n == 2:
            print("Preorder Traversal:")
            root.preorder()
            print()

        elif n == 3:
            print("Postorder Traversal:")
            root.postorder()
            print()

        elif n == 4:
            print("Inorder Traversal:")
            root.inorder()
            print()

        elif n == 0:
            sys.exit()

        else:
            print("Invalid Choice")