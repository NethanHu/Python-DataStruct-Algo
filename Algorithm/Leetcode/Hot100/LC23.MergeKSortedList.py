from heapq import heapify, heappop, heappush
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。
思路分析：自己想的是暴力解法（能通过，把问题分解成两两 merge）；灵神的思路是最小堆
1. 我们理一下思路，想想直观的解题思路是什么：
    * 如果可以有一个数据结构，能存下每个 Lis t的头节点，然后这个数据结构会循环地取出这些头节点中的最小值，掐了头之后剩下的元素继续放回这个数据结构中；
    * 然后我们把这个最小的头节点拿来连接到有序的 dummy 之后；
    * 综合以上考虑，我们需要使用的是最小堆 min_heap（本质上就是优先队列）。
2. 做法如下：
    * 我们先准备一个列表，里面存的是每个 lists 中元素的头节点（头节点中包含着next，可以从这个元素找到下一个元素在哪里）；
    * 直接对 min_heap 这个列表使用 heapq 的 heapify 方法，直接可以构造最小堆；
    * 每次 heappop 的时候，相当于就从最小堆中 pop 出最小的那个元素（ListNode 怎么比较大小呢？就定义魔法方法__lt__）；
    * 把最小的元素挂在我们的答案链表的后面，然后判断一下这个元素next存不存在，如果存在就把掐了头的部分重新入堆进行排序。
3. 注意点：
    * heapify(args)、heappop()、heappush() 都是直接使用即可，不是对象方法。
    * 更多使用方式参考：https://docs.python.org/zh-cn/3.11/library/heapq.html
"""

ListNode.__lt__ = lambda a, b: a.val < b.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 这个函数类似于Java里面的Comparable接口的方法，是为了比较两个ListNode谁大谁小
        dummy: ListNode = ListNode()
        cur: Optional[ListNode] = dummy
        min_heap: List[ListNode] = [head for head in lists if head]
        # 这个在LeetCode 的 Python3 中已经内置，刚刚的 __lt__ 就是为了实现堆化的前置条件（可比较）
        heapify(min_heap)

        while min_heap:
            node: Optional[ListNode] = heappop(min_heap)
            if node.next:
                heappush(min_heap, node.next)
            cur.next = node
            cur = cur.next

        return dummy.next

    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     # 排除 [] 和 [[]] 这两个特殊情况
    #     if not lists:
    #         return None
    #     if len(lists) == 1 and not lists[0]:
    #         return None
    #     dummy: ListNode = ListNode()
    #     dummy.next = lists.pop()
    #     while lists:
    #         dummy.next = self.merge2Lists(dummy.next, lists.pop())
    #     return dummy.next
    #
    #
    # def merge2Lists(
    #         self, head1: Optional[ListNode], head2: Optional[ListNode]
    # ) -> Optional[ListNode]:
    #     if not head1:
    #         return head2
    #     if not head2:
    #         return head1
    #     if head1.val < head2.val:
    #         head1.next = self.merge2Lists(head1.next, head2)
    #         return head1
    #     else:
    #         head2.next = self.merge2Lists(head1, head2.next)
    #         return head2
