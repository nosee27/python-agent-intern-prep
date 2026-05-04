"""
LeetCode 021.合并两个有序列表
链接: https://leetcode.cn/problems/merge-two-sorted-lists/
日期: 2026-05-04
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list=ListNode(0)
        current=new_list
        while list1 and list2:
            if list1.val<=list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            current=current.next
        current.next=list2 if list2 else list1

        return new_list.next
