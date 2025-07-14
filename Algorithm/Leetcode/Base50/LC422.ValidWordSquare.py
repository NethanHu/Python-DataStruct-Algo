from typing import List

"""
给你一个字符串数组 words，如果它能形成一个有效的 单词方块 ，则返回 true 。

有效的单词方块是指此由字符串数组组成的文字方块的 第 k 行 和 第 k 列所显示的字符串完全相同，其中 0 <= k < max(numRows, numColumns) 
"""
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        size: int = len(words)
        # 先对字符串进行填补操作
        for i, s in enumerate(words):
            if len(s) < size:
                words[i] = s.ljust(size, '*')
        # 接下来遍历行，提取字母，判断是否为对称矩阵
        for r in range(size):
            for c in range(size):
                if words[r][c] != words[c][r]:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.validWordSquare(["abcd", "bnrt", "crm", "dt"]))