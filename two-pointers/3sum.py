class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # List[List[int]]: 表示“整数列表的列表”——即外层是一个列表，里面每个元素又是一个 List[int]（一个整数序列）。用来表示多个三元组/数组的集合很常见。
        result = []
        nums.sort() # 排序是关键

        for i in range(len(nums)):
            # 如果第一个元素已经>0, 不需要进一步检查
            if nums[i] > 0:
                return result
            
            # 获取第一个数, 并对第一个数去重
            # 如果当前数和上一个数一样，说明这个数的情况已经处理过了，跳过。
            # 比如 [-1, -1, 0, 1]，处理完第一个 -1 后，第二个 -1 就不用再处理了。
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # 初始化双指针
            left = i + 1
            right = len(nums) - 1

            # 获取第二和第三个数并去重
            # 外层是“做查找”的循环，内层是“去重并保证边界”的循环，两者职责不同，不能省
            while right > left: # 此处right不能>=left, 因为一旦二者相等, 两个指针指向同一个位置, 那b和c就是一个数, 就不符合triple三元数组了, 所以left!=right
                sum_ = nums[i] + nums[left] + nums[right]

                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    # 找到一个解后
                    result.append([nums[i], nums[left], nums[right]]) # 会将一个列表作为元素添加到 result 中, append() 方法只接受 一个参数。如果传三个参数，会抛出 TypeError

                    # 对第二和第三个数即对nums[left]和nums[right]去重
                    # 对右指针去重：
                    # 如果 right 左边的数跟当前 right 指向的数一样，就一直往左跳。
                    # right > left 必须在内层也判断，防止跳过重复时指针交错（越界/变成无效区间）
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1 # 立即跳过所有重复的 right 值

                    # 对左指针去重：
                    # 如果 left 右边的数跟当前 left 指向的数一样，就一直往右跳。
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1 # 立即跳过所有重复的 left 值
                    
                    # 找到答案并去重后，双指针同时收缩，准备找下一组
                    right -= 1
                    left += 1
                    # 去重是去除相同的三元组，不是去重数组本身。
        return result