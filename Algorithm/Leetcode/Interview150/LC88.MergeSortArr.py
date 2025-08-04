from typing import List

"""
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
解题思路：数组+双指针
1. 本题从前往后遍历，会带来 0 判断的问题，我们不妨从后往前插入，依次从 nums1 和 nums2 最后一个元素中找最大的，插入到 nums1 的最后去； 
2. 我们只需要考虑 p2 >= 0 即可，因为毕竟是把 nums2 插入到 nums1 中：
    * 如果 nums2 首先用完，说明剩下的 nums1 肯定是有序的；反之，说明 nums1 用的更快，剩余 nums2 的元素就直接逐步插入即可。
3. 优化技巧是我们合并一系列条件：
    * 我们把 p1 >= 0 和 nums1[p1] > nums2[p2] 这俩条件并入一起，即当 nums1 还有元素 + nums1 更大要后移放在一起：
    * 其他的比如 nums1 用完、nums1[p1] <= nums2[p2] 这些就是在 else 里面，此时是 nums2 的指针前移；
    * 两个条件之后都需要把总的后指针前移。
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, p = m - 1, n - 1, m + n - 1
        # 我们只要考虑 p2 即可
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                # 此时的情况是 nums1 更大，所以需要后移
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                # 此时包含着 nums2 更大要更后移 + nums1 都用完了可以只填充 nums2
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
