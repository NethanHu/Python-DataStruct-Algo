# 我们在这里使用的二叉堆是min-binaryheap，即根节点的key是最小的
class BinaryHeap:
    def __init__(self):
        # 列表首元素无用，因为我们需要二叉堆（完全二叉树）满足以下性质：
        # 当前节点下标为p，左子节点是2p、右子节点是2p+1；父节点是p//2；
        # 如果我们使用列表第0个元素，就不能达成数学上的良好性质
        self.heap_list = [0]
        self.cur_size = 0

    def find_min_child(self, i: int): # i 是下标
        if i * 2 + 1 > self.cur_size: # 这里的意思是只有左节点，就返回左节点
            return i * 2
        else:
            # 如果两个子节点都存在，就返回更小的那个下标
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1


    def perc_up(self, i: int): # i 是下标
        # 新key在路径上进行交换实际上是冒泡排序，两两比较：如果新key比父节点小，就和父节点交换
        while i // 2 > 0: # 只要没有到根节点，就可以一直循环
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def perc_down(self, i: int): # i 是下标
        while i * 2 <= self.cur_size: # 只要保证一直可以插入到当前节点的子节点上
            min_child = self.find_min_child(i)
            # 找到最小的子节点之后，如果当前节点比子节点更大，就与更小的子节点进行交换
            if self.heap_list[i] > self.heap_list[min_child]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[min_child]
                self.heap_list[min_child] = tmp
            i = min_child

    def insert(self, k: int): # k 是新插入的key
        # 新的key首先放在队尾，但是这样无法保持堆次序，因为二叉堆需要保证从根节点出发，
        # 无论往下的哪里走都是逐渐增大的。因此我们要根据路径让key“上浮”到正确位置上
        self.heap_list.append(k)
        self.cur_size += 1
        self.perc_up(self.cur_size)

    def del_min(self):
        # 移除最小的元素就是类似于pop出优先队列中的第一个元素，当然在这里就是根节点
        # 做法是：把最后一个元素放到根节点上，然后进行“反向冒泡”，不断下沉到正确的位置上
        # 注意，在这里当key比两个子节点都大的时候，我们选择与更小的那个子节点交换
        # 因为如果选大的，那么交换之后当前新key就会比另一边更大，就是不正确的
        ret_val = self.heap_list[1] # 这是要返回的第一个（最小的）元素
        self.heap_list[1] = self.heap_list[self.cur_size]
        self.cur_size -= 1
        self.heap_list.pop()
        # 因为整个size-1了之后，最后一个元素已经放到了最前面，所以此时将最后一个元素pop出去 -> O(1)
        self.perc_down(1)
        return ret_val

    def build_heap(self, alist: list[int]):
        i = len(alist) // 2
        # 以 i 为分界线（数组长度的一半），一半以后的元素肯定都在叶节点（无法下沉）
        # 因此我们就只要关心 i 之前的元素，依次对它们进行下沉操作
        # 此时的 i 是最后一个节点的父节点
        self.cur_size = len(alist)
        self.heap_list = [0] + alist[:]
        while i > 0:
            # 这里是从下往上进行修复当前“符合完全二叉树但是不满足二叉堆性质”的树
            # 从下开始修复的时候，能保证下层不需要再进行调整，然后在继续修复上一层即可
            # 与从头开始 insert 的O(nlog n)相比，这样的方法复杂度是O(n)
            self.perc_down(i)
            i -= 1