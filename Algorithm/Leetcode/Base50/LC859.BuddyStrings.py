from collections import Counter

"""
给你两个字符串 s 和 goal ，只要我们可以通过交换 s 中的两个字母得到与 goal 相等的结果，就返回 true ；否则返回 false 。

交换字母的定义是：取两个下标 i 和 j （下标从 0 开始）且满足 i != j ，接着交换 s[i] 和 s[j] 处的字符。

例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad" 。
"""
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if len(s) == 1:
            return False
        # 如果s和goal都只由一个字母构成，返回True
        if len(set(s)) == 1 and s == goal:
            return True
        s_map: dict[str, int] = Counter(s)
        g_map: dict[str, int] = Counter(goal)
        # 只有长度>=2，长度相同，词频相同才可以继续进一步判断
        if s_map == g_map:
            # 要么就是差异仅为2，那么交换这两个字符即可
            if self.getDiff(s, goal) == 2:
                return True
            # 要么差异为0，但是其中会有字母出现次数在2次及以上
            # 那么交换这两个相同的字母也能得到正确结果
            if self.getDiff(s, goal) == 0:
                for v in s_map.values():
                    if v >= 2:
                        return True
        return False

    def getDiff(self, s1: str, s2: str) -> int:
        diff: int = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1
        return diff
