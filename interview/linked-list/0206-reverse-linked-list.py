"""
LeetCode 206.反转列表
链接: https://leetcode.cn/problems/reverse-linked-list/description/
日期: 2026-05-01
"""
#迭代法双指针
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        while curr:
            new=curr.next
            curr.next=prev
            prev=curr
            curr=new
        return prev
        