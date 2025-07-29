import heapq
import random
from typing import List

"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
解题思路1（简单）：使用heapq来维护一个大小为K的最小堆
1. 先解释一下最小堆的性质，最小堆的堆顶 heap[0] 就是当前堆中最小元素；我们想找到第 K 大的元素，也就是从一个排序后的数组从后往前数第 K 个：
    * 这就让我们联想到只要维护一个大小为 K 的最小堆，逐渐往堆中填充 nums 的各个元素，那么堆顶就一直都是第 K 大元素。
2. 由于 Python 不能设定 heap 大小，一开始我们不断 push，在长度达到 K 的时候就变成先 push 再 pop，这样就能一直维护一个大小为 K 的最小堆；
3. 查看官方文档，我们发现了一个 heappushpop 操作，这个方法会比先 push 再 pop 效率更高（时间从90ms变成60ms），因为一开始 push 只会和堆顶做比较，如果比堆顶小，
   就不再加入 sift-up 的环节，减少操作数；
4. 但是时间复杂度在 O(Nlog k)，是严格意义上的「准线性」，但是不能和 O(N) 完全相等。因此这种方法严格来说不正确。

解题思路2：快速选择
1. 我们首先任意选择一个搜索元，通过该搜索元，我们将要搜索的数组分成三份：
    * 大于 pivot 的归类于 more，小于 pivot 的归类于 less，相等归类于 equal。
2. 我们举个例子会比较好，假设我们的数组经过排序后是这样的：
    * [1  2  3 | 5 | 6  7  8  9] pivot 随机选择到了 5，然后我们要求第 3 大元素：
      那么此时满足这个条件 cur_k <= len(more)（3 <= 4），我们接下来要去 [6  7  8  9] 中继续搜索第 3 大元素（保留第 K 大）
    * [6  7 | 8 | 9] pivot 随机选择到了 8，然后我们要求第 3 大元素：
      此时满足条件 cur_k > len(more) + len(equal)（3 > 2），通过图中可以明显看出来，「倒数」第三个元素已经超过了 equal 和 more 的总长度，落在了 less 里面
      那么此时我们要找的数组就是 less，同时第 K 大元素就变成了在 Less 中的第 k - len(more) - len(equal) = 3 - 1 - 1 = 1 大元素
    * [6 | 7 | ] pivot 随机选到了 7，此时不再进入到递归的方法中，直接返回当前 pivot，也就是我们的正确答案。
3. 每次分区操作的成本与当前子数组的长度成正比,总操作次数大约是：
    N + N/2 + N/4 + N/8 +... 这是一个等比数列，其和收敛于 2N。因此，它的平均时间复杂度是 O(N)。
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(cur_nums: List[int], cur_k: int) -> int:
            pivot: int = random.choice(cur_nums)
            more, equal, less = [], [], []
            for n in cur_nums:
                if n > pivot:
                    more.append(n)
                elif n < pivot:
                    less.append(n)
                else:
                    equal.append(n)
            # 我们根据条件来查找第 K 大元素在哪个集合里面，然后就只找这个集合即可
            if cur_k <= len(more):
                return quickSelect(more, cur_k)
            if cur_k > len(more) + len(equal):
                return quickSelect(less, cur_k - len(more) - len(equal))
            return pivot

        return quickSelect(nums, k)

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     heap: List[int] = []
    #     for n in nums:
    #         if len(heap) < k:
    #             heapq.heappush(heap, n)
    #         else:
    #             heapq.heappushpop(heap, n)
    #     return heap[0]


if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
