# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional

"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head: ListNode = ListNode(0)
        cur_node: ListNode = head
        carry: int = 0
        while l1 or l2 or carry:
            x: int = l1.val if l1 else 0
            y: int = l2.val if l2 else 0
            cur_sum: int = x + y + carry
            # 接下去就是十进制的常规进位操作
            carry = cur_sum // 10
            cur_sum = cur_sum % 10
            cur_node.next = ListNode(cur_sum)
            cur_node = cur_node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head.next
