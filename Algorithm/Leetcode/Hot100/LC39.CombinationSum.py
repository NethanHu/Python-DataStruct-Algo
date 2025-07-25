from collections import Counter
from typing import List

"""
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 
对于给定的输入，保证和为 target 的不同组合数少于 150 个。
解题思路：DFS+剪枝
1. 我们使用DFS把这个问题逐渐分解，我们使用两个参数：
    * cur_list 记录搜索路径上所有的数字，然后由于题目不允许有重复的答案，我们使用 Counter 来统计各个数字个数来进行去重；
    * rem 记录选择上个数字之后，距离我们的target还剩多少大小；可以不同rem，直接统计sum(cur_list)，但是会花更多时间。
2. 在每次dfs中，我们会遍历candidates中的数字：
    * 如果n大于rem，如果我们一开始进行了排序，那么n接下去的数字也依然会大于rem（剪枝）；
    * 如果n等于rem，说明选了n之后我们得到了答案，但是为了去重，我们使用Counter进行统计数字出现的个数，只有出现不一样的组合之后才会添加到cnt_dict中；
    * 回溯的时候，就把刚刚选择的数字从 cur_list pop 出来。
3. 最后我们写一个方法，通过cnt_dict中的dict来生成答案。
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cnt_dict: List[dict[int, int]] = []
        # 只有排序之后的元素才可以优化DFS次数
        candidates = sorted(candidates)

        def dfs(cur_list: List[int], rem: int) -> None:
            for n in candidates:
                if n > rem:
                    return
                elif n == rem:
                    cur_list.append(n)
                    # 确认一下这种组合有没有在ans中出现
                    ans_dict: dict[int, int] = Counter(cur_list[:])
                    if ans_dict not in cnt_dict:
                        cnt_dict.append(ans_dict)
                    # 回溯，把刚刚最后一个元素pop出来
                    cur_list.pop()
                    return
                else:
                    cur_list.append(n)
                    dfs(cur_list, rem - n)
                    cur_list.pop()

        dfs([], target)

        # 将dict中的答案转变成ans
        ans_list: List[List[int]] = []
        for d in cnt_dict:
            ans: List[int] = []
            for k, v in d.items():
                for _ in range(v):
                    ans.append(k)
            ans_list.append(ans)

        return ans_list


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))
