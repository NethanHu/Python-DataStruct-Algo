from collections import deque
from typing import List, Deque

"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，
并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
思路很简单，我们先对intervals按第一元素进行排序，保证第一个元素是单调不递减
然后我们使用deque来模拟queue，循环的步骤如下：
1. 每次popleft出两个元素，对它们进行分类讨论：
    * 如果第一个元素包裹了第二个元素，就返回第一个元素，因为它们合体了，所以再将它appendleft放回到queue中；
    * 如果第一个元素和第二个元素部分重合，就返回他们的并集，再放回去等待下一次讨论；
    * 如果两个元素没有重合的部分，就把第一个元素加入到ans中，因为第一个元素已经无法与后面进行合体，再将第二个元素再次加回到queue中。
2. 在循环结束后，queue中还会剩一个元素，把它加入到ans中，最后返回ans。
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        s_intv: List[List[int]] = sorted(intervals, key=lambda x: x[0])
        queue: Deque[List[int]] = deque(s_intv)
        ans: List[List[int]] = []
        while len(queue) > 1:
            l_intv: List[int] = queue.popleft()
            r_intv: List[int] = queue.popleft()
            if l_intv[1] >= r_intv[0]:
                # 说明是连续的
                if l_intv[1] <= r_intv[1]:
                    # 说明我们取左intv的左界、右intv的右界
                    queue.appendleft([l_intv[0], r_intv[1]])
                else:
                    # 说明左intv把整个右intv包裹了进去
                    queue.appendleft(l_intv)
            else:
                # 说明是不连续的，把左区间加入到ans中，把右区间塞回去
                ans.append(l_intv)
                queue.appendleft(r_intv)
        ans.append(queue.popleft())
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
