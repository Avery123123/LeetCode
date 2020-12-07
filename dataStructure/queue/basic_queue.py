class Queue(object):
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return self.data == []

    def insert(self,newElem):
        self.data.append(newElem)

    def delete(self):
        if self.isEmpty():
            raise Exception("Your queue is Empty!")

        else:
            return self.data.pop()

    def head(self):
        return self.data[0]

    def tail(self):
        return self.data[len(self.data)-1]

    def size(self):
        return len(self.data)

