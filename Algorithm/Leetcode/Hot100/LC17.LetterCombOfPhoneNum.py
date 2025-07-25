from typing import List

"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同，每个数字按照九宫格与英文字母映射）。注意 1 不对应任何字母。
解题思路：字符串+DFS+回溯
1. 我们先制作一个从digit到字母的映射表，之后可以根据digit查询有哪些字母可以遍历；
2. 我们设计DFS思路，每次获取一个idx位置上的digit，根据字母表依次选择字母，结束条件是idx与长度相等的时候退出，把此时制作好的cur_list添加到ans中；
3. 回溯的时候需要把cur_list中刚刚选择的字母弹出，以便可以选择下一个字母。
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans_list: List[str] = []
        num_map: dict[str, List[str]] = {
            '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
        }

        def dfs(idx: int, cur_list: List[str]) -> None:
            digit: str = digits[idx]
            ch_list: List[str] = num_map[digit]
            for ch in ch_list:
                cur_list.append(ch)
                if idx == len(digits) - 1:
                    ans_list.append(''.join(cur_list[:]))
                else:
                    dfs(idx + 1, cur_list)
                cur_list.pop()

        dfs(0, [])

        return ans_list


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))
