from collections import deque
from typing import List, Deque

"""
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。
如果气温在这之后都不会升高，请在该位置用 0 来代替。
解题思路：单调递增栈，时间复杂度为O(n)
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size: int = len(temperatures)
        if size == 1:
            return [0]
        # 对结果序列进行初始化，0代表着右边已经没有比自己更大的元素
        ans: List[int] = [0] * size
        # 我们用二元组来记录 (下标i, 温度t)
        stack: Deque[(int, int)] = deque()
        for i, t in enumerate(temperatures):
            if len(stack) == 0 or t <= stack[-1][1]:
                stack.append((i, t))
            else:
                while len(stack) > 0:
                    # 碰到相等的时候不算“大于”，因此我们直接退出
                    if t > stack[-1][1]:
                        idx, _ = stack.pop()
                        ans[idx] = i - idx
                    else:
                        break
                stack.append((i, t))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
