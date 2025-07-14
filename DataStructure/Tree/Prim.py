from pythonds import PriorityQueue, Vertex, Graph

def prim(g: Graph, start: Vertex):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in g])
    while not pq.isEmpty():
        cur_vert = pq.delMin()
        for next_vert in cur_vert.getConnections():
            # 从当前节点出发，逐个检验到邻接节点的权重
            new_cost = cur_vert.getWeight(next_vert)
            # 如果邻接节点是"安全边"，并且小于邻接节点原有最小权重代价dist，就更新邻接节点
            if next_vert in pq and new_cost < next_vert.getDistance():
                next_vert.setPred(cur_vert)
                next_vert.setDistance(new_cost)
                pq.decreaseKey(next_vert, new_cost)