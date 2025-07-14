from typing import List

"""
给定一个字符串 s ，返回 s 是否是一个 有效数字。

例如，下面的都是有效数字："2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93",
 "-123.456e789"，而接下来的不是："abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"。
"""
class Solution:
    def isNumber(self, s: str) -> bool:
        # 把E转化成e
        s = s.lower()
        # 按e进行分割，如果没有e就是一整个数字；如果有个e就会多个
        digits: List[str] = s.split('e')
        if len(digits) > 2:
            return False
        if len(digits) == 1:
            return self.isValidNumber(s)
        # 此时说明e前后只有两个数字
        # 判断一下前者是否为整数/浮点数，后者是否是整数
        if self.isValidNumber(digits[0]):
            if self.isValidNumber(digits[1]) and '.' not in digits[1]:
                return True
        return False

    # 这个方法用来判断e或者E前后两部分数字是否是有效
    def isValidNumber(self, s: str) -> bool:
        # 这是为了防止e前或后没有数字的情况
        if s == '':
            return False
        is_float: bool = False  # 小数位，确保只出现一次小数点
        has_flag: bool = False  # 符号位，确保只出现一次符号位
        for d in s:
            if d.islower() or d.isupper():
                return False
            elif d == '+' or d == '-':
                if not has_flag:
                    has_flag = True
                else:
                    # 这种情况是符号出现了多次，或者在数字后出现符号
                    return False
            elif d == '.':
                if not is_float:
                    is_float = True
                else:
                    # 这种情况是出现了多次小数点
                    return False
            else:
                # 匹配到了数字，那就无事发生
                continue
        # 最后上一个保险，如果能强转成float数，说明就没问题
        try:
            float(s)
        except ValueError:
            return False
        return True