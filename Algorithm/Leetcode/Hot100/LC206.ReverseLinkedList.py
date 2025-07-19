"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
此题目在Base50中也有记录，Base50中记录得更详细，参考那部分的注释。
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head: Optional[ListNode] = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
