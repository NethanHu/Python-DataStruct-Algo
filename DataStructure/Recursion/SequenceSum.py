"""
递归的“三定律”：
1. 必须包含基本结束条件：需要定义一个临界值，到这里会结束程序
2. 算法必须有演进：每一次操作完之后的结果是原来的状态进行了缩减
3. 调用自身：将问题分解成“更小自身”的相同问题
"""
def list_sum(num_list: list[int]) -> int:
    if len(num_list) == 1:
        return num_list[0]
    else:
        # 将前面累加的结果 加上 新的数组从"第二个数后面的全部"
        return num_list[0] + list_sum(num_list[1:])

my_list = [1, 2, 3, 4, 5, 6]
print(list_sum(my_list))