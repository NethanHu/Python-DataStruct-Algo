tr = [None, {'w': 2, 'v': 3}, {'w': 3, 'v': 4}, {'w': 4, 'v': 8},
      {'w': 5, 'v': 8}, {'w': 9, 'v': 10}]

max_w = 20

# initialization of the dp_table
dp = {
    (i, w): 0
    for i in range(len(tr))
    for w in range(max_w + 1)
}

# 看待动态规划问题，永远不要从中间切入，要从每一循环的开始进行思考
# 正是有了循环之前的结果，才会有中间的结果，他们是有依赖关系的
for i in range(1, len(tr)):
    for w in range(1, max_w + 1):
        if tr[i]['w'] > w: # 当前选择的宝物重量超过了容量
            dp[(i, w)] = dp[(i - 1, w)] # 只能选择退回去选择更轻的那个宝物
        else: # 如果当前选择的宝物重量放得下
            # 我们进行抉择，要么还是选择上一个宝物；
            # 要么就选择装新的宝物，然后剩余容量可以装的东西选择之前的最优解
            dp[(i, w)] = max(
                dp[(i - 1, w)], tr[i]['v'] + dp[(i - 1, w - tr[i]['w'])]
            )

print('Best treasure value is:', dp[(len(tr) - 1, max_w)])