"""
LeetCode 128.最长连续序列
链接: https://leetcode.cn/problems/longest-consecutive-sequence/description/
日期: 2026-05-10
"""
#哈希表法
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        longest=0
        for x in s:
            if x-1 not in s:
                current=x
                current_len=1
                while current+1 in s:
                    current+=1
                    current_len+=1
                longest=max(longest,current_len)
        return longest