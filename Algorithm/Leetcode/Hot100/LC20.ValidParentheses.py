from typing import List

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
解题思路：栈
1. 如果是左半边括号，就压入栈中；
2. 如果是右半边括号：
    * 如果栈为空，说明没有匹配的左半边，返回False；
    * 如果栈 pop 出的元素不是当前字符匹配的左半边括号，就返回False。
3. 在结束的时候，如果栈为空就返回True，否则就是False。
"""


class Solution:
    def isValid(self, s: str) -> bool:
        mapping: dict[str, str] = {')': '(', ']': '[', '}': '{'}
        stack: List[str] = []
        for p in s:
            if p in mapping.values():
                stack.append(p)
            else:
                if not stack:
                    return False
                if mapping[p] != stack.pop():
                    return False
        return True if not stack else False
