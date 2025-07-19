from typing import Optional

"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
解题思路：递归
1. 我们首先理解 mergeTwoLists 这个函数在做什么：
    * 传入两个链表的头节点，然后输出这两个链表按照升序排序好的新链表的头节点
2. 判断递归的三大条件：
    * 结束条件：list1的节点为空的时候，就把list2及剩下的返回；反之同理；
    * 递归逻辑：比对当前list1、list2节点的元素大小，取出更小的元素（比如list1）让list1拼接递归方法，让list1.next和list2继续进行比较；
        这一步相当于是让list1的下一个元素指向list1.next和list2这两个元素的更小值，也就是mergeTwoLists在干的事情；
    * 问题分解：我们可以发现，mergeTwoLists不断的把问题进行分解，每次的问题都是原来的更小问题，说明递归是可以做到解决问题本身的。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
            self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val > list2.val:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        else:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
