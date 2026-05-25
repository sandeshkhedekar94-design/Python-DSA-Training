import sys

class GetNode:
    def __init__(self):
        self.data=None
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self):
        data=int(input("Enter data: "))
        newNode=GetNode()
        newNode.data=data

        if self.head==None:
            self.head=newNode
        else:
            ptr=self.head

            while ptr.next!=None:
                ptr=ptr.next

            ptr.next=newNode

        print(data, "is added")

    def addAtBeginning(self):
        data=int(input("Enter data: "))
        newNode=GetNode()
        newNode.data=data

        newNode.next=self.head
        self.head=newNode

        print(data, "is added at beginning")

    def traverse(self):
        if self.head==None:
            print("Linked List not Present")
        else:
            ptr=self.head

            while ptr!=None:
                print(ptr.data," -> ",end="")
                ptr=ptr.next

            print("None")


if __name__ == '__main__':
    obj=LinkedList()

    while True:
        print("\n1. Append")
        print("2. Add At Beginning")
        print("3. Traverse")
        print("0. Exit")

        n=int(input("Select Any Choice: "))

        if n==1:
            obj.append()

        elif n==2:
            obj.addAtBeginning()

        elif n==3:
            obj.traverse()

        elif n==0:
            sys.exit()