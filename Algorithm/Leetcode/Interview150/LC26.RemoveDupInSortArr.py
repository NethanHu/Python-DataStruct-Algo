from typing import List

"""
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。
考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：
更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。返回 k 。
解题思路：双指针+哈希表
1. 由于要去重，我们不妨设置一个 set 来记录下当前已经出现过的元素，如果遍历到的元素在 set 中，那就直接跳过；
2. 思路很简单，我们设置一个指针 i 来控制「有效且元素唯一」数组的右边界，如果 i 遍历到的元素没有出现过在 set 中，就让 i 自增；
    * 当指针 i 遍历到的元素在 set 中出现过的时候，我们设置一个从 i 位置出发的指针 j，向后寻找第一个未出现的元素，然后把找到的元素先添加到 set，然后把该元素换到 i 的位置上；
    * 如果 j 遍历到数组的末尾，都没有找到新的元素时候，则整个循环退出，因为接下来的所有元素都已经重复了，不会再次出现新的元素；
    * 最后返回指针 i，因为指针 i 的左边都是唯一只出现一次的元素，同时也保持了原来的递增顺序。
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup_num: set[int] = set()
        i: int = 0
        while i < len(nums):
            if nums[i] not in dup_num:
                dup_num.add(nums[i])
                i += 1
            else:
                j: int = i
                while j < len(nums):
                    if nums[j] in dup_num:
                        j += 1
                    else:
                        # 如果发现了第一个不重复的元素，就更换，同时 i 应该走到下一个元素上
                        dup_num.add(nums[j])
                        nums[i] = nums[j]
                        i += 1
                        break
                if j == len(nums):
                    break
        return i


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
