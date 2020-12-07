    def __init__(self):
        self.dataStack = Stack()
        self.minStack = Stack()

    def isEmpty(self):
        return self.dataStack.data == []

    def push(self,newElem):
        self.dataStack.push(newElem)

        if self.minStack.isEmpty():
            self.minStack.push(newElem)

        elif newElem <= self.minStack.top():
            self.minStack.push(newElem)

    def pop(self):
        value = self.dataStack.pop()

        if value == self.minStack.top():
            self.minStack.pop()

        return value

    def top(self):
        return self.dataStack.top()

    def size(self):
        return self.dataStack.size()

    def getMin(self):
        return self.minStack.top()

