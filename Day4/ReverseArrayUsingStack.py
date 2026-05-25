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

    arr = [10, 20, 30, 40, 50]

    print("Original Array:")
    print(arr)

    for i in arr:
        obj.push(i)

    for i in range(len(arr)):
        arr[i] = obj.pop()

    print("Reversed Array:")
    print(arr)