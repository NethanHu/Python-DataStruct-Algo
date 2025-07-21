## Python版本的数据结构和算法

> 基于Bilibili课程：[【北京大学】数据结构与算法Python版（完整版）](https://www.bilibili.com/video/BV1VC4y1x7uv/?p=87&share_source=copy_web&vd_source=4462f9f91cf69d0596e719cbf56bea30)

个别代码会用到`pythonds`这一个库，需要使用`pip install pythonds`进行安装。

相比于Java的数据结构，Python拥有List、deque这种强大的原生数据结构，在实现形式上变得非常简单。在保持简洁性的同时，也保证使用大规模注释来保证理解。
代码全部进行手写整理，相比于老师课上的源代码，在实现过程中也包含了`typing`库的[PEP484](https://peps.python.org/pep-0484/)代码规范，标注出数据类型，
使其更加优雅和规范。例如：

```python
def order_by_available(n: DFSVertex) -> list[DFSVertex]:
    res_list: list[tuple[int, DFSVertex]] = []
    for v in n.get_connections():
        if v.get_color() == 'white':
            c = 0
            for w in v.get_connections():
                if w.get_color() == 'white':
                    c += 1
            res_list.append((c, v))
    res_list.sort(key=lambda x: x[0])
    return [y[1] for y in res_list]
```

在[Algorithm](Algorithm/)中，上传了个人认为比较有记录意义的经典题型。题目来自[LeetCode 基础50题](https://leetcode.cn/studyplan/programming-skills/)、[LeetCode Hot100题](https://leetcode.cn/studyplan/top-100-liked/)。
正在持续刷题中，会持续将经典题、思路巧妙题、死记硬背等题型进行上传。其中里面包含自己的思路分析，以供复习或交流使用。

使用Python3做LeetCode的一些小技巧：
> 根据官方描述：版本：Python 3.11
> 
> 为了方便起见，大部分常用库已经被自动 导入，如array, bisect, collections。 如果您需要使用其他库函数，请自行导入。
> 
> 如需使用 Map/TreeMap 数据结构，您可使用 sortedcontainers 库。
 
这些预导入的库有几个好处：

| 库/模块             | 核心数据结构                      | 一句话总结                | 典型应用场景               |
|------------------|-----------------------------|----------------------|----------------------|
| collections      | deque, Counter, defaultdict | 绝对主力，几乎所有类型的题目都可能用到。 | BFS、滑动窗口、频率统计、分组、建图。 |
| bisect           | (无，是工具)                     | 在已排序列表中进行高效的二分查找和插入。 | 动态维护有序数组、最长递增子序列。    |
| sortedcontainers | SortedList, SortedDict      | 解题大杀器，处理需要动态维护的有序集合。 | 滑动窗口中位数、日程表问题、区间问题。  |
| array            | array                       | 内存优化的 list，但类型受限。    | 在 LeetCode 中极少使用。    |
| heapq            | min-heap / max-heap         | 用来解决优先队列问题。          | 某些题目会使用到，比如LC23。     |



P.S.: 如果发现LeetCode Hot100题库中没有收录某些题目，这些题目大概率已经收录在了Base50中（如果思路不变的情况下）。如果Base50、Hot100都收录了某道题目，
说明两者在思路上、实现上有一定的差异。
