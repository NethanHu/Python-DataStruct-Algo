from typing import List

"""
不使用任何内建的哈希表库设计一个哈希映射（HashMap）。

实现 MyHashMap 类：

MyHashMap() 用空映射初始化对象
void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。
"""
class MyHashMap:
    # 我们使用数据链法（简单），不用线性探测法（remove更复杂）
    def __init__(self):
        self.size: int = 128
        self.data: List[List[List[int, int]]] = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        hash_val: int = key % self.size
        # 查询kv是否已经在data里面
        for kv in self.data[hash_val]:
            if kv[0] == key:
                kv[1] = value
                return
        self.data[hash_val].append([key, value])

    def get(self, key: int) -> int:
        hash_val: int = key % self.size
        for kv in self.data[hash_val]:
            if kv[0] == key:
                return kv[1]
        return -1

    def remove(self, key: int) -> None:
        hash_val: int = key % self.size
        bucket: List[tuple[int, int]] = self.data[hash_val]
        for i, kv in enumerate(self.data[hash_val]):
            if kv[0] == key:
                del bucket[i]



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)