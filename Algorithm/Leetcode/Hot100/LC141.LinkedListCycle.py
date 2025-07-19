"""
给你一个链表的头节点 head ，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接
到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
如果链表中存在环 ，则返回 true 。 否则，返回 false 。
解题思路：快慢指针
1. 我们使用一对快慢指针来遍历这个链表。想象一下，如果链表没有环，那么快指针必然更早到达链表尾端；而到达了链表尾端，必然代表无环存在；
2. 如果有环，那么两个指针会在环中不断循环，而快慢指针的速度相差1，说明每次循环两者距离都会减少1（在环中快指针追慢指针，追到的时候相当于套圈）；
3. 而距离每次减少1能保证在环中两者注定会相遇，如果相遇就说明有环了（快指针都套圈了）。
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
