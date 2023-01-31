from typing import Any
from tree import TreeNode, Tree

class BinaryTreeNode(TreeNode):
    """Represents a Binary Tree Node
    """
    def __init__(self, key):
        super().__init__(key)
        self.left, self.right = None, None

    def height(self) -> int:
        return BinaryTreeNode.__height(self.root)

    @classmethod
    def __height(cls, node: 'BinaryTreeNode') -> int:
        """Returns the height of the tree rooted at node.

        Returns:
            An int. The height of the tree.
        """
        if not node:
            return 0
        return max(cls.__height(node.left), cls.__height(node.right)) + 1

    def degree(self) -> int:
        degree = 0
        if self.left is not None:
            degree += 1
        if self.right is not None:
            degree += 1
        return degree

class BinaryTree(Tree):
    """A Binary Tree

    Inherits Tree

    Attributes:
        root: Root node of the Binary Tree.
    """
    def search(self, key: Any) -> BinaryTreeNode:
        """Search for the node with the given key.

        Args:
            key: key of the node to search for.

        Returns:
            The node if found, else None.
        """
        pass

    def insert(self, key: Any):
        """Insert a node with the given key into the tree

        Args:
            key: key of the node to insert into the tree.
        """
        pass

    def delete(self, key: Any):
        """Delete the node with the given key in the tree

        Args:
            key: key of the node to delete from the tree.
        """
        pass