"""
在无限的平面上，机器人最初位于 (0, 0) 处，面朝北方。注意:

北方向 是y轴的正方向。
南方向 是y轴的负方向。
东方向 是x轴的正方向。
西方向 是x轴的负方向。
机器人可以接受下列三条指令之一：

"G"：直走 1 个单位
"L"：左转 90 度
"R"：右转 90 度
机器人按顺序执行指令 instructions，并一直重复它们。

只有在平面中存在环使得机器人永远无法离开时，返回 true。否则，返回 false。
"""
import math
from typing import List


class Solution:
    """
    从数学角度去思考这个问题，我们可以完全不用考虑一段指令中指令的先后。
    我们只要考虑经过这段指令之后，在终点位置时的「坐标」和「朝向」；
    这样，在新的点做出一样的指令，相当于把当时的朝向作为北方，然后继续复制之前的运动轨迹。
    我们可以比较容易得出结论：
    1. 当运动之后左边无变化，不管朝向是哪里，下一次还是会回到原点
    1. 当运动之后坐标发生了变化，且最终还是朝北的话，那么永远不可能回到原点
    2. 当运动之后坐标变化，且最终朝向是南的话，经过一轮就可以原路返回
    3. 当运动之后坐标变化，且最终朝向是东、西的话，经过四轮就可以原路返回
    """
    def isRobotBounded(self, instructions: str) -> bool:
        state: dict[str, List[int]] = {
            'pos': [0, 0], 'dir': [0, 1]
        }
        for ins in list(instructions):
            if ins == 'G':
                state['pos'][0] += state['dir'][0]
                state['pos'][1] += state['dir'][1]
            elif ins == 'L':
                # 一个向量 (dx, dy) 左转90度的结果是 (-dy, dx)
                state['dir'][0], state['dir'][1] = -state['dir'][1], state['dir'][0]
            elif ins == 'R':
                # 一个向量 (dx, dy) 右转90度的结果是 (dy, -dx)
                state['dir'][0], state['dir'][1] = state['dir'][1], -state['dir'][0]
        if state['pos'] == [0, 0]:
            return True
        return False if state['dir'] == [0, 1] else True

if __name__ == "__main__":
    s = Solution()
    print(s.isRobotBounded("GLGLGGLGL"))