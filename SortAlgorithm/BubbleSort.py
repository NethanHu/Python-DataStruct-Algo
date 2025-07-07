

def bubble_sort(alist: list[int]) -> None:
    # 一开始从头完整遍历一遍数组，第二轮从头遍历到倒数第二项，...
    for interval in range(len(alist) - 1, 0, -1):
        for i in range(interval):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

def fast_bubble_sort(alist: list[int]) -> None:
    # 如果一趟下来前几位已经完全不需要swap操作了，那么就可以直接退出
    need_exchange = True
    interval = len(alist) - 1
    # 一开始从头完整遍历一遍数组，第二轮从头遍历到倒数第二项，...
    while interval > 0 and need_exchange:
        need_exchange = False
        for i in range(interval):
            if alist[i] > alist[i + 1]:
                # 只要这一趟下来还是存在着swap操作，那么还是需要exchange
                need_exchange = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        interval -= 1

# test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# fast_bubble_sort(test_list)
# print(test_list)