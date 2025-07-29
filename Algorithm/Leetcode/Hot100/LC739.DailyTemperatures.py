from collections import deque
from typing import List, Deque

"""
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。
如果气温在这之后都不会升高，请在该位置用 0 来代替。
解题思路：单调栈，时间复杂度为O(n)
1. 我们维护一个非严格单调递减栈，从 0 到倒数第一个元素，温度是逐渐下降的。同时我们的 stack 存的是一个二元组，即当天序号 i 和温度 t；
    * 同时初始化我们的 ans，初始全部为 0，如果后面没有比自己更大的元素的时候，就返回为 0，符合题目要求。
2. 我们遍历 temperatures 这个数组，有以下几种情况：
    * 如果 stack 为空，或者栈顶元素的温度 >= 当前温度，此时符合递减栈定义，直接把当前二元组 append 进去；
    * 如果栈顶元素的温度 < 当前温度，我们此时可以给这些往日的温度赋值了，因为我们有此时这一天的序号 i，和 pop 出来的往日序号 idx，
      让 ans[idx] 等于 i - idx 就是设置在第几天后温度升高；
    * 这样是正确的，因为我们的栈是非严格「递减」，我们回溯历史只会找到逐渐增大的温度，可以一直找到从现在开始比当前 t 更小的温度。
    * 最后不管如何，都要把当天的 (i, t) 再次加入到栈中，以便后续比较。
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
                while stack:
                    # 碰到相等的时候不算“大于”，因此我们直接退出
                    if t > stack[-1][1]:
                        idx, _ = stack.pop()
                        # 被弹出的元素记录，i是当前比较元素，idx是在栈里面的元素
                        ans[idx] = i - idx
                    else:
                        break
                stack.append((i, t))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
