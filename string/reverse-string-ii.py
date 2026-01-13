class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # 方法一: 切片反转
        # res = list(s) # str 在python里是不可变的, 所以必须转为可变的列表list, 才能对里面的字符进行修改和交换
        # for i in range(0, len(res), 2*k): # 使用range(start, stop, step) 函数来确定需要调换的初始位置。i的值从索引0开始, 循环到列表末尾结束, 每一次循环, i=0, 2k, 4k,...
        #     res[i: i+k] = res[i:i+k][::-1] # 反转前k个字符后, 更改原值为反转后值. 用切片整体替换, 而不是一个个替换
# res[i:i+k]：取出从位置 i 开始的 k 个字符
# 例如：i=0, k=2 → res[0:2] = ['a', 'b']
# [::-1]：反转切片（Python 反转语法）
# ['a', 'b'][::-1] = ['b', 'a']
# 赋值回原位置：整体替换（不需要逐个交换）
        
        # 方法二: reverse自主实现(two pointer approach)
        def reverse_substring(text: List[str]) -> List[str]:
            left, right = 0, len(text)-1
            while left < right:
                text[left], text[right] = text[right], text[left]
                left += 1
                right -= 1
            return text
        
        res = list(s)
        for i in range(0, len(s), 2*k):
            res[i: i+k] = reverse_substring(res[i: i+k])

        return ''.join(res) # 将 list 转回 str. 用空字符串 '' 作为连接符，将列表 res 中的所有字符连接起来。eg: ['a', 'b', 'c'] -> 'abc'