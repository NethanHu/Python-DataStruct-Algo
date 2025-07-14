# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # 先获取到最尾部的节点（新链表的头节点）
        new_head = self.reverseList(head.next)
        # new_head 只是找到最后，返回的新头节点，和下方逻辑没关系

        # 下方的逻辑是：当程序栈运行到当前head的时候，改变顺序，
        # 然后返回到前一层程序栈
        # 到栈顶开始依次处理反向操作
        head.next.next = head
        # 注意，自己指向谁不重要，重要的是要让后一个节点指向自己
        head.next = None

        return new_head
