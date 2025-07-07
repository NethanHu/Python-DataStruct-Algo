from Graph.DFS import DFSGraph, DFSVertex


def legal_coord(x: int, board_size: int) -> bool:
    return 0 <= x < board_size

def pos_to_node_id(row: int, col: int, board_size: int) -> int:
    return row * board_size + col

def node_id_to_pos(node_id: int, board_size: int) -> tuple[int, int]:
    row = node_id // board_size
    col = node_id % board_size
    return row, col

def gen_legal_moves(x: int, y: int, board_size: int) -> list[tuple[int, int]]:
    move_offsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                    (1, -2), (1, 2), (2, -1), (2, 1)]
    new_moves = []
    for m in move_offsets:
        new_x = x + m[0]
        new_y = y + m[1]
        if legal_coord(new_x, board_size) and legal_coord(new_y, board_size):
            new_moves.append((new_x, new_y))
    return new_moves

# 生成的骑士周游图是一个洗漱图，棋盘上每一个位置对应一个节点，每个节点与骑士可以走到的位置相连
# 8*8的棋盘可以生成336条边
def knight_graph(board_size: int) -> DFSGraph:
    kt_graph = DFSGraph()
    for row in range(board_size):
        for col in range(board_size):
            node_id = pos_to_node_id(row, col, board_size)
            new_pos = gen_legal_moves(row, col, board_size)
            for n in new_pos:
                pos_id = pos_to_node_id(n[0], n[1], board_size)
                kt_graph.add_edge(node_id, pos_id)
    return kt_graph

# 启发式算法，利用先验知识来改进算法性能
# 在这里，这种算法称为Warndorff算法，目的是优先占住边角位置
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

def knight_tour(n: int, path: list[DFSVertex], u: DFSVertex, limit: int) -> bool:
    u.set_color('grey') # 灰色是标记出来已经走过的
    path.append(u)
    if n < limit:
        # 调用启发式算法，从边角开始搜寻，可以大大减少递归时间
        nbr_list: list[DFSVertex] = order_by_available(u)
        i = 0
        done = False
        while i < len(nbr_list) and not done:
            if nbr_list[i].get_color() == 'white':
                done = knight_tour(n + 1, path, nbr_list[i], limit)
            i += 1
        if not done:
            path.pop()
            u.set_color('white') # white是标记出来未走过的节点
    else:
        done = True
    return done

if __name__ == "__main__":
    BOARD_SIZE = 8
    print(f"正在为 {BOARD_SIZE}x{BOARD_SIZE} 的棋盘寻找骑士周游路径...")
    knight_graph_obj = knight_graph(BOARD_SIZE)
    path = []
    start_pos = (1, 1)
    start_node_id = pos_to_node_id(start_pos[0], start_pos[1], BOARD_SIZE)
    start_vertex = knight_graph_obj.get_vertex(start_node_id)
    total_squares = BOARD_SIZE * BOARD_SIZE

    path_found = knight_tour(1, path, start_vertex, total_squares)

    print("-" * 30)
    if path_found:
        print("成功找到一条完整的骑士周游路径！")
        print("路径如下 (行列坐标):")
        output_path = [str(node_id_to_pos(v.get_id(), BOARD_SIZE)) for v in path]
        print(" -> ".join(output_path))
    else:
        print(f"未能在从 {start_pos} 出发的情况下找到一条完整的路径。")