import heapq
from typing import List, Counter

"""
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
解题思路：堆排序
1. 我们使用 Python 常用的集合统计方法 Counter 来统计 {整数: 次数}，然后接下来我们要对 val 进行 K 大的堆排序，方法类似 LC215，但是我们此时不选择，而是找出 K 大及之后的所有 key；
2. 我们维护一个大小为 K 的 heap：
    * 在 heap 长度不及 K 的时候，直接把 (val, key) 加入到 heap 中；
    * 此处有个实现细节，为什么要把 val 放在元组的第一位呢？因为 Python 内部排序如果碰到这种非整数、字符串变量，特别是元组，会优先按照元组第一个元素进行比较；
    * 如果碰到出现次数相同的情况怎么办？题目说明了 K 大的元素数量都是唯一的，因此只要是 K 大的元素，出现次数一定 unique 同时比别的出现次数多，一定会加入到 heap 中；
    * 如果 heap 长度 超过了 K，我们使用 heappushpop，它会比较当前元素 val 和栈顶元素 val，如果堆顶更小，就把堆顶弹出然后插入当前出现次数更多的元素 (val, key)；
3. 相比于手动判断 if heap[0][0] < val，然后手动弹出堆顶再插入新元素，这边会涉及到一次上浮一次下沉，而 heappushpop 判断完更小之后，只需要一次 sift-up；
4. 时间复杂度是在 O(Nlog k)，符合题目要求。
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elem_dict: dict[int, int] = Counter(nums)
        heap: List[tuple[int, int]] = []
        for key, val in elem_dict.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))

        return [item[1] for item in heap]


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
