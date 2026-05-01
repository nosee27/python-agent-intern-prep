"""
LeetCode 26. 删除有序数组中的重复项
链接: https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
日期: 2026-04-27
"""
#双指针快慢法 O(n)
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow=0
        for fast in range(1,len(nums)):
            if nums[slow] !=nums[fast]:
                slow+=1
                nums[slow]=nums[fast]

        return slow+1