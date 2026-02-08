# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        
        # queue = collections.deque([root])
        # depth = 0 # 代表二叉树的层数
        
        # while queue:# 代表queue存在, 因此此时depth不可能为0
        #     depth += 1 # 
        #     for _ in range(len(queue)): # 取每层的元素, len(queue)代表每层的元素个数
        #         cur = queue.popleft()

        #         if cur.left:
        #             queue.append(cur.left)
        #         if cur.right:
        #             queue.append(cur.right)

        # return depth
    # 方法二: 后续遍历的递归法求高度, 即最大深度
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: #不必判断两遍，只保留 getDepth 里的 if not node: return 0 就够；若你更喜欢在入口显式处理空树，两处都写也可以。
            return 0
        
        return self.getDepth(root)
    # 递归三步法: 1. 确定递归函数的参数和返回值 2. 确定终止条件 3. 确定单层递归的逻辑
    def getDepth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        # 后序递归遍历求高度(即最大深度): 左右中, 先求左右子树的深度, 然后加上当前节点的深度
        leftDepth = self.getDepth(node.left) # 左
        rightDepth = self.getDepth(node.right) # 右
        height = 1+ max(leftDepth, rightDepth) # 中, 中在左和右的上面一层, 所以加1, 代表从下往上的处理逻辑
        return height