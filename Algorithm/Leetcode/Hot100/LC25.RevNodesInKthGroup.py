from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
解题思路：拓展两两交换到K个交换，注重边界值范围
1. 根据灵神的思路进行实现，关键在于链表长度未知，而不一定能整除K，所以要提前确定好反转几组节点（那么每一组里面就不需要考虑边界情况，因为肯定是有K个元素了）；
2. 在每一组K长度链表中，我们就按照LC92.反转链表II的思路来进行反转，我们此时使用迭代法:
    * 首先反转K个元素内部的指针，通过nxt和cur的反转来进行，在反转结束以后，cur实际上已经在K个元素链表的后继节点上了（K个元素之后）；
    * 然后我们考虑K个元素的前后继情况。p0扮演K个元素的前继节点，cur扮演K个元素的后继节点；我们让nxt作为辅助节点，
        - 首先是让p0的下一个元素（原链表中的第一个元素，反转之后的新链表中的最后一个元素）指向后继节点cur；
        - 然后让p0自身指向新链表中的第一个元素（也就是原链表中第K个元素）；
        - 最后让p0归位，成为新链表的哑节点（也就是上一个链表的最后的节点）。
"""

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy: ListNode = ListNode(next=head)
        n: int = 0
        cur: Optional[ListNode] = head
        # 先计算链表的长度
        while cur:
            n += 1
            cur = cur.next

        p0: ListNode = dummy
        # 首先初始化pre为None
        pre: Optional[ListNode] = None
        cur = head
        # 对每组满足长度符合K个元素的链表，我们进行反转操作
        while n >= k:
            n -= k
            for _ in range(k):
                # 提前获取到nxt节点，以防之后获取不到了；然后断开cur指向nxt的指针，让其指向pre前继节点
                nxt: Optional[ListNode] = cur.next
                cur.next = pre
                # 移动pre、nxt指针各一格，用来进行下一步交换
                pre = cur
                cur = nxt

            # 我们让nxt指针继续做脏活累活，现在跑到前面来，用来重新安排K个节点前后继节点的顺序
            nxt = p0.next
            # 开始重组前后继节点
            nxt.next = cur
            p0.next = pre
            # 最后让p0重新做回新链表的哑节点
            p0 = nxt

        return dummy.next
