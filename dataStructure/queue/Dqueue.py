class DQueue(object):
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return self.data == []

    def insertHead(self,newElem):
        self.data.insert(0,newElem)

    def insertTail(self,newElem):
        self.data.append(newElem)

    def deleteHead(self):
        if self.isEmpty():
            raise Exception("Your Dqueue is empty!")
        else:
            return self.data.pop(0)

    def deleteTail(self):
        if self.isEmpty():
            raise Exception("Ypur DQueue is empty!")
        else:
            return self.data.pop()

    def getHead(self):
        if self.isEmpty():
            raise Exception("Your DQueue is empty!")
        else:
            return self.data[0]

    def getTail(self):
        if self.isEmpty():
            raise Exception("Your DQueue is empty!")
        else:
            return self.data[len(self.data)-1]

    def size(self):
        return len(self.data)

