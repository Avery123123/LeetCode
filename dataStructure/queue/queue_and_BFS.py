 class Queue(object):
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return self.data == []

    def enQueue(self,newElwm):
        self.data.append(newElwm)

    def deQueue(self):
        if self.isEmpty():
            raise Exception("Ypur Queue is Empty!")
        else:
            return self.data.pop(0)

    def gethead(self):
        if self.isEmpty():
            raise Exception("Your Queue is Empty!")
        else:
            return self.data[0]

    def getTail(self):
        if self.isEmpty():
            raise Exception("Your Queue is Empty!")
        else:
            return self.data[len(self.data)-1]

    def size(self):
        return len(self.data)

def bfs(adj,start):
    visited = set()
    q = Queue()
    q.enQueue(start) # 起始点入队
    while q.isEmpty() != True:
        u = q.deQueue()
        print(u)
        for v in adj.get(u,[]):
            if v not in visited:
                visited.add(v)
                q.enQueue(v)



if __name__ == "__main__":
    graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}

    bfs(graph, 1)



