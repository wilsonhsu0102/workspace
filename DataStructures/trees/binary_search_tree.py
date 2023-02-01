from typing import Optional
from trees.binary_tree import BinaryTreeNode

class BSTNode(BinaryTreeNode):
    """A Binary Search Tree (contains no duplicate).

    Inherits Binary Tree Node.

    Attributes:
        key: Key of the node.
        left: Left child of the node.
        right: Right child of the node.
    """
    left: 'BSTNode'
    right: 'BSTNode'

    def search(self, key: int) -> Optional['BSTNode']:
        if self.key == key:
            return self
        if self.key > key and self.left:
            return self.left.search(key)
        if self.key < key and self.right:
            return self.right.search(key)
        return None

    def insert(self, key: int):
        selfType = type(self) # For subclasses
        if self.key > key:
            if self.left is None:
                self.left = selfType(key)
            else:
                self.left.insert(key)
            return
        elif self.key < key:
            if self.right is None:
                self.right = selfType(key)
            else:
                self.right.insert(key)
        return

    def delete(self, key: int) -> Optional['BSTNode']:
        if self.key == key:
            selfType = type(self)
            if self.left is None and self.right is None:
                return None
            if self.left is None and self.right is not None:
                return self.right
            if self.left is not None and self.right is None:
                return self.left
            # both child not None
            next_key = self.find_next_node().key
            self.right = self.right.delete(next_key)
            new_root = selfType(next_key)
            new_root.left = self.left
            new_root.right = self.right
            self = new_root
        elif self.key > key:
            self.left = self.left.delete(key)
        else:
            self.right = self.right.delete(key)
        return self

    def find_next_node(self) -> Optional['BSTNode']:
        if self.right is None:
            return None
        cur = self.right
        while cur.left is not None:
            cur = cur.left
        return cur

if __name__ == "__main__":
    root = BSTNode(2)
    root.insert(3)
    root.insert(100)
    root.insert(-1545)
    root.insert(-13)
    root = root.delete(2)
    root.insert(-17)
    print(root)
    print(root.height())
    print(root.degree())
    print(type(root))
