  stack = []
        output = [0 for i in range(len(T))]
 
        for index, value in enumerate(T):
            # 空栈，直接把元素放入
            if len(stack) == 0:
                stack.append((index, value))
            else:
                # 扫描元素小于栈顶元素，入栈
                if value < stack[-1][1]:
                    stack.append((index, value))
                # 扫描元素大于栈顶元素，弹出栈顶元素并记录索引差值。
                # 之后再判断与新的栈顶元素大小关系
                else:
                    while (len(stack) > 0) and (value > stack[-1][1]):
                        index_pop, value_pop = stack.pop()
                        output[index_pop] = index - index_pop
                        #######
                    stack.append((index, value))
 
        return output


