
# 对间隔为gap的一串数字进行插入排序，我们假设start那个位置是子列表中的第一个，然后进行插入排序
def gap_insertion_sort(alist: list[int], start: int, gap: int) -> None:
    for i in range(start + gap, len(alist), gap):
        cur_value = alist[i]
        pos = i
        # 比较遍历到的数字与间隔为gap的上一个数字，如果当前数字更小，就与上一个数字交换
        while pos >= gap and cur_value < alist[pos - gap]:
            alist[pos] = alist[pos - gap]
            pos -= gap
        alist[pos] = cur_value


# 希尔排序将原数组进行间隔为n/2、n/4、...的子数组进行子插入排序，可以看到操作的粒度会越来越细
# 和插入排序相比，可以发现希尔排序的优化方法在于长距离移动，然后逐步缩短距离进行微调
# 时间复杂度在O(n log n)和O(n^1.5)之间
def shell_sort(alist: list[int]) -> None:
    sublist_interval = len(alist) // 2
    while sublist_interval > 0:
        # 如何理解这段循环？假设数组长度为10，一开始的间隔是10//2=5：
        # 那么分割出来的子插入排序应该会在下标为0和5，1和6，...，4和9的数字进行插入排序
        # 接下来间隔是5//2=2：
        # 子插入排序会发生在下标为0、2、4、6、8和1、3、5、7、9的这两个子列表中
        # 最后间隔是2//2=1：
        # 此时相当于对整个数组进行插入排序
        for start_pos in range(sublist_interval):
            gap_insertion_sort(alist, start_pos, sublist_interval)

        sublist_interval = sublist_interval // 2


# test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 32]
# shell_sort(test_list)
# print(test_list)

# 为什么这样会更快？
# 通过先对间隔较远的元素进行排序（大增量），希尔排序可以快速地将“逆序”的元素（比如本该在前面的小元素）
# 进行“长距离”的移动，让它们迅速到达大致正确的位置。这样，当后续增量变小时，列表已经变得“部分有序”。
# 我们知道插入排序在处理“几乎有序”的列表时效率非常高（接近O(n)），因此最后一轮 gap=1 的插入排序会执行得飞快。