
class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.left_child: TreeNode | None = left
        self.right_child: TreeNode | None = right
        self.parent: TreeNode | None = parent

    # 我们在这里使用中序遍历的迭代方法
    # 包含yield的普通函数被称为生成器，可以生成迭代器；每次yield只返回一个值，直到下一次迭代
    def __iter__(self):
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.has_right_child():
                for elem in self.right_child:
                    yield elem

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self is self.parent.left_child

    def is_right_child(self):
        return self.parent and self is self.parent.right_child

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left_child or self.right_child)

    def has_any_children(self):
        return self.left_child or self.right_child

    def has_both_children(self):
        return self.left_child and self.right_child

    def replace_node_data(self, key, value, left, right):
        self.key = key
        self.payload = value
        self.left_child: TreeNode | None = left
        self.right_child: TreeNode | None = right
        # 因为当前对象的内容修改之后，哈希值会出现不一样，如果使用 == 或者 is 操作符会导致false
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def find_min(self):
        cur_node = self
        while cur_node.has_left_child():
            cur_node = cur_node.left_child
        return cur_node

    def find_successor(self):
        suc = None
        if self.has_right_child():
            # 1. 如果有右子树，后继就是右子树中的最小值
            suc = self.right_child.find_min()
        else:
            # 2. 如果没有右子树，需要向上寻找祖先
            if self.parent:
                current = self
                # 只要当前节点还是父节点的右孩子，就继续向上
                while current.parent and current.is_right_child():
                    current = current.parent
                # 循环结束时，current.parent 就是后继
                suc = current.parent
        return suc

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        # 后继节点不可能有左孩子，所以只需要检查右孩子
        elif self.has_right_child():
            # 将孙子节点的 parent 指针指向祖父节点
            self.right_child.parent = self.parent # ★★★ 补上这一步
            if self.is_left_child():
                self.parent.left_child = self.right_child
            else:
                self.parent.right_child = self.right_child


class BinarySearchTree:
    def __init__(self):
        self.root: TreeNode | None = None
        self.size = 0

    def length(self) -> int:
        return self.size

    def __len__(self) -> int:
        return self.size

    # 实现__iter__方法就可以生成迭代器，比如for key in my_tree
    def __iter__(self):
        return self.root.__iter__()

    # __setitem__支持使用类似于my_tree['XX']的方式进行赋值
    def __setitem__(self, key, value):
        self.put(key, value)

    # __getitem__支持类似于my_tree['XX']的方式进行得到对应payload
    def __getitem__(self, item):
        return self.get(item)

    # __contains__实现了归属判断，比如说判断一下key是否在BST中，例如 3 in my_tree
    def __contains__(self, item):
        return True if self._get(item, self.root) else False

    # __delitem__实现了删除的功能，可以支持类似于del my_tree['XX']这样的实现形式
    def __delitem__(self, key):
        self.delete(key)

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, cur_node: TreeNode):
        # 如果说key比当前的node小，那么_put到左子树
        if key < cur_node.key:
            if cur_node.has_left_child():
                # 如果左子树存在东西，那么就在左子树继续递归调用_put
                self._put(key, val, cur_node.left_child)
            else:
                # 如果左子树不存在东西，那么就直接把当前节点挂载为左子节点
                cur_node.left_child = TreeNode(key, val, parent=cur_node)
        # 右边同理
        else:
            if cur_node.has_right_child():
                self._put(key, val, cur_node.right_child)
            else:
                cur_node.right_child = TreeNode(key, val, parent=cur_node)

    def get(self, key):
        if self.root:
            # 如果根节点存在，从根节点开始递归查找key
            res = self._get(key, self.root)
            # 如果 res 最后找到了，就返回里面的 payload
            return res.payload if res else None
        else:
            return None


    def _get(self, key, cur_node: TreeNode):
        # 遍历一遍从顶到底都没有，那么就返回None
        if not cur_node:
            return None
        elif cur_node.key == key:
            return cur_node
        # 如果发现要找的key小于当前节点的key，就往左边递归调用
        elif key < cur_node.key:
            return self._get(key, cur_node.left_child)
        # 右边同理
        else:
            return self._get(key, cur_node.right_child)

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in the tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in the tree')


    def remove(self, cur_node: TreeNode):
        # 最简单的情况，当前节点就是叶节点，直接删除自己即可
        if cur_node.is_leaf():
            if cur_node.is_left_child():
                cur_node.parent.left_child = None
            else:
                cur_node.parent.right_child = None
        # 稍微复杂的情况，当前节点有且只有一个子节点
        elif cur_node.has_both_children() is False:
            child = cur_node.left_child if cur_node.has_left_child() else cur_node.right_child
            # 如果要删除的是根节点
            if cur_node.is_root():
                self.root = child
                if child: # 如果树不是变空
                    child.parent = None
            # 如果要删除的是内部节点
            else:
                if cur_node.is_left_child():
                    cur_node.parent.left_child = child
                else:
                    cur_node.parent.right_child = child
                if child:
                    child.parent = cur_node.parent
        else:
            # 这种情况最复杂，需要找到一个合适的节点来替换被删的节点
            suc = cur_node.find_successor()
            suc.splice_out()
            cur_node.key = suc.key
            cur_node.payload = suc.payload
