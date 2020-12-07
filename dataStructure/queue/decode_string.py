class Stack(object):
    def __init__(self):
        self.data =[]

    def isEmpty(self):
        return self.data == []


    def push(self,newElem):
        self.data.append(newElem)

    def pop(self):
        if self.isEmpty():
            raise Exception("Your Stack is Empty！")
        else:
            return self.data.pop()

    def size(self):
        return len(self.data)


class Solution(object):
    def decodeString(self,s):
        stack = Stack()

        curNum = 0
        curString = ''

        for c in s:
            if c == '[':
                stack.push(curString)
                stack.push(curNum)
                curNum = 0
                curString = ''
            elif c == ']':
                num = stack.pop()
                preString = stack.pop()
                curString = preString + num * curString

            elif c.isdigit():
                curNum = curNum * 10 +int(c)

            else:
                curString += c

        return curString


if __name__ == "__main__":
    solu =Solution()
    s = "3[a]2[bc]"
    print(solu.decodeString(s))

