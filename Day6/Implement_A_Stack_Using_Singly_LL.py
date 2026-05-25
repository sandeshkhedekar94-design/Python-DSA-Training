import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode
        print(data, "inserted into stack")

    def pop(self):
        if self.top == None:
            print("Stack Underflow")
        else:
            temp = self.top
            print(temp.data, "deleted from stack")
            self.top = self.top.next
            del temp

    def peek(self):
        if self.top == None:
            print("Stack is Empty")
        else:
            print("Top element is:", self.top.data)

    def traverse(self):
        if self.top == None:
            print("Stack is Empty")
        else:
            ptr = self.top
            print("Stack elements are:")
            while ptr != None:
                print(ptr.data)
                ptr = ptr.next

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False


if __name__ == '__main__':

    obj = Stack()

    while True:

        print("\n1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            data = int(input("Enter data: "))
            obj.push(data)

        elif choice == 2:
            obj.pop()

        elif choice == 3:
            obj.peek()

        elif choice == 4:
            obj.traverse()

        elif choice == 0:
            sys.exit()

        else:
            print("Invalid Choice")