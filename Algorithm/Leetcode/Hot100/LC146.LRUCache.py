from typing import Optional


class BiLinkNode:
    def __init__(self, key: int = 0, value: int = 0):
        self.key: int = key
        self.value: int = value
        self.prev: Optional[BiLinkNode] = None
        self.next: Optional[BiLinkNode] = None


"""
请你设计并实现一个满足 LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

解题思路：设计+双向链表+哈希表
1. 我们发现题目要求「函数 get 和 put 必须以 O(1) 的平均时间复杂度运行」，毋庸置疑这肯定是需要哈希表；
2. 但是LRU缓存又需要能够保存修改、查找的「历史记录」，因此必然在操作之后数据结构中的先后顺序会发生变化，结合还需要逐出关键词，我们想到删除时间只有O(1)的双向链表；
3. 因此思路明确，查找场景使用哈希表，而底层也会加入双向链表的使用：
    * 我们在构造双向链表的时候，使用两个dummy节点，一个是头节点（应付插入场景）一个是尾节点（应付删除场景），因此我们实现以下若干方法：
        - _add_to_head 可以把元素加入到头部（基础方法）
        - _remove_node 可以把某个位置的元素删除（基础方法）
        - _move_to_head 可以把某个元素从自己的位置先删除，然后再添加到头部（组合方法）
        - _remove_tail 可以把在tail之前的那个元素删除（组合方法，面对的是把多余的元素「逐出」的情况）
    * get 方法我们就去哈希表中查找，如果有就返回value，并且 _move_to_head；否则就是-1；
    * put 方法稍微麻烦一些，我们分类：
        - 如果在cache中，就进行update，同时把元素 _move_to_head
        - 如果不在cache中，就 _add_to_head，然后判断一下当前size有没有超过capacity，如果有就_remove_tail，然后把tail元素在cache中也删除
"""


class LRUCache:

    def __init__(self, capacity: int):
        self.cache: dict[int, BiLinkNode] = {}
        self.capacity: int = capacity
        self.size: int = 0
        # 这里的head和tail都是哑节点，位于头尾
        self.head: Optional[BiLinkNode] = BiLinkNode()
        self.tail: Optional[BiLinkNode] = BiLinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_head(self, node: BiLinkNode):
        node.prev = self.head
        node.next = self.head.next
        # 断开原来哑节点和第一个节点的连接，然后重新构造
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: BiLinkNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node: BiLinkNode):
        self._remove_node(node)
        self._add_to_head(node)

    def _remove_tail(self) -> BiLinkNode:
        node = self.tail.prev
        self._remove_node(node)
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            node = BiLinkNode(key, value)
            self.cache[key] = node
            self._add_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                node = self._remove_tail()
                del self.cache[node.key]
                self.size -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
