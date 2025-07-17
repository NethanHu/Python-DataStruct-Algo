
"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
核心思路：哈希表+滑动窗口
1. 我们将目标的t字符串变成一个dict，便于我们比较；同时初始化一个window作为我们统计滑动窗口内字符数的数据结构
2. 如何判断window中所有字符都和need中匹配上呢？我们设置一个key_matched，如果window中一个key对应的value==need中该key的value，就将其+1；
   那么当key_matched==len(need.keys())的时候，说明所有字符都匹配上了
3. 我们遍历的思路如下：
    * 左指针设置为l，右指针获取为r、右指针的字符为c；当遍历到c的时候，我们在window中加入这个元素；
    * 此时右指针走了一步。在左指针走之前，我们毕竟要抛弃掉左指针的元素了，在走之前我们看看如果这个字符抛弃了，是否会导致window中这个key的value小于need中，
      如果小于，那说明抛弃掉l指向的元素之后，我们就无法匹配need了。所以仅当window[s[l]] > need[s[l]]的时候才可以走左指针，进行循环；
    * 左右指针都走完了之后，我们匹配一下是否key_matched == len(need)，然后更新最小能覆盖字符串。
4. 可能有一个问题：左指针走了之后，抛弃了当前元素，可能会导致key_matched变小啊，为什么不会让key_matched-=1。
   这个问题很简单，我们维护的key_matched只会增加不会减少，就是说window[s[l]] >= need[s[l]]的时候都是key_matched，
   而我们只会在window[s[l]] > need[s[l]]的时候去移动左指针，此时就算移动了，也最多是达到window[s[l]] == need[s[l]]而已。
"""
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        size: int = len(s)
        need: dict[str, int] = Counter(t)
        window: dict[str, int] = defaultdict(int)
        l: int = 0
        key_matched: int = 0
        min_len = float('inf')
        ans: str = ''

        for r, c in enumerate(s):
            window[c] += 1
            if window[c] == need[c]:
                key_matched += 1

            while l < size and window[s[l]] > need[s[l]]:
                window[s[l]] -= 1
                l += 1

            if key_matched == len(need) and r - l + 1 < min_len:
                ans = s[l:r + 1]
                min_len = r - l + 1

        return ans
