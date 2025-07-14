from typing import Iterator

from Graph.ADTGraph import Graph, Vertex


class GeneralDFSVertex(Vertex):
    def __init__(self, key):
        super().__init__(key)
        self.color = 'white' # white 代表还未发现这个节点
        self.pred: int | None = None
        self.discovery: bool = False
        self.finish_time: int = 0

    def set_color(self, new_color: str):
        self.color = new_color

    def get_color(self) -> str:
        return self.color

    def set_pred(self, pred):
        self.pred = pred # 这里的pred用的是key来表示

    def get_pred(self):
        return self.pred

    def set_discovery(self, state: bool):
        self.discovery = state

    def get_discovery(self) -> bool:
        return self.discovery

    def set_finish_time(self, time: int):
        self.finish_time = time

    def get_finish_time(self) -> int:
        return self.finish_time


class GeneralDFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.vertex_list: dict[int, GeneralDFSVertex] = {}
        self.time = 0

    def __iter__(self) -> Iterator[GeneralDFSVertex]:
        return iter(self.vertex_list.values())

    def dfs_visit(self, start_vertex: GeneralDFSVertex):
        start_vertex.set_color('grey')
        self.time += 1
        # 使用新的方法记录发现时间
        start_vertex.set_discovery(True)

        for next_vertex in start_vertex.get_connections():
            if next_vertex.get_color() == 'white':
                # 建议直接存储对象引用，而不是 key
                next_vertex.set_pred(start_vertex)
                self.dfs_visit(next_vertex)

        start_vertex.set_color('black')
        self.time += 1
        # 使用新的方法记录完成时间
        start_vertex.set_finish_time(self.time)

    def dfs(self):
        for a_vertex in self:
            a_vertex.set_color('white')
            a_vertex.set_pred(None) # 使用 None 作为前驱的初始值更通用

        self.time = 0 # 每次调用 dfs 时重置时间计数器
        for a_vertex in self:
            if a_vertex.get_color() == 'white':
                self.dfs_visit(a_vertex)

