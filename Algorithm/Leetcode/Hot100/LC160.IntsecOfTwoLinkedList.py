"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
解题思路：从不等长中寻找等长
1. 假设链表A长度为a，链表B长度为b，两者最后的公共部分长度为c，那么：
    * 从headA出发遍历到公共起点，一共会走(a-c)步
    * 从headB出发遍历到公共起点，一共会走(b-c)步
2. 我们可以巧妙的加上这一个关系：
    * 我们让一个 node A 从 headA 出发，到达A的尾端之后，再从 headB 开始走，一路到公共节点，那么会走 a + (b - c) 步
    * 我们让一个 node B 从 headB 出发，到达B的尾端之后，再从 headA 开始走，一路到公共节点，那么会走 b + (a - c) 步
    * 我们可以发现 a + (b - c) = b + (a - c)，且双方最后都会在公共节点相遇
3. 循环终止条件是 A == B，在此之前都是 A != B，我们考虑两者情况：
    * 如果 A == B == null 的时候，说明两个node都遍历完自己之后又把对面也遍历了，最后都到了null，说明两者没有相交的位置
    * 如果 A == B != null 的时候，说明两个node在某个点开始有公共部分，就把公共部分开始的那个节点返回即可
其中，while A is not B: 这句代码，使用的是 is 运算符。它是在判断指针 A 和指针 B 是否指向了内存中同一个节点对象。
能保证一定返回的是同个节点，而不会是「恰好」val、next都相等的不同节点。
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A: ListNode = headA
        B: ListNode = headB
        while A is not B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
