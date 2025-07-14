from collections import defaultdict
from typing import List

"""
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。

每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

注意，一开始你手头没有任何零钱。
给你一个整数数组 bills ，其中 bills[i] 是第 i 位顾客付的账。如果你能给每位顾客正确找零，返回 true ，否则返回 false 。
"""


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 硬编码所有状态：收到5美元就加入列表
        # 收到10美元就从列表中remove一个5美元
        # 收到20美元就从列表中remove一个10+5或者5+5+5
        changes: dict[int, int] = defaultdict(int)
        for money in bills:
            if money == 5:
                changes[5] += 1
            elif money == 10:
                changes[10] += 1
                if not self.makeChange(changes, money):
                    return False
            elif money == 20:
                changes[20] += 1
                if not self.makeChange(changes, money):
                    return False
        return True

    def makeChange(self, changes: dict[int, int], money: int):
        if money == 10:
            if changes[5] == 0:
                return False
            else:
                changes[5] -= 1
                return True
        elif money == 20:
            # 优先找10美元，因为5美元是更小的基础单位
            if changes[10] > 0 and changes[5] > 0:
                changes[10] -= 1
                changes[5] -= 1
                return True
            if changes[10] == 0 and changes[5] >= 3:
                changes[5] -= 3
                return True
            else:
                return False


if __name__ == '__main__':
    s = Solution()
    s.lemonadeChange([5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5])
