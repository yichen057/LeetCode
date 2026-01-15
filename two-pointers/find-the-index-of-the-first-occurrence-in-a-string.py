class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
         # 方法一: 切片法
        # n, m =len(haystack), len(needle)
        # # 只需要遍历到 n - m 的位置即可，后面剩下的长度不够 needle 长了. 
        # 循环变量 i 代表的是子串的“起始位置”，我们需要保证从这个位置开始往后数，剩余的长度还够放得下整个 needle
        # for i in range(n - m + 1):
        #     # 截取子串进行比较. Python 的切片语法 [start : end] 确实是 左闭右开 的
        # 保证子串needle的长度是(i + m) - i = m
        # 虽然这里用了切片 haystack[i : i + m]，其底层也是字符逐个比较，时间复杂度总体接近 $O(N \times M)$)
        #     if haystack[i: i + m] == needle:
        #         return i
        # return -1
        # 方法二: 纯循环方法
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            # 将needle的元素逐个与haystack的字符对比
            index_needle = 0
            index_haystack = i
            while index_needle < m and haystack[index_haystack] == needle[index_needle]:
                index_haystack += 1
                index_needle += 1
            
            # 如果index_needle走到了末尾, 说明完全匹配
            if index_needle == m:
                return i
            
        return -1