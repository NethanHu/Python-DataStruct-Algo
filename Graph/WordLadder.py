from Graph.BFS import BFSVertex, bfs, BFSGraph
from LinearStructure.Stack import Stack


def build_graph(word_file='fourletterwords.txt') -> BFSGraph:
    d = {}
    g = BFSGraph()
    w_file = open(word_file, 'r')
    for line in w_file:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    for bucket in d.keys():
        for word_1 in d[bucket]:
            for word_2 in d[bucket]:
                if word_1 != word_2:
                    g.add_edge(word_1, word_2)
    return g

def traverse(y: BFSVertex):
    x = y
    s = Stack()
    while x.get_pred():
        s.push(x.get_id())
        x = x.get_pred()
    s.push(x.get_id())
    print(s)

bfs_graph: BFSGraph = build_graph()
bfs(bfs_graph, bfs_graph.get_vertex('FOOL'))
traverse(bfs_graph.get_vertex('SAGE'))
