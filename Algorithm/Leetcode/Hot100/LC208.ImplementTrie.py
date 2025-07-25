class Node:
    # slot魔法属性能够手动控制Node中只能含有这两个属性，不能额外添加，用于优化内存
    __slots__ = 'son', 'end'

    def __init__(self):
        self.son = {}
        self.end = False


"""
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补全和拼写检查。
请你实现 Trie 类：
Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
解题思路：设计+多叉树+哈希表
1. 参考二叉树，假设我们的字母表中就只有a、b两个字母，那么我们可以使用二叉树来记录单词，并且有以下结论：
    * 我们要 insert abb 这个单词，我们碰到a的时候往左走，碰到b的时候往右走，那么 abb 保存下来的树结构就是从root出发，「左-右-右」的树结构，且在最后一个节点属性end=True；
    * 我们使用 search 方法寻找 abb，那么也是从root出发，遵循“找a往左走，找b往右走”的方法，依次从每个节点的属性son中找路径：
        - 如果存在着一条路「左-右-右」，且最后一个节点end=True，说明添加过一个单词为abb，返回为True。
    * 如果我们使用 startsWith 方法搜索 aa，我们只需要判断有没有「左-左」这个分支即可，如果没有就返回False。
2. 由于字母表中有26个字符，我们使用26叉树（不要被26叉吓到，用哈希表即可完事）：
    * 每个节点「有且只有」son和end两个属性，son中的key保存着从这个节点出发，可以接下去走的路径，而end保存着有没有在这个节点停止的单词；
    * 结合二叉树的思路，我们共用一个find方法，如果从son找不到接下去路径要走的key的时候返回0，能接着走但不是end就返回1，到这个点停下就是2；
    * search、startsWith 方法就根据find的返回值来返回输出即可。
"""


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur: Node = self.root
        for c in word:
            # 如果当前字符c不在当前遍历到的节点的key中
            if c not in cur.son:
                cur.son[c] = Node()
            cur = cur.son[c]
        cur.end = True

    def find(self, word: str) -> int:
        cur: Node = self.root
        for c in word:
            if c not in cur.son:
                return 0
            cur = cur.son[c]
        return 2 if cur.end else 1

    def search(self, word: str) -> bool:
        return self.find(word) == 2

    def startsWith(self, prefix: str) -> bool:
        # startsWith 包含着search的True结果，只要find的不是得到0就是True
        return self.find(prefix) != 0

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
