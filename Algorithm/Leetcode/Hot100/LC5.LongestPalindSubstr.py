"""
给你一个字符串 s，找到 s 中最长的 回文 子串。
解题思路：字符串+中心扩散法
1. 本题的核心思路是，如果我们有了单个字符 a（其实单个字符本身就是回文的），我们只需要判断一下 a 左右两边的字符是否相等，如果是则增加回文串的长度：
    * 我们遍历字符下标 i = 0, 1, ..., size - 1，以遍历到的字符 s[i] 为锚点，初始化 l 和 r，不断扩充 l 和 r 的边界，从而找到最大的回文串长度；
    * 偶数回文串同理，我们再遍历一遍，只是此时 i = 0, 1, ..., size - 2，初始化的 l = i、r = i + 1，然后继续不断扩充 l、r 的边界，记录最长回文串的字符下标；
2. 细节是：我们永远保持 l_bound 是左边的闭区间，r_bound 是右边的开区间，那么此时最长的长度为 r_bound - l_bound；而我们 l、r 边界（开区间）的长度为 r - l - 1；
    * 同样的，找到最大边界之后，l_bound 设置为 i + 1，r_bound 设置为 r。
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        size: int = len(s)
        l_bound = r_bound = 0
        # 对于奇数的回文串，我们判断一次
        for i in range(size):
            l = r = i
            while (l >= 0 and r < size) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > r_bound - l_bound:
                # 左闭右开区间
                l_bound, r_bound = l + 1, r
        # 对于偶数的回文串，我们再遍历一次
        for i in range(size - 1):
            l, r = i, i + 1
            while (l >= 0 and r < size) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > r_bound - l_bound:
                l_bound, r_bound = l + 1, r
        return s[l_bound: r_bound]
