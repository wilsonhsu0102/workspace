from typing import Any
import abc

class BalancedBSTAbstractClass(Tree):
    """Implement this abstract class for a Balanced BST.

    Attributes:
        root: Root node of the Balanced BST.
    """
    def __init__(self):
        self.root = None

    def is_balanced(self) -> bool:
        """Checks if this tree is balanced.

        Method based on the instance created.

        Returns:
            A boolean value. True is tree is balanced, False otherwise.
        """
        return BalancedBSTAbstractClass.__is_balanced(self.root)

    @classmethod
    def __is_balanced(cls, node: Any) -> bool:
        """Checks if the tree rooted at node is balanced.

        Class method, does not based on instances.

        Returns:
            A boolean value. True is tree is balanced, False otherwise.
        """
        if node is None:
            return True
        left_height = cls.height(node.left)
        right_height = cls.height(node.right)

        if abs(left_height - right_height) <= 1 and cls.__is_balanced(node.left) and cls.__is_balanced(node.right):
            return True
        return False

    @classmethod
    def height(cls, node: Any) -> int:
        """Returns the height of the tree rooted at node.

        Returns:
            An int. The height of the tree.
        """
        if not node:
            return 0
        return max(cls.height(node.left), cls.height(node.right)) + 1

class AVLTree(BalancedBSTAbstractClass):
    """An AVL Tree

    Inherits BalancedBSTAbstractClass

    Attributes:
        root: Root node of the AVL Tree.
    """
    def search(self, key: Any) -> Any:
        """Search for the node with the given key.

        Args: 
            key: key of the node to search for.

        Returns:
            The node if found, else None.
        """
        pass

    def insert(self, key: Any) -> Any:
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
    
if __name__ == "__main__":
    # abstractTree = BalancedBSTAbstractClass()
    avlTree = AVLTree()
    print(avlTree.is_balanced())
    print(avlTree.height(avlTree.root))
