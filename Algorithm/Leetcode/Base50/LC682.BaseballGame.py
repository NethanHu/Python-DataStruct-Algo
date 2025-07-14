from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores: list[int] = []
        for ch in operations:
            if ch == 'C':
                scores.pop()
            elif ch == '+':
                scores.append(scores[-1] + scores[-2])
            elif ch == 'D':
                scores.append(scores[-1] * 2)
            else: # 正负数都在这个情况里面
                scores.append(int(ch))
        return sum(scores)


if __name__ == '__main__':
    s = Solution()
    s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"])
