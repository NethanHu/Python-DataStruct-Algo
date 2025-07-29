from typing import List

"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
解题思路：单调栈
1. 本题和接雨水是反过来的题目，本题使用了单调递增栈（从栈底到栈顶递增），这样有什么好处呢？
    * 只用遍历一次，维护一个单调递增栈，如果元素不断递增，就不断加入到栈中；如果出现了递减，就把当前元素当成右边界 ri（用来求宽度）
      不断 pop 出 stack 栈顶元素并把它当成 middle 元素，此时我们通过栈顶元素的 mi 和 mh 就可以求出「以 mid 左边元素为左边界 li，当前元素为右边界 ri，mid 元素的高度 mh」的矩形面积。
2. 为什么可以这样做呢？
    * 由于单调递增栈的性质，我们可以得知 ri 不断往右（停在不递增的地方），然后 mi 是不断向左回溯的；
    * 面积公式 = mh * (ri - li - 1)，即回溯到的元素 mi 对应的高度 mh 乘上两个边界的差值 - 1；
    * 为什么可以这样计算呢？因为有单调递增栈的存在，stack 中所有 mid 元素的高度都能从左→右贯穿整个高度线
    例如单调栈中下标对应的高度为 [-1, 1, 5, 6]，遍历到6的时候，面积为6 * 1；5的时候，由于 6 >= 5，5的高度可以延伸到6的位置，因此高度是5 * 2；1的时候，1可以贯穿5、6，因此面积为1 * 3。
4. 几个小细节：
    * 为了防止出现数组只有单调递增/递减情况，我们加入头尾哨兵 -1，而且为了能照顾头元素的计算，我们第一个元素是 -1 正好可以抵消掉 (ri - li - 1) 中的减1操作；
    * 我们有且只有三个元素存在的时候才能进行操作，即一次遍历中的右指针 ri，不断 pop 出的 middle 元素 mi，以及递增的起点 li；
    * 在 pop 操作和面积计算结束之后，不要忘了把当前元素 append 到栈中。
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)
        stack: List[int] = [-1]
        ans: int = 0
        for ri, rh in enumerate(heights):
            while len(stack) > 1 and rh <= heights[stack[-1]]:
                mi: int = stack.pop()
                mh: int = heights[mi]
                li: int = stack[-1]
                area: int = mh * (ri - li - 1)
                ans = max(ans, area)
            stack.append(ri)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
