from collections import defaultdict
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
解题思路：哈希+Python内置排序功能，LeetCode时间87.79%、空间不行5%，虽然A出了算法题，但是不是最优解
1. 使用num_list来记录val，使用num_dict来记录val->ListNode。
2. 对num_list进行排序，从小到大获取其中的val，然后根据对应的val从num_dict中查找节点；
3. 自己创建一个dummy节点，然后不要忘了获取到节点的时候，需要把这个节点原来指向的对象变成None，否则会造成混乱。
"""


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num_list: List[int] = []
        num_dict: dict[int, List[ListNode]] = defaultdict(list)
        cur: Optional[ListNode] = head
        while cur:
            num_list.append(cur.val)
            num_dict[cur.val].append(cur)
            cur = cur.next

        num_list.sort()

        dummy: ListNode = ListNode()
        cur = dummy
        for n in num_list:
            while num_dict[n]:
                node: ListNode = num_dict[n].pop()
                node.next = None
                cur.next = node
                cur = cur.next

        return dummy.next
