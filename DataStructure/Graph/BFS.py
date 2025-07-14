from Graph.ADTGraph import Graph, Vertex
from LinearStructure.Queue import Queue


class BFSVertex(Vertex):
    def __init__(self, key):
        super().__init__(key)
        self.distance: int = 0
        self.pred: BFSVertex | None = None
        self.color: str = 'white'

    def set_distance(self, dist: int):
        self.distance = dist

    def get_distance(self) -> int:
        return self.distance

    def set_pred(self, pred):
        self.pred = pred

    def get_pred(self):
        return self.pred

    def set_color(self, color: str):
        self.color = color

    def get_color(self) -> str:
        return self.color


class BFSGraph(Graph):
    def __init__(self):
        super().__init__()

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = BFSVertex(key)
        self.vertex_list[key] = new_vertex
        return new_vertex


def bfs(g: BFSGraph, start: BFSVertex):
    start.set_distance(0)
    start.set_pred(None)
    start.set_color('grey')
    vertex_queue = Queue()
    vertex_queue.enqueue(start)
    while vertex_queue.size() > 0:
        cur_vertex: BFSVertex = vertex_queue.dequeue()
        for nbr in cur_vertex.get_connections():
            if nbr.get_color() == 'white':
                nbr.set_color('grey')
                nbr.set_distance(cur_vertex.get_distance() + 1)
                nbr.set_pred(cur_vertex)
                vertex_queue.enqueue(nbr)
        cur_vertex.set_color('black')