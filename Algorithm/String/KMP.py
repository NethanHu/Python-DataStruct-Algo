class KMP:

    def build_next(self, patt: str) -> list[int]:
        next: list[int] = [0]
        prefix_len: int = 0
        i: int = 1
        while i < len(patt):
            if patt[prefix_len] == patt[i]:
                prefix_len += 1
                next.append(prefix_len)
                i += 1
            else:
                if prefix_len == 0:
                    next.append(0)
                    i += 1
                else:
                    prefix_len = next[prefix_len - 1]
        return next

    def kmp_search(self, string: str, patt: str) -> int:
        next: list[int] = self.build_next(patt)
        i: int = 0
        j: int = 0
        while i < len(string):
            if string[i] == patt[j]:
                i += 1
                j += 1
            elif j > 0:
                j = next[j - 1]
            else:
                i += 1

            if j == len(patt):
                return i - j
        return -1




if __name__ == '__main__':
    kmp = KMP()
    pattern = 'AABAAF'
    string = 'AABAABAAF'
    next = kmp.build_next(pattern)
    print(kmp.kmp_search(string, pattern))
