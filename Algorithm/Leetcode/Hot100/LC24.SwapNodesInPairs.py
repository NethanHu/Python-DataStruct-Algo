from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
思路：没什么特别的思路，只要不要把自己绕进去就行
1. 为了方便，我们设定四个节点：node0是待交换的两个节点的前继节点；node3是待交换的两个节点的后继节点；node1、node2是待交换节点的前后两者。
2. 设定哑节点dummy指向head，最后返回dummy.next
3. 交换的逻辑如下：
    * 必须有两个节点即以上才能while循环，所以必须存在node1和node1.next，node0指向待交换的前继节点，node1指向待交换的第一个节点；
    * node2设为node1的下一个（待交换的第二个节点），node3就是node1、node2的后继节点（可以为None，所以不能使用node3.next）；
    * 0 -> 1 -> 2 -> 3 交换顺序为： 0 -> 2、2 -> 1、1 -> 3；
    * 然后node1此时变成了指向下一对待交换节点的前继，因此node0=node1；node3变成了待交换节点的第一个，因此node0=node3。
"""


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy: ListNode = ListNode(next=head)
        node0: ListNode = dummy
        node1: Optional[ListNode] = head
        # 至少得有两个节点才能进行交换，否则不交换
        while node1 and node1.next:
            # 把当事方全部拉进来
            node2 = node1.next
            node3 = node2.next
            # 以下是交换的逻辑
            # 0 -> 1 -> 2 -> 3 变成 0 -> 2
            node0.next = node2
            # 2 -> 1
            node2.next = node1
            # 1 -> 3
            node1.next = node3
            # 然后准备下一轮交换，移动指针
            node0 = node1
            node1 = node3
        return dummy.next
