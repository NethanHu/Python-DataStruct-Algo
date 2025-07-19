from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。链表长度未知。
解题思路：双指针
1. 根据灵神的思路，我们要删除倒数第n个元素，那必然要找第n+1个元素（n-th元素不重要），因为我们可以直接删除：e(n+1).next = e(n+1).next.next；
2. 我们构造一对双指针，间隔为（n+1），此时我们不断移动右边界一直到末尾，那么有边界在末尾的时候，左边界恰好就是倒数第（n+1）个元素；
3. 为了防止出现n==链表长度（即删除的为第一个元素），为了一劳永逸，我们在head之前设定一个哨兵节点dummy，这样「所有的删除操作都只发生在dummy元素之后」；
4. 使用 while right.next 而不是 while right 的原因：如果使用while right会使得right最后停在原数组的最后一个元素的下一个位置（指向None），
    但是如果选择的left在left前一个元素就可以规避这个问题。纯看个人构造的时候的想法。
"""


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 设定一个dummy节点，dummy的下一个元素指向head。那么最后返回的节点肯定是dummy.next
        dummy: ListNode = ListNode(next=head)
        # 双指针一开始都在dummy的位置上
        left = right = dummy
        # 右指针要保证比左指针多n才可以。好处是由于一开始初始化的时候在dummy这个额外的节点上，因此right遍历到结尾的时候，left就刚好指向的是
        # 倒数第n个元素的前一个元素（可以画图感受一下）
        for _ in range(n):
            right = right.next
        # 双指针（这把长度固定的尺子）的right遍历到结尾，那么left恰好指向pre这个节点
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
