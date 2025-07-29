from typing import List

"""
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
示例：输入：s = "3[a2[c]]"，输出："accaccacc"
解题思路：栈+字符串
1. 使用一个 List 来模拟栈，我们把数字、字母和括号都加入到这个栈中。根据遍历到不同的字符，我们有以下判断：
    * 由于我们一次（或者一群）字符只会是数字、数字、字符的交替，即字符就扮演字符的意思，数字就扮演数字的意思，括号就扮演括号的意思，省下了很多条件判断：
    * 如果栈为空或者是左括号，直接加入我们的字符；
    * 如果我们碰到了英文字符，「假设」我们之前也是个英文字符，这个类似于「补充」，那么我们就让它在栈顶的字符串后面添加；
    * 如果我们碰到了数字字符，「假设」我们之前也是个数字字符，这个类似于「补充」，那么我们就让它在栈顶的字符串后面添加；
    * 如果是右括号，我们有以下操作：
        - 依次把括号内的字符串 pop 出来，使用一个 buf 来拼接他们；
        - 如果碰到了左括号，说明字符串已经结束，如果左括号前面是数字，那么再乘上倍率；否则直接再次加入到 stack 中。
    * 最后使用字符串拼接方法返回答案。
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack: List[str] = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if c.isalpha() and stack[-1].isalpha():
                    stack[-1] += c
                elif c.isdigit() and stack[-1].isdigit():
                    stack[-1] += c
                elif c == '[':
                    stack.append(c)
                elif c == ']':
                    buf: str = ''
                    while stack[-1] != '[':
                        buf = stack.pop() + buf
                    # 弹出右半括号
                    stack.pop()
                    if stack[-1].isdigit():
                        buf = buf * int(stack.pop())
                    stack.append(buf)
                else:
                    stack.append(c)
        return ''.join(stack)


if __name__ == '__main__':
    s = Solution()
    print(s.decodeString('3[ab2[cd]]'))
