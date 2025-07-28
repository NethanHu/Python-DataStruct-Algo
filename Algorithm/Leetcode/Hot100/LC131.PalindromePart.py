from typing import List, Deque

"""
给你一个字符串 s，请你将 s 分割成一些 子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
解题思路：DFS+回溯
1. 求一个字符串是否为回文并不难，只需要判断一个逻辑 s == s[::-1]，难就难在如何对一个字符串做完整且有穷的分割；
2. 我们设计一个递归方法DFS，只需要传入一个参数i，代表着这个方法继续会递归处理s[i:]的结果，i前面的我们不需要再考虑，因为这是上层方法考虑的：
    * 递归的退出条件是 i == n，因为此时的切片 s[i:] 不会再有字符，所以此时算是一个完整的分割过程，我们把临时答案填充进ans中；
    * 假设i在字符串的中间，此时我们可以对 s[i:] 进行 n - 1 - i 次分割，每次选择往后切一刀得到长度1的子串、2的子串等等，因此for循环得到子串长度j；
    * 我们得到的子串为 s[i: j + 1]，如果这个子串是回文，那么就把它加入到临时答案中，并且此时递归将从切口后的新的起点开始，即backtrack(j + 1)；
    * 在递归完新的起点之后，我们进行回溯，把当前找到的「是回文的」子串弹出，再找下一个合适的答案。
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n: int = len(s)
        ans: List[List[str]] = []
        # 用来存放临时答案
        cur_ans: List[str] = []

        def backtrack(i: int) -> None:
            if i == n:
                ans.append(cur_ans[:])
                return
            for j in range(i, n):
                sub_s: str = s[i: j + 1]
                if self.isPalindrome(sub_s):
                    cur_ans.append(sub_s)
                    backtrack(j + 1)
                    cur_ans.pop()

        backtrack(0)
        return ans

    def isPalindrome(self, s: str) -> bool:
        return True if s == s[::-1] else False


if __name__ == '__main__':
    s = Solution()
    print(s.partition('aab'))
