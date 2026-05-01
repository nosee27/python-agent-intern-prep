"""
LeetCode 283. 移动零
链接: https://leetcode.cn/problems/move-zeroes/description/
日期: 2026-04-28
"""
#快慢指针法
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow=0
        for fast in range(0,len(nums)):
            if nums[fast]!=0:
                nums[slow]=nums[fast]
                slow+=1

        for i in range(slow,len(nums)):
            nums[i]=0
     
#快慢指针交换法
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow=0
        for fast in range(0,len(nums)):
            if nums[fast] !=0:
                nums[slow],nums[fast]=nums[fast],nums[slow]
                slow+=1