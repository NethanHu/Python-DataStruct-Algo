from typing import List

"""
给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。例如，字符串 "ababcc" 能够被分为 ["abab", "cc"]，但类似 ["aba", "bcc"] 或 ["ab", "ab", "cc"] 的划分是非法的。
注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
返回一个表示每个字符串片段的长度的列表。
解题思路：贪心算法
1. 我们想一想，如果一个字符串能够分割成几份，每一份中的字母不会在别的地方出现，那么说明某一份中的几个字母，它们出现的终点都是「有穷」的，会停在一个地方；
    * 举个例子，比如字符串 s = ababcbacadefegdehijhklij，我们经过统计，会发现 a 最后出现在第8位，b 最后出现在第5位，c 最后出现在第7位；
    * 那么我们有理由去在第8位截断，因为 a、b、c 都不会在后面出现过。前提是也没有其他字符在 a、b、c 中出现过；
    * 说明我们先要统计一下每个字符最后出现的位置在哪里，这样可以做成一个大边界的上限。
2. 我们再从头遍历一遍字符串，由于当前区间必须包含所有字符 s[i]，所以用 last[s[i]] 更新区间右端点 end 的最大值；
    * 如果在一个区间中遍历到的所有字符 s[i] 它们的上限被确定死了，即通过 last 去查找发现它们不再后面再出现过，那说明可以把 end 设置在这里，输出一个 partition；
    * 最后更新答案 end - start + 1，并把 start 设置为新的起点 i + 1。
"""


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last: dict[str, int] = {c: i for i, c in enumerate(s)}
        ans: List[int] = []
        start = end = 0
        for i, c in enumerate(s):
            # 如果说有几个字母「群居」在一个限定区域内，那么他们必然不可能在后面出现，end 会在一个分界线的地方停下
            end = max(end, last[c])
            if end == i:
                ans.append(end - start + 1)
                start = i + 1
        return ans
