# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        if root is None:
            return []
        t = type(root)			                        # 保存树的类型
        out = []				                        # 初始化输出数组
        stack = [root]			                        # 将树压入栈中
        while stack:			                        # 循环栈
            root = stack.pop()	                                # 根节点等于出栈的节点
            if type(root) != t and root is not None:	        # 如果此时root不为树并且不为空
                out.append(root)				        # 将这个数加入输出数组中
                continue						# 结束本次循环
            if root:      						# 如果此时root是树
                stack.append(root.right)				# 将右孩子压入栈
                stack.append(root.left)				# 将左孩子压入栈
                stack.append(root.val)				# 将根的值压入栈
        return out