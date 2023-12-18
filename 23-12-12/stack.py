class mystack():
    def __init__(self, size):
        self.s = []
        self.max = size
        self.top = -1

        for i in range(0, self.max):
            self.s.append(None)

    def push(self, item):
        self.top += 1
        self.s[self.top] = item

    def isempty(self):
        return self.top < 0

    def stack(self):
        return self.top + 1

    def printstack(self):
        if self.isempty():
            print("stack is empty")
        else:
            for i in range(self.max):
                if self.s[i] is not None:
                    print(self.s[i])


k = mystack(6)
k.push(25)
k.push(32)
print(k.isempty())
k.printstack()
