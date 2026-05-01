<<<<<<< HEAD
"""
LeetCode 1. 两数之和
链接: https://leetcode.cn/problems/two-sum/
日期: 2026-04-26
"""

from typing import List

# 解法1: 暴力枚举 O(n²)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# 解法2: 哈希表 O(n)
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in new_dict:
                return [new_dict[need], i]
            new_dict[num] = i
        return []
=======
"""
LeetCode 1. 两数之和
链接: https://leetcode.cn/problems/two-sum/
日期: 2026-04-26
"""

from typing import List

# 解法1: 暴力枚举 O(n²)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# 解法2: 哈希表 O(n)
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in new_dict:
                return [new_dict[need], i]
            new_dict[num] = i
        return []
>>>>>>> 276dd67 (day03: 闭包+双指针(26.删除重复项))
