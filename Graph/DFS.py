from Graph.ADTGraph import Vertex, Graph


class DFSVertex(Vertex):
    def __init__(self, key, color: str='white'):
        super().__init__(key)
        self.connected_to: dict[DFSVertex, int] = {}
        # 一开始的时候节点被标记为白色
        self.color: str | None = color

    def get_color(self) -> str:
        return self.color

    def set_color(self, new_color: str):
        self.color = new_color

    def get_connections(self):
        return self.connected_to.keys()


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()

    def __iter__(self):
        return iter(self.vertex_list.values())

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = DFSVertex(key)
        self.vertex_list[key] = new_vertex
        return new_vertex

    def add_edge(self, from_key, to_key, cost=0):
        if from_key not in self.vertex_list:
            self.add_vertex(from_key)
        if to_key not in self.vertex_list:
            self.add_vertex(to_key)
        from_vertex: DFSVertex = self.vertex_list[from_key]
        to_vertex: DFSVertex = self.vertex_list[to_key]
        from_vertex.add_neighbor(to_vertex, cost)
        to_vertex.add_neighbor(from_vertex, cost)