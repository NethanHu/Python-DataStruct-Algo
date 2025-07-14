class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key: int) -> int:
        return key % self.size

    # 线性探测的逻辑
    def rehash(self, old_hash: int) -> int:
        # 我们也可以在这里使用+3，因为gcd(1, 11) = 1，gcd(3, 11) = 1
        # 使用+1就是标准的线性探测，+3是带步长的线性探测，+3的性能通常优于+1，因为可以防止聚集
        return (old_hash + 1) % self.size

    def put(self, key: int, data) -> None:
        hash_val = self.hash_function(key)
        # 如果当前空槽没有被占用，就把这个空槽和对应的data来进行存储
        if self.slots[hash_val] is None:
            self.slots[hash_val] = key
            self.data[hash_val] = data
        else:
            # 如果当前空槽已经有元素，且是相同的key时，进行替换（更新操作）
            if self.slots[hash_val] == key:
                self.data[hash_val] = data
            else:
                # 如果当前空槽已经被占用了，就再次进行哈希计算
                next_slot = self.rehash(hash_val)
                # 反复进行rehash操作，直到计算出一个hash可供使用（要么就是空槽，要么又算回到了自己之前的hash，就更新自己的data）
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot)

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def get(self, key: int):
        start_slot = self.hash_function(key)
        data = None
        stop = False
        found = False
        pos = start_slot
        # 这是一个很精髓的查找过程：
        # 1. 首先拿到初始的key，我们对key进行hash操作，得到一个slot的位置。
        #    此时我们进入slot比较我们查找的key和slot中的key是不是一样，如果一样就返回data；否则就rehash
        # 2. 不断进行rehash，直到出现三种结果：
        #    - 在一个rehash之后的slot中找到了我们要查找的key，此时返回data；
        #    - rehash了一个None的空槽给我们，说明这个元素一开始就没加进来，否则不可能是空槽；
        #    - 兜兜转转又回到了start_slot，说明按hash函数遍历了一整遍都没有找到这个元素，因此不存在。
        # 因此我们可以明白一个事实，如果HashTable很空，那么查询效率很高，因为走几步就能找到（或者是找到None）
        # 如果HashTable很满，那么最坏情况下找一个不存在的元素需要完整遍历一遍table，效率低下
        while self.slots[pos] is not None and not found and not stop:
            # 使用一次hash计算，看看找到的那个slots中的key是不是我们要找的
            if self.slots[pos] == key:
                found = True
                data = self.data[pos]
            else:
                # 如果不是，再次进行rehash，直到找到我们对应的key，或者是回到原点
                pos = self.rehash(pos)
                if pos == start_slot:
                    stop = True
        return data
