from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

"""
给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。
构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也
都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。
例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。
返回复制链表的头节点。
思路分析：脑筋急转弯（个人这么认为），思路来自灵神
1. 因为有random这个属性的存在，导致一遍遍历赋值的时候，如果random指向后方的一个元素，就会使得程序出现错误
    * 先有鸡还是先有蛋的问题，random中的元素可能会早于/晚于当前元素cur生成，但是没有random属性那么cur元素就不完整；
    * 那么我们可以用额外的哈希表/数组来存储每个「历史元素」，之后把random指向里面的元素即可，但是这样会占用大量空间。
2. 有没有办法能够满足兼顾时间顺序+节省空间（不用别的哈希表来查询所有元素）呢？
    * 原来的链表我们表示为 1 -> 2 -> 3 -> ...，新的链表我们表示为 1' -> 2' -> 3' -> ...
    * 我们借用原来的链表，每次遍历的时候把复制的元素挂在当前元素后面：1 -> 1' -> 2 -> 2' -> ...
    * 这样有什么好处呢？如果1的random指向17，那么1'的random指向17.next（也就是17'）。
3. 我们先第一遍遍历，把新元素一一对应地挂在旧元素后面，先不管random，先把值复制；
4. 再遍历第二遍链表，步长为2（就能保证遍历的都是旧元素），如果当前有random，那么就给自己cur.next.random = cur.random.next（满足传递性）
5. 最后为了不破坏原来的链表，我们把一个个新元素摘出来构建一个新链表，然后把链表修复。
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cur: Optional[Node] = head
        while cur:
            # 先初始化一个val相等的节点挂在原来节点的后面
            cur.next = Node(cur.val, cur.next)
            cur = cur.next.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        new_head: Optional[Node] = head.next
        cur = head
        # 我们把原来的链表修复，把新元素挂在new_head后面
        while cur.next.next:
            copied: Optional[Node] = cur.next
            cur.next = copied.next
            copied.next = copied.next.next
            cur = cur.next

        cur.next = None
        return new_head