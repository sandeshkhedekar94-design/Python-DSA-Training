import sys

class stacks:

    def __init__(self):
        self.stack = []
        self.top = -1
        self.CAPACITY = 100

    def isFull(self):
        return self.top == self.CAPACITY - 1

    def isEmpty(self):
        return self.top == -1

    def push(self, ele):
        if self.isFull():
            print("Stack is Full")
        else:
            self.top += 1
            self.stack.append(ele)

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            ele = self.stack.pop()
            self.top -= 1
            return ele


if __name__ == '__main__':

    obj = stacks()

    string = input("Enter a string: ")

    for ch in string:
        obj.push(ch)

    reversed_string = ""

    while not obj.isEmpty():
        reversed_string += obj.pop()

    print("Original String:", string)
    print("Reversed String:", reversed_string)