from typing import Optional

"""
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false。
解题思路：快慢指针找中间节点，反转链表比对
* 快慢指针：如果链表有奇数个节点，那么找的是正中间的节点；如果链表有偶数个节点，那么找的是正中间右边的节点。
1. 先通过快慢指针找到mid这个节点；
2. 反转从 mid 到链表末尾的这段，获得新的节点叫做new_head，然后同时遍历head和new_head：
3. 每次循环判断 head.val 是否等于 new_head.val，若不相等，则返回 false。
相比于直接deepcopy一个head，整个reverse之后遍历比较，使用中间节点再reverse可以省下很多空间：
7638ms + 286.8MB -> 80ms + 39.9MB 提升明显，因为没有开辟新内存，也不需要遍历两遍
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid: Optional[ListNode] = self.getMiddleNode(head)
        new_head: Optional[ListNode] = self.getReversedList(mid)
        # 此处不用while head: 的原因是，反转之后的new_head必然更短，使用head来做条件会报错
        while new_head:
            if head.val != new_head.val:
                return False
            head = head.next
            new_head = new_head.next
        return True


    def getMiddleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast: Optional[ListNode] = head
        slow: Optional[ListNode] = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


    def getReversedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head: Optional[ListNode] = self.getReversedList(head.next)
        head.next.next = head
        head.next = None
        return new_head
