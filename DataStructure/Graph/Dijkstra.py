from pythonds.graphs import PriorityQueue, Graph, Vertex

def dijkstra(g: Graph, start: Vertex):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in g])
    while not pq.isEmpty():
        cur_vert: Vertex = pq.delMin()
        for next_vert in cur_vert.getConnections():
            new_dist = cur_vert.getDistance() + cur_vert.getWeight(next_vert)
            if new_dist < next_vert.getDistance():
                next_vert.setDistance(new_dist)
                next_vert.setPred(cur_vert)
                pq.decreaseKey(next_vert, new_dist)


if __name__ == '__main__':
    G = Graph()
    nd_edge = [('u', 'v', 2), ('u', 'w', 5), ('u', 'x', 1),
               ('v', 'x', 2), ('v', 'w', 3), ('x', 'w', 3),
               ('x', 'y', 1), ('w', 'y', 1), ('w', 'z', 5),
               ('y', 'z', 1)]
    for nd in nd_edge:
        G.addEdge(nd[0], nd[1], nd[2])
        G.addEdge(nd[1], nd[0], nd[2])
    start = G.getVertex('u')
    dijkstra(G, start)
    print(G.vertices)
