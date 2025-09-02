from typing import List

"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
解题思路：回溯
这道题目可以感受到回溯的本质，先下潜到最深（全都选），到一层层上浮（部分选），最后是一个也不选。
1. 我们定义递归函数：
    * cur_str 是当前拼接的字符串，由于我们不是共享内存，因此add之后回溯不需要pop；
    * left 是左括号的个数，我们需要遵循规则：左括号的个数必须大于等于右括号个数，最终左括号右括号个数都得等于n；
    * right 是右括号的个数；
    * 递归退出条件是当前拼接的 cur_str 长度等于 2n，此时把 cur_str 添加到 ans 中。
2. 如果 left 小于n，就可以一直选择左括号，我们递归这个函数，递归的深度决定了选择了多少左括号，从而回溯的时候可以逐渐少选，形成多样性；
3. 左括号选好了，只要右括号的个数依然小于等于左括号个数，那么可以一直选择右括号。右括号可以全选（递归最深），或者是部分选（回溯）。
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans: List[str] = []

        def backtrack(cur_str: str, left: int, right: int):
            # 当cur_len的长度等于两倍n的时候说明生成了一个合理的括号组合
            if len(cur_str) == 2 * n:
                ans.append(cur_str)
                return
            # 这里随着回溯，第一层程序栈选择左括号的个数'(((' -> '((' -> '(' -> ''（当然这种不合法，因为右括号的数量必须小于等于左括号个数）
            if left < n:
                backtrack(cur_str + '(', left + 1, right)
            # 在左括号做好了选择之后，右括号可以选择 <= 左括号的个数
            if right < left:
                backtrack(cur_str + ')', left, right + 1)

        backtrack('', 0, 0)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
