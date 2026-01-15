class MyQueue:

    def __init__(self):
        """
        in 主要负责push, out 主要负责pop
        stack_in（输入栈）：只负责接收新来的元素。相当于“队尾”。
        stack_out（输出栈）：只负责提供要出去的元素。相当于“队头”。
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        """
        有新元素进来，就往in里面push
        """
        self.stack_in.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty(): # self.empty() 是判断整个队列是否为空，所以应同时判断 stack_in 和 stack_out 两个栈都为空
            return None
        
        if self.stack_out:
            return self.stack_out.pop()
        # pop() 是 Python list 的方法，常用来当栈的 “弹出栈顶”。
        # 还能用这些数据结构当栈：
        # collections.deque：也有 append / pop，更适合频繁从两端操作
        # 自己封装的栈类（内部用 list 或 deque）
        # queue.LifoQueue：线程安全的栈（一般刷题不用）
        # 总结：LeetCode 里最常见就是 list 或 deque
        else: # stack_out is empty
            # 两种循环方式均可, 都是 O(n) 次 pop/append。Python 层面一般更推荐 while self.stack_in:，代码更直观，也不会反复计算 len 的范围。
            # for i in range(len(self.stack_in)):
            #     self.stack_out.append(self.stack_in.pop())
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
        
    def peek(self) -> int: # peek的目的是看一眼, 然后假装没动过
        """
        Get the front element.查询数值
        """
        result = self.pop() # 直接使用已有的pop函数, pop函数最终是从stack_out出去的元素
        self.stack_out.append(result) # 秉着queue"先进先出"的顺序不被打乱, 从哪里拿出来的，就必须放回哪里去。
        return result

    def empty(self) -> bool:
        """
        只要in或者out有元素，说明队列不为空
        """
        return not (self.stack_in or self.stack_out)
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()