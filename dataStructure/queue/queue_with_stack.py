class Stack(object):
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return self.data ==[]

    def push(self,newElem):
        self.data.append(newElem)


    def pop(self):
        if self.isEmpty():
            raise Exception("Your Stack is Empty!")

        else:
            return self.data.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("Your Stack is Empty!")

        else:
            return self.data[-1]

    def size(self):
        return len(self.data)


class MyQueue(object):
    def __init__(self):
        self.pushStack = Stack()
        self.popStack = Stack()

    def isEmpty(self):
        if self.pushStack.isEmpty() and self.popStack.isEmpty():
            return True
        else:
            return False

    def push(self,newElem):
        self.pushStack.push(newElem)

    def pop(self):
        while(self.pushStack.isEmpty() != True):
            self.popStack.push(self.pushStack.pop())

        return self.popStack.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("Your Queue is Empty!")
        else:
            while (self.pushStack.isEmpty() != True):
                self.popStack.push(self.pushStack.pop())

            return self.popStack.peek()



if __name__ == "__main__":

    mq = MyQueue()

    mq.push(1)
    mq.push(2)
    mq.push(3)
    mq.push(4)
    print(mq.pop())
    print(mq.peek())



