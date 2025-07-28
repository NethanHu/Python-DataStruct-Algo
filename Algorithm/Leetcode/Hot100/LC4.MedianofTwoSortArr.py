from bisect import bisect_left
from math import inf
from typing import List

"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
算法的时间复杂度应该为 O(log (m+n)) 。
解题思路：二分查找+数学
1. 暴力的方法就是把两个数组直接合并，然后使用排序方法，最后使用原生中位数方法就可以实现；但是这样的时间复杂度在O(m+n)插入+O(log n)排序，达不到题目的要求
   因此我们接下来做的，就是用不插入不排序的方式，通过二分查找的方法来解决这个问题。
2. 我们思考一下中位数的定义是什么，中位数是一个特殊临界点：
    * 如果长度为奇数，那么中位数恰好在中间点，把数组分成了左右「等长」两部分；如果长度为偶数，那么中间两个数可以把数组分成左右「等长」两部分；
    * 同时左半边的「最大值」一定会小于等于右半边的「最小值」。
3. 我们采用划分数组的方法，以中位数为界，左半和右半部分遵循以下关系（长度关系和大小关系）：
    * 我们首先确保 nums1 长度小于等于 nums2，这样我们就获得了较小的长度 m 和较长的长度 n，我们不去分析奇偶数的情况，直接让左半部分的长度为 (m + n + 1) // 2；
    * nums1 左半部分的最大值，必须小于等于 nums2 右半部分的最小值。并且，nums2 左半部分的最大值，必须小于等于 nums1 右半部分的最小值。
4. 由于长度固定好了，如果我们能遍历（或者是搜索）nums1 的指针 i，那么 nums2 的指针 j 就可以 (m + n - 1) // 2 - i 得到。
    * 我们使用 Python 二分查找方法简化搜索，从左边开始搜索，直到发现第一个 i 使得 nums1[i] > nums2[(m + n - 1) // 2 - i])，说明这是一个第一个「太大」的 i，它的前者才是我们需要的 i；
    * 为什么不考虑 j，因为此时 j 是关于 i 的函数，我们把问题简化成了寻找 i 即可。
E.g.:
* 奇数情况，我们的划分如下：
    nums1: 1   3   5   7 | 9
    nums2: 2   8 | 12  18  20  22  23
* 偶数情况，我们的划分如下：
    nums1: 1   3   5   7   9 | 11
    nums2: 2   8 | 12  18  20  22  23
5. 有了以上部分的示例，求得中位数就很简单了，我们考虑中位数边界情况和奇偶性，左半部分的最大值就是 max(ai, bj)，右半部分的最小值就是 min(ai1, bj1)。
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        # 注意 range(m) 是 O(1) 的，不是 O(m)
        i = bisect_left(range(m), True, key=lambda i: nums1[i] > nums2[(m + n - 1) // 2 - i]) - 1

        j = (m + n - 3) // 2 - i
        ai = nums1[i] if i >= 0 else -inf
        bj = nums2[j] if j >= 0 else -inf
        ai1 = nums1[i + 1] if i + 1 < m else inf
        bj1 = nums2[j + 1] if j + 1 < n else inf
        max1 = max(ai, bj)
        min2 = min(ai1, bj1)
        return max1 if (m + n) % 2 else (max1 + min2) / 2


"""
Appendix A.
(m + n - 3) // 2：用于计算分割点 j
这个数字出现在计算 nums2 的分割点 j 的公式 j = (m + n - 3) // 2 - i 中。
我们来看它是如何推导出来的：
我们要在 nums1 中取 i+1 个元素（从索引 0 到 i），在 nums2 中取 j+1 个元素（从索引 0 到 j），作为我们的左半部分。
左半部分的总元素个数必须等于我们上面算出的 k_size。
    所以：(i + 1) + (j + 1) = k_size
代入 k_size = (m + n + 1) // 2：
    (i + 1) + (j + 1) = (m + n + 1) // 2
我们来解这个关于 j 的方程：
    j + 2 = (m + n + 1) // 2 - i
    j = (m + n + 1) // 2 - i - 2
在整数除法中，(a // b) - c 等于 ((a - b*c) // b)。所以：
    j = (m + n + 1 - 4) // 2 - i
    j = (m + n - 3) // 2 - i

Appendix B.
j_check = (m + n - 1) // 2 - i。这个 j_check 到底是谁的索引？
这其实是另一个常见的分割点定义。设左半部分 i 个元素，右半部分 j 个元素。i+j = (m+n)/2。这里的 i 和 j 是数量。
nums1 取 i 个，nums2 取 j 个。
i 的范围 0..m。当 nums1 取 i 个时，nums2 取 j = (m+n)/2 - i 个。
判断条件为 max(left) <= min(right)，即 nums1[i-1] <= nums2[j] 且 nums2[j-1] <= nums1[i]。
代码 lambda i: nums1[i] > nums2[(m + n - 1) // 2 - i] 判断的是 nums1[i] > nums2[j_check]。
这里的 j_check 就对应了 j-1。
j = (m+n)/2 - i  (这里的 i, j是数量)
j-1 的索引 (j-1)
"""