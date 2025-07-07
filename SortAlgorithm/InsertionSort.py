
# 插入排序要维护一个子列表，类似于从大表中摸牌，每次把抽到的牌按照大小放到子列表中
# 依次遍历的是大表，依次插入的是子列表
# 注意，不需要开辟额外内存。只需要把大表的前半部分当成排好序的子列表，依次把后面的元素取出，插入到前面对应的位置即可

def insertion_sort(alist: list[int]) -> None:
    # 把第一个数字当成子列表的第一个元素，所以从第二个元素开始遍历
    for i in range(1, len(alist)):
        # 依次找到子列表之后的元素应该插入到子列表中的哪里
        cur_value = alist[i]  # 把当前位置的数字拿出来，目标是找到合适的插入位置
        pos = i  # 先假设位置不动，然后从后到前依次去比较当前元素与子列表中遍历的元素大小
        while pos > 0 and alist[pos - 1] > cur_value:
            alist[pos] = alist[pos - 1]  # 将子列表中拿来做比较的数与该数进行交换
            pos -= 1
        alist[pos] = cur_value  # 找到合适的位置之后，把拿起的数字插入其中

# test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# insertion_sort(test_list)
# print(test_list)