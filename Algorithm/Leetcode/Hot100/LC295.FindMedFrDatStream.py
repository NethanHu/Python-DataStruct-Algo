import bisect
from typing import List

"""
中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。
例如 arr = [2,3,4] 的中位数是 3 。
例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
实现 MedianFinder 类:
MedianFinder() 初始化 MedianFinder 对象。
void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。
解题思路：二分插入保持数组有序
1. 这道题目可以直接维护一个 SortedList，然后不断 add 新元素；或者维护一个普通 list，不断使用二分插入 bisect.insort_left 插入，中位数就很好求出来了；
2. 这道题目的正解应该是维护两个堆，一个大顶堆、一个小顶堆，各保存一半的元素，但是 Python 没有大顶堆，所以较为复杂，只能用负值代替。
"""


class MedianFinder:
    def __init__(self):
        self.sorted_list: List[int] = []
        self.size: int = 0

    def addNum(self, num: int) -> None:
        bisect.insort_left(self.sorted_list, num)
        self.size += 1

    def findMedian(self) -> float:
        if len(self.sorted_list) % 2 == 0:
            return (self.sorted_list[self.size // 2 - 1] + self.sorted_list[self.size // 2]) / 2
        else:
            return self.sorted_list[self.size // 2]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
