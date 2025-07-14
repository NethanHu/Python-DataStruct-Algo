import random
import timeit

from SortAlgorithm.InsertionSort import insertion_sort
from SortAlgorithm.MergeSort import merge_sort
from SortAlgorithm.QuickSort import quick_sort
from SortAlgorithm.ShellSort import shell_sort


# ==============================================================================
# 性能测试主逻辑
# ==============================================================================

def generate_random_list(size: int, min_val: int = 0, max_val: int = 100000) -> list[int]:
    """生成一个指定大小的随机整数列表。"""
    return [random.randint(min_val, max_val) for _ in range(size)]

def run_sorting_test():
    """执行排序算法的性能测试并打印结果。"""
    # 定义要测试的列表规模
    list_sizes = [5000, 10000, 50000]

    # 定义要测试的排序算法
    sorting_algorithms = {
        "Insertion Sort": insertion_sort,
        "Shell Sort": shell_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Python's Timsort (sorted)": sorted # 加入Python内置排序作为性能基准
    }

    print("开始排序算法性能测试...")
    print("-" * 60)

    for size in list_sizes:
        print(f"[*] 测试列表规模: {size} 个元素")

        # 1. 生成一个大规模的随机列表
        original_list = generate_random_list(size)

        results = {}

        for name, func in sorting_algorithms.items():
            # 2. 为每个算法创建一个列表副本，确保测试数据一致
            list_copy = original_list[:]

            # 3. 使用 timeit 进行时间测试
            # setup部分导入函数，stmt部分执行函数
            # number=1 表示只执行一次（对于大规模排序足够了）
            # 使用 lambda 来调用函数，因为它比直接传字符串更灵活
            stmt = lambda: func(list_copy)

            # Python内置的sorted函数返回新列表，所以调用方式不同
            if name == "Python's Timsort (sorted)":
                stmt = lambda: sorted(list_copy)

            try:
                # timeit 会返回执行 stmt 指定次数（number）所花费的总秒数
                time_taken = timeit.timeit(stmt, number=1)
                results[name] = time_taken
            except Exception as e:
                results[name] = f"Error: {e}"

        # 4. 打印本次规模的测试结果
        for name, time_taken in results.items():
            if isinstance(time_taken, float):
                print(f"  - {name:<28}: {time_taken:.6f} 秒")
            else:
                print(f"  - {name:<28}: {time_taken}")
        print("-" * 60)

if __name__ == "__main__":
    run_sorting_test()