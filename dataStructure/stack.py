class Stack(object):
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return self.data == []

    def push(self,newElem):
        self.data.append(newElem)

    def pop(self):
        if self.isEmpty():
            raise Exception("Your Stack is Empty!")

        else:
            return self.data.pop()

    def top(self):
        if self.isEmpty():
            raise Exception("Your stack is Empty!")
        else:
            return self.data[len(self.data)-1]

    def size(self):
        return len(self.data)

