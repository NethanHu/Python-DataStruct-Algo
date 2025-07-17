"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
思路分析：我们使用滑动窗口，使用一个队列，队列中只能包含不重复字符。
然后不断把新字符从右append，如果有重复就不断从左pop，直到不包含重复。这样遍历到字符串结尾。
"""
from collections import Counter
from typing import Deque, List

from cytoolz.itertoolz import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len: int = 0
        queue: Deque[str] = deque()
        for c in s:
            queue.append(c)
            while not self.isUnique(queue):
                queue.popleft()
            if len(queue) > max_len:
                max_len = len(queue)
        return max_len

    # def isUnique(self, queue: Deque[str]) -> bool:
    #     # 使用 Counter(queue).most_common(1) 来统计queue中最常出现的元素是否出现次数>=2次
    #     # 用法：Counter('abracadabra').most_common(3)
    #     # 返回 [('a', 5), ('b', 2), ('r', 2)]
    #     most_e: List[tuple[str, int]] = Counter(queue).most_common(1)
    #     return most_e[0][1] == 1

    # 或者直接使用set去重，判断一下去重之后与原queue长度是否一致
    def isUnique(self, queue: Deque[str]) -> bool:
        return len(set(queue)) == len(queue)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('abcabcbb'))