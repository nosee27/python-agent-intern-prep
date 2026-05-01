"""
LeetCode  3. 无重复字符的最长子串
链接: https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
日期: 2026-04-30
"""
from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}    
        left = 0             
        max_len = 0                
        for right, char in enumerate(s):
            # 如果字符在窗口内出现过，移动左指针
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            # 更新字符位置
            char_index[char] = right 
            # 更新最大长度
            max_len = max(max_len, right - left + 1)
        return max_len