"""
LeetCode 049.字母异位词分组
链接: https://leetcode.cn/problems/group-anagrams/description/
日期: 2026-05-09
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for s in strs:
            t=''.join(sorted(s))
            if t in d:
                d[t].append(s)
            else:
                d[t]=[s]
        return list(d.values())