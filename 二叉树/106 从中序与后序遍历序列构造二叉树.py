# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(iOrder, pOrder):
            if not pOrder: return None
            root = TreeNode(pOrder[-1])
            rootInx = iOrder.index(root.val)

            root.left = helper(iOrder[0:rootInx], pOrder[0:rootInx])
            root.right = helper(iOrder[rootInx + 1:], pOrder[rootInx:-1])
            return root

        return helper(inorder, postorder)