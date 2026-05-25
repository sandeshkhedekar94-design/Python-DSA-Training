import sys
class Stacks:
    def __init__(self):
        self.stack = []
        self.top = -1
        self.CAPACITY = 5
    def isFull(self):
        if self.top == self.CAPACITY - 1:
            return True
        else:
            return False

    def isEmpty(self):

        if self.top == -1:
            return True
        else:
            return False

    def push(self):

        if self.isFull():
            print("Stack is Full")

        else:
            ele = int(input("Enter element: "))
            self.stack.append(ele)
            self.top += 1
            print(ele, "is pushed")

    def pop(self):

        if self.isEmpty():
            print("Stack is Empty")

        else:
            ele = self.stack.pop()
            self.top -= 1
            print(ele, "is popped")

    def peek(self):

        if self.isEmpty():
            print("Stack is Empty")

        else:
            print("Top element is:", self.stack[self.top])

    def traverse(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("Stack elements are:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])

class Queue:

    def __init__(self):
        self.queue = []
        self.rear = -1
        self.front = 0
        self.CAPACITY = 5

    def isFull(self):

        if self.rear == self.CAPACITY - 1:
            return True
        else:
            return False

    def isEmpty(self):
        if self.rear == -1:
            return True
        else:
            return False
    def insert(self, ele):
        if self.isFull():
            print("Queue is Full")
        else:
            self.rear += 1
            self.queue.append(ele)
            print(ele, "is inserted")

    def delete(self):
        if self.isEmpty():
            print("Queue is Empty")

        else:

            ele = self.queue[0]
            for i in range(1, self.rear + 1):
                self.queue[i - 1] = self.queue[i]
            self.queue.pop()
            self.rear -= 1

            print(ele, "is deleted")

    def peek(self):

        if self.isEmpty():
            print("Queue is Empty")

        else:
            print("Front element is:", self.queue[0])

    def traverse(self):

        if self.isEmpty():
            print("Queue is Empty")

        else:
            print("Queue elements are:")

            for i in range(self.rear + 1):
                print(self.queue[i])

if __name__ == '__main__':

    stack_obj = Stacks()
    queue_obj = Queue()

    while True:

        print(" MAIN MENU ")
        print("1. Stack Operations")
        print("2. Queue Operations")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            while True:

                print(" STACK MENU ")
                print("1. Push")
                print("3. Peek")
                print("4. Traverse")
                print("0. Back")

                ch = int(input("Select any option: "))

                if ch == 1:
                    stack_obj.push()

                elif ch == 2:
                    stack_obj.pop()

                elif ch == 3:
                    stack_obj.peek()

                elif ch == 4:
                    stack_obj.traverse()

                elif ch == 0:
                    break

                else:
                    print("Invalid Choice")
        elif choice == 2:
            while True:
                print(" QUEUE MENU ")
                print("1. Insert")
                print("2. Delete")
                print("3. Peek")
                print("4. Traverse")
                print("0. Back")

                ch = int(input("Select any choice: "))

                if ch == 1:
                    ele = int(input("Enter data: "))
                    queue_obj.insert(ele)

                elif ch == 2:
                    queue_obj.delete()

                elif ch == 3:
                    queue_obj.peek()

                elif ch == 4:
                    queue_obj.traverse()

                elif ch == 0:
                    break

                else:
                    print("Invalid Choice")

        elif choice == 0:
            sys.exit(0)
        else:
            print("Invalid Choice")