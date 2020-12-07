class Stack(object):
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return self.data == []

    def push(self,newElem):
        self.data.append(newElem)

    def pop(self):
        if self.isEmpty():
            raise Exception("Your stack is Empty!")
        else:
            self.data.pop()

    def top(self):
        return self.data[len(self.data)-1]

    def size(self):
        return len(self.data)


class Solution(object):

    def isValid(self,s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()

        item ={'(':')','[':']','{':'}'}

        if len(s) % 2 != 0:
            return False
        for i in s:
            if i in item.keys():
                stack.push(i)
            elif i in item.values() and stack.isEmpty():
                return False

            elif i in item.values() and i == item[stack.top()]:
                stack.pop()

        return stack.isEmpty()



