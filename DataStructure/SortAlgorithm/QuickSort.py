def inplace_swap(alist: list[int], i: int, j: int) -> None:
    alist[i], alist[j] = alist[j], alist[i]

def find_mid(a: int, b: int, c: int) -> int:
    if a == max([a, b, c]):
        return b if b > c else c
    elif b == max([a, b, c]):
        return a if a > c else c
    else:
        return b if b > a else a

def partition(alist: list[int], first: int, last: int) -> int:
    pivot = find_mid(alist[first], alist[len(alist) // 2], alist[last])
    left_ptr = first + 1
    right_ptr = last

    done = False
    while not done:
        # 移动左指针，确保左半边应该比pivot更小。如果在左边找到一个比pivot大的值就停止移动
        while left_ptr <= right_ptr and alist[left_ptr] <= pivot:
            left_ptr += 1
        # 移动右指针，确保右半边应该比pivot更大。如果在右边找到一个比pivot小的值就停止移动
        while left_ptr <= right_ptr and alist[right_ptr] >= pivot:
            right_ptr -= 1

        # 如果左指针的下标大于右指针下标，说明两者已经交错，结束移动
        if left_ptr > right_ptr:
            done = True
        else:
            # 左边找到了比pivot大的数，右边找到了比pivot小的数，交换他们
            inplace_swap(alist, left_ptr, right_ptr)
    # 当它们交错后，阵列的状态看起来像这样：
    # [pivot, ... (<= pivot 的元素) ..., alist[right_ptr], alist[left_ptr], ... (>= pivot 的元素) ...]
    # alist[left_ptr] 是大于等于 pivot 的，因此我们无法把 pivot 与 alist[left_ptr] 进行交换（因为左边的所有元素都应该小于等于pivot）
    # 最后把第一个数（也就是pivot）与中位点进行交换
    inplace_swap(alist, first, right_ptr)
    return right_ptr

def rec_quick_sort(alist: list[int], first: int, last: int) -> None:
    if first < last:
        split_point = partition(alist, first, last)
        rec_quick_sort(alist, first, split_point - 1)
        rec_quick_sort(alist, split_point + 1, last)

def quick_sort(alist: list[int]) -> None:
    rec_quick_sort(alist, 0, len(alist) - 1)


# test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 32]
# quick_sort(test_list)
# print(test_list)