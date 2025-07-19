from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到
链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
不允许修改链表。
解题思路：快慢指针+数值求解
我们和LC141思路一样，如果fast、slow指针可以相遇，说明此时是有环的，我们更进一步要求环入口位置。
1. 我们假设这个链表前a个节点在环之外，b个节点在环之内；第一次相遇的时候slow指针走了s步，fast指针走了f步：
    * 由于速度关系，我们可以得出 f = 2s；
    * 我们继续假设快指针追上慢指针的时候套了n圈，那么 f = s + nb（由于环的独特循环性质）；
    * 得到关系 s = nb，那么说明相遇的时候，slow指针走的步数其实就是环长度的整数倍。
2. 从head开始走到「入环节点」的时候需要走几步呢？由于循环关系，根据我们的假设需要走 a 步或者 a + nb 步；
    * 而我们知道，第一次相遇的时候慢节点已经走了 s = nb 步，那么如果我们知道 a 的数量的话，slow指针再走 a 步（a + nb）就可以到「入环节点」；
    * 此时我们可以发现，slow 节点距离「入环节点」还有 a 步；如果我们假设一个new_slow节点从head开始一步一步走，走到「入环节点」也需要 a 步；
    * 那么slow继续走，和new_slow相遇的地方必然是「入环节点」！
3. 稍微修改了灵神的答案，因为不允许修改链表，我设了一个new_slow去遍历，最后相遇的时候返回new_slow即可。
"""


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast: Optional[ListNode] = head
        slow: Optional[ListNode] = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # 如果我们发现存在环的话，就开始找「入环节点」
            if fast is slow:
                new_slow: Optional[ListNode] = head
                while new_slow is not slow:
                    slow = slow.next
                    new_slow = new_slow.next
                return new_slow
        return None
