import abc
from typing import Optional

class TreeNode(metaclass=abc.ABCMeta):
    """Represents the most general tree node.

    Attributes:
        key: Key of the node.
    """
    key: int

    def __init__(self, key: int):
        self.key = key

    @abc.abstractmethod
    def height(self) -> int:
        """Returns the height of the tree.

        Returns:
            An int. The height of the tree.
        """
        pass

    @abc.abstractmethod
    def degree(self) -> int:
        """Returns the degree of the node.

        Returns:
            An int. The degree of the node.
        """
        pass

    @abc.abstractmethod
    def search(self, key: int) -> Optional['TreeNode']:
        """Search for the node with the given key within the tree.

        Args: 
            key: key of the node to search for.

        Returns:
            The node if found, else None.
        """
        pass

    @abc.abstractmethod
    def insert(self, key: int) -> Optional['TreeNode']:
        """Insert a node with the given key into the tree.

        Args:
            key: key of the node to insert into the tree.
        """
        pass

    @abc.abstractmethod
    def delete(self, key: int) -> Optional['TreeNode']:
        """Delete the node with the given key in the tree.

        If the deleted node is the root node that the parent pointer point to,
        you would need to assign the return node to the parent pointer to update.

        Args: 
            key: key of the node to delete from the tree.

        Returns:
            The new root node, returns None if tree is empty.
        """
        pass