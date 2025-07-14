

def binary_search(alist: list[int], item: int) -> int:
    first = 0
    last = len(alist) - 1

    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return mid
        else:
            if item < alist[mid]:
                last = mid - 1
            else:
                first = mid + 1
    # 如果没有发现就返回 -1
    return -1

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))