"""
LeetCode 053. 最大子数组合
链接: https://leetcode.cn/problems/maximum-subarray/description/
日期: 2026-05-12
"""
#动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current=max_sum=nums[0]
        for n in nums[1:]:
            current=max(n,current+n)
            max_sum=max(current,max_sum)
        return max_sum