class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print("Link List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->", end=" ")
                n = n.ref

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_afterNode(self,data,x):
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in link list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

node = LinkedList()
node.add_begin(10)
node.add_end(50)
node.add_end(60)
node.add_begin(13)
node.add_begin(9)
node.add_afterNode(11, 10)
node.add_afterNode(70, 60)

node.printList()




