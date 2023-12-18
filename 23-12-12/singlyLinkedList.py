class slist:
    class node:
        def __init__(self, data):
            self.element = data
            self.next = None

    def __init__(self):
        self.head = self.node(None)
        self.size = 0

    def insertfirst(self, item):
        newnode = self.node(item)
        if self.size == 0:
            self.head.element = newnode.element
        else:
            newnode.next = self.head
            self.head = newnode
        self.size += 1

    def printlist(self):
        if self.isempty():
            print("List is Empty")
        else:
            currentnode = self.head
            while currentnode is not None:
                print(currentnode.element, end=" ")
                currentnode = currentnode.next

    def isempty(self):
        return self.size == 0

    def insertlast(self, item):
        newnode = self.node(item)

        currentnode = self.head
        while currentnode is not None:
            currentnode = currentnode.next

        currentnode.next = newnode
        self.size += 1

    def deletefirst(self):
        if self.isempty():
            print("List is Empty")
        else:
            if self.head.next == None:
                self.head.element = None
            else:
                temp = self.head
                self.head = self.head.next
                del temp
                self.size -= 1


l1 = slist()
l1.insertfirst(25)
l1.insertfirst(35)
l1.insertfirst(15)
l1.printlist()
