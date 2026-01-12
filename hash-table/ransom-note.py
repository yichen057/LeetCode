# 解题的思路是利用一个哈希表或者说一个长度为 26 的数组，因为只有小写字母 a 到 z 共 26 个。
# 我们先统计 magazine 中每个字符出现的次数，然后再统计 ransom 中每个字符需要的次数。
# 最后比较 ransom 中每个字符的需求量是否都能被 magazine 中对应的字符数覆盖。
# 如果 magazine 中的某个字符不够用，那么返回 false；如果全部满足，则返回 true。
# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = [0] * 26
        magazine_count = [0] * 26
        for c in ransomNote:
            ransom_count[ord(c) - ord('a')] += 1
            # ord(c)：Python 的函数，用来获取字符 c 的 ASCII 码（整数）
        for c in magazine:
            magazine_count[ord(c) - ord('a')] += 1
        for i in range(26): # 让变量 i 依次取值 0, 1, 2, ..., 25。
            if ransom_count[i] > magazine_count[i]:
                return False
        return True
            
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here

if __name__ == '__main__':
    solution = Solution()

    # Quick prints
    print(solution.canConstruct("a", "b"))    # False
    print(solution.canConstruct("aa", "ab"))  # False
    print(solution.canConstruct("aa", "aab")) # True

    # Or assertions
    assert solution.canConstruct("a", "b") is False
    assert solution.canConstruct("aa", "ab") is False
    assert solution.canConstruct("aa", "aab") is True      