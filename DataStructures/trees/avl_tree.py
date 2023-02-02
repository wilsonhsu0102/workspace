from trees.balanced_BST import BalancedBSTNode
from typing import Optional

class AVLTreeNode(BalancedBSTNode):
    """An AVL Tree

    Inherits BalancedBSTNode

    Attributes:
        key: Key of this AVLTreeNode
        left: Left child of this AVLTreeNode
        right: Right child of this AVLTreeNode
    """
    key: int
    balance_factor: int
    left: 'AVLTreeNode'
    right: 'AVLTreeNode'

    def __init__(self, key):
        super().__init__(key)
        self.balance_factor = 0

    def insert(self, key: int) -> Optional['AVLTreeNode']:
        selfType = type(self)
        if self.key > key:
            if self.left is None:
                self.left = selfType(key)
            else:
                self.left = self.left.insert(key)
            self.update_balance_factor()
            # print("Left Insert %d BF:" % key, self.balance_factor)
            if self.balance_factor < -1:
                if self.left is None:
                    return self
                if self.left.balance_factor > 1:
                    # left right case
                    self.left = self.left.__rotate_left()
                    self = self.__rotate_right()
                else:
                    # left left case
                    self = self.__rotate_right()
        elif self.key < key:
            if self.right is None:
                self.right = selfType(key)
            else:
                self.right = self.right.insert(key)
            self.update_balance_factor()
            # print("Right Insert %d BF:" % key, self.balance_factor)
            if self.balance_factor > 1:
                if self.right is None:
                    return self
                if self.right.balance_factor >= 0:
                    # right right case
                    self = self.__rotate_left()
                else:
                    # right left case
                    self.right = self.right.__rotate_right()
                    self = self.__rotate_left()
        return self


    def delete(self, key: int) -> Optional['AVLTreeNode']:
        pass

    def update_balance_factor(self):
        left_bf = right_bf = 0
        if self.left is not None:
            left_bf = self.left.height()
        if self.right is not None:
            right_bf = self.right.height()
        self.balance_factor = right_bf - left_bf
        return

    def __rotate_left(self) -> 'AVLTreeNode':
        """Rotate current node to the left, so it becomes the 
        left child of its original right child. Current node's
        new left child will become original right child's left 
        child

        Returns:
            The old right child of this node as the new root.
        """
        # No rotation can be done.
        if self.right is None:
            return self
        oldRightChild = self.right
        self.right = self.right.left
        self.update_balance_factor()
        oldRightChild.left = self
        oldRightChild.update_balance_factor()
        return oldRightChild

    def __rotate_right(self) -> 'AVLTreeNode':
        """Rotate current node to the right, so it becomes the 
        right child of its original left child. Current node's new
        right child will become original left child's right child

        Returns:
            The old left child of this node as the new root.
        """
        # No rotation can be done.
        if self.left is None:
            return self
        oldLeftChild = self.left
        self.left = self.left.right
        self.update_balance_factor()
        oldLeftChild.right = self
        oldLeftChild.update_balance_factor()
        return oldLeftChild
    
if __name__ == "__main__":
    root = AVLTreeNode(0)
    print("Root\n", root)
    root = root.insert(5)
    print("Root\n", root)
    root = root.insert(2)
    print("Root\n", root)
    root = root.insert(3)
    print("Root\n", root)
    root = root.insert(-1)
    print("Root\n", root)
    root = root.insert(-2)
    print("Root\n", root)
    root = root.insert(-3)
    print("Root\n", root)
    root = root.insert(-4)
    print("Root\n", root)
    root = root.insert(-5)
    print("Root\n", root)
    root = root.insert(-6)
    print("Root\n", root)
    root = root.insert(-7)
    print("Root\n", root)
    print("Root BF:", root.balance_factor)
    
