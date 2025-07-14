# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverseNumbers(l1)
        l2 = self.reverseNumbers(l2)
        rev_ans = self.addTwoRevNumbers(l1, l2)
        return self.reverseNumbers(rev_ans)

    def reverseNumbers(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head: ListNode = self.reverseNumbers(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def addTwoRevNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head: ListNode = ListNode(0)
        cur_node: ListNode = head
        carry: int = 0
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry
            carry = total // 10
            digit = total % 10
            cur_node.next = ListNode(digit)
            cur_node = cur_node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head.next