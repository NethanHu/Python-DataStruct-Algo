"""
你可以选择使用单链表或者双链表，设计并实现自己的链表。

单链表中的节点应该具备两个属性：val 和 next 。val 是当前节点的值，next 是指向下一个节点的指针/引用。

如果是双向链表，则还需要属性 prev 以指示链表中的上一个节点。假设链表中的所有节点下标从 0 开始。

实现 MyLinkedList 类：

MyLinkedList() 初始化 MyLinkedList 对象。
int get(int index) 获取链表中下标为 index 的节点的值。如果下标无效，则返回 -1 。
void addAtHead(int val) 将一个值为 val 的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。
void addAtTail(int val) 将一个值为 val 的节点追加到链表中作为链表的最后一个元素。
void addAtIndex(int index, int val) 将一个值为 val 的节点插入到链表中下标为 index 的节点之前。如果 index 等于链表的长度，那么该节点会被追加到链表的末尾。如果 index 比长度更大，该节点将 不会插入 到链表中。
void deleteAtIndex(int index) 如果下标有效，则删除链表中下标为 index 的节点。
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Node | None = next


class MyLinkedList:
    def __init__(self):
        self.head: Node = Node()
        self.size: int = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        cur_node: Node = self.head
        # 要多遍历一次，因为头节点是哑节点
        for _ in range(index + 1):
            cur_node = cur_node.next
        return cur_node.val

    # 哑节点永远是卫兵，千万不要试图给哑节点赋值成为正常节点，然后再塞一个哑节点（这是违背设计理念的）
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        # 遍历到最后的节点
        cur_node: Node = self.head
        for _ in range(self.size):
            cur_node = cur_node.next
        cur_node.next = Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return None
        elif index == self.size:
            self.addAtTail(val)
            return None
        else:
            cur_node: Node = self.head
            for _ in range(index):
                cur_node = cur_node.next
            # 此时cur_node已经到了待插入节点的前面
            new_node: Node = Node(val)
            new_node.next = cur_node.next
            cur_node.next = new_node
            self.size += 1
            return None

    def deleteAtIndex(self, index: int) -> None:
        if index < self.size:
            pre_node: Node = self.head
            cur_node: Node = self.head
            for _ in range(index):
                cur_node = cur_node.next
                pre_node = pre_node.next
            del_node = cur_node.next
            pre_node.next = del_node.next
            del_node.next = None
            self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
