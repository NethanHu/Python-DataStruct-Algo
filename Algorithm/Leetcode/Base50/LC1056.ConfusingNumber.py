from typing import List

"""
给定一个数字 N，当它满足以下条件的时候返回 true：
原数字旋转 180° 以后可以得到新的数字。
如 0, 1, 6, 8, 9 旋转 180° 以后，得到了新的数字 0, 1, 9, 8, 6 。
2, 3, 4, 5, 7 旋转 180° 后，得到的不是数字。
易混淆数 (confusing number) 在旋转180°以后，可以得到和原来不同的数，且新数字的每一位都是有效的。
"""
class Solution:
    def confusingNumber(self, n: int) -> bool:
        # 我们把所有的digit变成str，这样方便遍历和比较
        origin: List[str] = list(str(n))
        rotated: List[str] = []
        for i in range(len(origin) - 1, -1, -1):
            rotated.append(self.rotate(origin[i]))
        # 如果所有数字都有效
        if '#' not in rotated:
            return origin != rotated
        return False


    def rotate(self, n: str) -> str:
        rotate_num: dict[str, str] = {
            '0': '0', '1': '1', '2': '#', '3': '#', '4': '#',
            '5': '#', '6': '9', '7': '#', '8': '8', '9': '6'
        }
        return rotate_num[n]

if __name__ == '__main__':
    s = Solution()
    print(s.confusingNumber(89))  # true
    print(s.confusingNumber(11))  # false