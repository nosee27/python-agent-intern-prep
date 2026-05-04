"""
LeetCode 019.删除链表的倒数第 N 个结点
链接: https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/
日期: 2026-05-05
"""
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(-1,head)
        slow=dummy
        fast=dummy
        for _ in range(n):
            fast=fast.next
        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return dummy.next