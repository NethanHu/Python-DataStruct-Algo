from typing import List

"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
解题思路：递归+回溯
1. 本题看到这种「完全找路径、匹配模式」我们第一时间想到递归方法，具体而言递归的思路如下：
    * 我们在递归参数中传入一个维护的cur_list，用来维护当前我们的一个排列组合；
    * 我们在外部维护一个num_set，由于题目表示每个整数都不一样，那么我们可以放心使用set不会去重，同时拥有着更快的add、remove速度；
    * 递归中我们每次从for循环中获取到一个数字，当我们选定这个数字之后，我们将其从set中移除，然后在cur_list加入这个数字；
    * 由于for循环的存在，在每个程序栈中都会稳定遍历所有的数字组合；
    * 最后在回溯的时候我们做两件事：
        - 第一是从cur_list中返还我们选中的数字，第二是在num_set中补充回我们刚刚锁定的那个数字。
2. 有很多细节问题：
    * Python 中的list是动态的，最后往ans添加我们的结果cur_list时，一定是深拷贝，即ans.append(cur_list[:])，否则会造成错乱；
    * Python 的set在循环中是可以动态修改的（类似于Java的Concurrent HashMap），这就导致循环中对set的写入/修改会打乱我们的逻辑：
        - 因此在每一个程序栈中，我们手动给当前的set打一个快照，即使用list：for n in list(num_set)。
    * 我们在递归结束之后一定要进行回溯，如果每次传入的都是一个副本，那么这一举动不必要，但是对于我们内存优化（共享一个set的时候）必须进行回溯操作。
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        num_set: set[int] = set(nums)
        ans: List[List[int]] = []

        def recursion(cur_list: List[int]):
            if len(num_set) == 0:
                ans.append(cur_list[:])
                return
            for n in list(num_set):
                # 选择了这个数字之后就先移除
                num_set.remove(n)
                cur_list.append(n)
                recursion(cur_list)
                cur_list.pop()
                # 递归结束之后把这个数字补回去
                num_set.add(n)

        recursion([])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
