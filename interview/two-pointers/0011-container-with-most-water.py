"""
LeetCode 11.盛最多水的容器
链接: https://leetcode.cn/problems/container-with-most-water/description/
日期: 2026-04-29
"""
#双指针
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right,res=0,len(height)-1,0
        while left<right:
            length=right-left
            width=min(height[left],height[right])
            res=max(res,length*width)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return res