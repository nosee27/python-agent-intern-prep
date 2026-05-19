"""
LeetCode 112.路径总和
链接: https://leetcode.cn/problems/path-sum/description/
日期: 2026-05-19
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root==targetSum
        return self.hashPathSum(root.right,targetSum-root.val) or self.hashPathSum(root.left,targetSum-root.val)