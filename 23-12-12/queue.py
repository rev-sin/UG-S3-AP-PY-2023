class myqueue:

    def __init__(self, sz):
        self.s = None
        self.q = []
        self.f = 0
        self.r = -1
        self.max_size = sz
        for i in range(0, self.max_size):
            self.q.append(None)
        self.size = 0

    def enque(self, item):
        if self.size == self.max_size:
            print("Queue is full")
        else:
            self.r = self.r + 1
            self.q[self.r] = item
            self.size += 1

    def isempty(self):
        return self.size == 0

    def queuesize(self):
        print(self.size)

    def deque(self):
        if self.isempty():
            print("Queue is empty")
        else:
            self.q[self.f] = None
            self.f = self.f + 1
            self.size = self.size - 1

    def front(self):
        if self.size != 0:
            return self.q[self.s]

    def displayqueue(self):
        if self.isempty():
            print("Queue is empty")
        else:
            for i in range(self.max_size):
                if self.q[i] is not None:
                    print(self.q, " ")


k = myqueue(5)
k.enque(10)
k.enque(20)
k.enque(30)
k.enque(40)
k.deque()
k.displayqueue()
