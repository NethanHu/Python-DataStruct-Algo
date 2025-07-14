from collections import defaultdict
from typing import List


"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 这里是把异位词排序后的字符串作为key，属于异位词的单词加入到List中
        sorted_list: dict[str, List[str]] = defaultdict(list)
        for word in strs:
            _str: str = ''.join(sorted(word))
            sorted_list[_str].append(word)
        ans_list: List[List[str]] = []
        for v in sorted_list.values():
            ans_list.append(v)
        return ans_list
