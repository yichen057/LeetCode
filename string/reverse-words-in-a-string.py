class Solution:
    # 方法一: 时间复杂度 O(n)：整体反转 O(n)，再用快慢双指针扫描并反转每个单词，总体仍是线性。空间复杂度 O(n)：把字符串转成列表 s = list(s)，还有 result 存结果，都是线性额外空间。
    def reverseWords(self, s: str) -> str:
        s = list(s)
        # Step 1: 对已知string做整体翻转
        s.reverse() # list的反转, 此时： "the sky" -> "yks eht"
# list 有 .reverse() 方法，会就地反转。
# str 没有 .reverse() 方法，所以字符串不能直接调用。如果是字符串，要么用切片 s[::-1]，要么先转成 list 再 reverse()

        # Step 2: 使用快慢指针, 对单词间加空格 
        result = [] # 这里的result是list列表
        fast = 0

        while fast < len(s): # 外层 while fast < len(s) 只保证“开始这一轮”时 fast 没越界
            # 当fast指针指向的非空元素, 确认当前位置不是空格, 只判断了当前一个字符
            if s[fast] != " ":
                if result: # 如果result列表不为空，说明不是第一个单词，需要先加一个空格
                    result.append(" ")

                # 此时result列表为空, 说明是第一个单词, 直接记录单词到result
                start = fast # 记录单词开始的位置
# 内层 while的二次判断, 是用来“走完整个单词”，fast不断递增一直推进到单词末尾（空格或结尾）。所以不是重复判断：外层判断进入单词，内层负责吃完整个单词。
# 内层 while 会不断递增 fast，中途可能到达末尾，所以内层也必须检查 fast < len(s) 才安全访问 s[fast]
                while fast<len(s) and s[fast] != " ": # 内层 while 已经把 fast 向右移动，直到遇到空格或字符串末尾为止。
                    fast += 1

                # step 3: 切片取出字符串里的每个单词, 并在单词内部进行翻转, 变成正常顺序的单词
                #str 和 list 都支持切片语法 s[start:fast]，返回同类型的新对象：对 str 切片得到的是新的 str; 对 list 切片得到的是新的 list
                # 这一步很关键：
                # 因为s整体反转了，单词内部也是反的('yks')。
                # 我们切片取出这个单词，再反转一次变回('sky')，然后加入result
# 在进入这行之前，内层 while 已经把 fast 向右移动，直到遇到空格或字符串末尾为止。也就是说此时 fast 指向的是“单词后面的第一个位置”（空格或末尾），而切片 s[start:fast] 是左闭右开，正好取到完整单词。
                word = s[start:fast] # word是一个字符列表, 左闭右开区间
                word.reverse() # 单词内部反转
                result.extend(word) # 使用 extend 批量加入字符  
                # extend(word) 会把里面的每个字符逐个加入 result。
                # append(word) 会把整个列表当成一个元素塞进去，变成嵌套列表，最后 ''.join(result) 会报错。
                # 示例：
                # result = ['a']; word = ['b','c']
                # extend → ['a','b','c']
                # append → ['a',['b','c']] 
            # 当fast指针指向的空格, fast+1跳过
            else:
                fast += 1

        return "".join(result) # 最后统一拼接返回字符串
        