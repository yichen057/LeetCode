class MyStack:

    def __init__(self):
        self.que = deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        if self.empty(): # 复用本题里写好的empty()方法
            return None
        for _ in range(len(self.que)-1): # 弹出size-1个元素, 使得想要pop的元素从队尾到队首
            self.que.append(self.que.popleft()) # 弹出的元素再重新加回到队列里
        return self.que.popleft() # 只有deque(双端队列)有popleft()这个方法; queue 用的是 get(); 
    # list/stack用pop()移除并返回最后一个元素; dictionary用pop(key)=value, 移除并返回指定key的value;set用pop()随机返回一个元素, 因为集合是无序的;
    # deque用pop()移除最右边一个(尾部)
    
    def top(self) -> int:
        # 写法一: 
        # if self.empty():
        #     return None
        # return self.que[-1] # 将que尾部的元素先弹出
        # 写法二: 
        if self.empty():
            return None
        result = self.pop() # 复用 pop() 获取栈顶元素 (此时一定能取到值)
        # 理解变量和容器的关系: 当你执行 temp = self.que.popleft() 时，temp 这个变量就“抓住了”那个元素。 无论你之后拿这个元素去做了什么（比如把它放回队列、打印它、还是用它做计算），只要你没有把 temp 变量本身覆盖掉（比如写 temp = 0），它手里的那个东西就一直都在。
        self.que.append(result) # 将取出的元素重新添加回队列末尾（恢复原状）

        return result
        # # 写法三：
        # if self.empty():
        #     return None
        # for i in range(len(self.que)-1):
        #     self.que.append(self.que.popleft())
        # temp = self.que.popleft()
        # self.que.append(temp)
        # return temp

    def empty(self) -> bool:
        return not self.que
        
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()