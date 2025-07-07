## Python版本的数据结构和算法

> 基于Bilibili课程：[【北京大学】数据结构与算法Python版（完整版）](https://www.bilibili.com/video/BV1VC4y1x7uv/?p=87&share_source=copy_web&vd_source=4462f9f91cf69d0596e719cbf56bea30)

个别代码会用到`pythonsds`这一个库，需要使用`pip install pythonds`进行安装。

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