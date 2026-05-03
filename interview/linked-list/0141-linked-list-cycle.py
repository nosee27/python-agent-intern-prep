"""
LeetCode 141.环形链表
链接: https://leetcode.cn/problems/linked-list-cycle/description/
日期: 2026-05-02
"""
#快慢指针法
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head  or not head.next:
            return False
        slow=head
        fast=head.next
        while slow!=fast:
            if not fast or not fast.next:
                return False
            slow=slow.next
            fast=fast.next.next
        return True
        