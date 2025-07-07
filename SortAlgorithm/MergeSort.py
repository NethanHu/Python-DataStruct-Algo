
# 归并排序是一种原地修改的排序形式，尽管不断地开辟左右两边数组的副本空间，但是最后alist如何修改完全是原地修改的
# 因为需要改变的值是来自于副本内的，alist本身不需要任何的swap操作
def merge_sort(alist: list[int]) -> None:
    if len(alist) > 1:
        mid = len(alist) // 2 # --> 这里要对数组进行拆分，将一个原数组对半拆分
        left_half = alist[:mid]
        right_half = alist[mid:]
        merge_sort(left_half)  # --> 这里对左半边继续进行拆分
        merge_sort(right_half) # --> 这里对右半边继续进行拆分
        i = j = k = 0  # --> i是左半边指针，j是右半边指针，k是在两半边结合之后的列表中的指针
        # 因为此时我们已经为左半边、右半边和原来的数组都开辟了内存空间，所以可以直接通过数组的下标取值
        while i < len(left_half) and j < len(right_half):
            # 类似于拉链式的从两边比较数字大小，把小的插入到前面
            # 被取了数字的半边数组指针后移一格
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i += 1
            else:
                alist[k] = right_half[j]
                j += 1
            # 原数组指针后移一格
            k += 1
        # 当两半边有一个已经取完数字之后，把另一半边剩余的数字依次放到原数组的后面
        while i < len(left_half):
            alist[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            alist[k] = right_half[j]
            j += 1
            k += 1

def pythonic_merge_sort(alist: list[int]) -> list[int]:
    if len(alist) <= 1:
        return alist

    m = len(alist) // 2
    l = pythonic_merge_sort(alist[:m])
    r = pythonic_merge_sort(alist[m:])

    merged = []
    while l and r:
        if l[0] <= r[0]:
            merged.append(l.pop(0))
        else:
            merged.append(r.pop(0))

    merged.extend(r if r else l)
    return merged



# test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 32]
# print(pythonic_merge_sort(test_list))