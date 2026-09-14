# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #res = 0
        def findDepth(root):
            #res = 0
            if root == None:
                return 0
            #else:
             #findDepth(root.right)
            #findDepth(root.left)
                #res = res + 1
            return 1 +  max(findDepth(root.right), findDepth(root.left))
        return findDepth(root)