from typing import List

"""
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
解题思路：拓扑排序+哈希表
1. 我们先理解一下这个问题，如果要完成所有课程的学习，肯定是需要先学习没有依赖的课程（或者依赖少的），那必然得需要有一个入口（零依赖的课程），否则会造成循环依赖。
    * 我们可以试试看，如果这几节课程都存在着依赖关系，那么走一遍就会发现会造成死结出不来；
    * 因此能学的必要条件是：必须要有零依赖的课程。
2. 我们设立一个哈希表，key是课程数字；value是一个set，其中包含着所有依赖的课程。这个哈希表可以通过遍历prerequisites获得。
3. 我们遍历哈希表并设置循环条件：
    * 当哈希表 depend 中还有元素的时候，就继续循环。每次给 depend 做一个快照，我们继续操作；
    * 从 depend 中获得零依赖的课程加入列表，这是我们这一次需要「学习」的课程；反之，如果depend中还有课程，但是已经没有零依赖的课程了，说明肯定不能学习完所有课程；
    * 我们遍历零依赖的所有课程，把他们「学习」了，并且在所有其他课程的依赖项中把它删去。最后在depend中把这门课删除即可，这样depend才会越来越少直到没有。
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        depend: dict[int, set[int]] = {k: set() for k in range(numCourses)}
        for p in prerequisites:
            course: int = p[0]
            prereq: int = p[1]
            depend[course].add(prereq)
        # 只有每次循环中，有课程不依赖于别的课程才能进一步运行
        while depend:
            zero_dep_courses: List[int] = []
            for k, v in depend.items():
                # 如果有一门课不依赖于别的课程
                if len(v) == 0:
                    # 先准备学这门课，然后把这个依赖项从别的课程中删去
                    zero_dep_courses.append(k)
            # 如果不存在这样一个「不依赖别的课程」的课程，说明必然存在着循环依赖
            if not zero_dep_courses:
                return False

            for course in zero_dep_courses:
                for v in depend.values():
                    v.discard(course)
                del depend[course]

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canFinish(2, [[1, 0]]))
