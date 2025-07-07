

def selection_sort(alist: list[int]) -> None:
    # 大概思路就是先从一整个数组中找到最大的交换到最后面
    # 然后在 [0, len(alist)-1] 区间内找最大，交换到倒数第二个位置
    # 和 bubble sort 的区别在于没有那么多的 swap 操作，但是无法改变复杂度是O(n)
    for fill_slot in range(len(alist) - 1, 0, -1):
        max_pos = 0
        for loc in range(1, fill_slot + 1):
            if alist[loc] > alist[max_pos]:
                max_pos = loc
        alist[fill_slot], alist[max_pos] = alist[max_pos], alist[fill_slot]


# test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# selection_sort(test_list)
# print(test_list)