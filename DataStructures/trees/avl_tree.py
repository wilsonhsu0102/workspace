from trees.balanced_BST import BalancedBSTNode
from typing import Optional

class AVLTreeNode(BalancedBSTNode):
    """An AVL Tree

    Inherits BalancedBSTNode

    Attributes:
        root: Root node of the AVL Tree.
    """
    def search(self, key: int) -> Optional['AVLTreeNode']:
        pass

    def insert(self, key: int):
        pass

    def delete(self, key: int) -> Optional['AVLTreeNode']:
        pass