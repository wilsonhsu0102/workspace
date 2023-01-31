import abc
from typing import TypeVar, Generic

T = TypeVar("T")

class TreeNode(Generic[T], metaclass=abc.ABCMeta):
    """Represents the most general tree node.
    """
    def __init__(self, key: T):
        self.key = key

    @abc.abstractmethod
    def height(self) -> int:
        """Returns the height of the tree.

        Returns:
            An int. The height of the tree.
        """
        raise NotImplementedError("Class %s doesn't implement height()" % (self.__class__.__name__))
    
    @abc.abstractmethod
    def degree(self) -> int:
        """Returns the degree of the node.

        Returns:
            An int. The degree of the node.
        """
        raise NotImplementedError("Class %s doesn't implement degree()" % (self.__class__.__name__))

class Tree(metaclass=abc.ABCMeta):
    """Represents the most general tree.

    Attributes:
        root: Root node of the Tree.
    """
    def __init__(self):
        self.root = None

    @abc.abstractmethod
    def search(self, key: T) -> TreeNode[T]:
        """Search for the node with the given key.

        Args: 
            key: key of the node to search for.

        Returns:
            The node if found, else None.
        """
        raise NotImplementedError("Class %s doesn't implement search()" % (self.__class__.__name__))

    @abc.abstractmethod
    def insert(self, key: T):
        """Insert a node with the given key into the tree

        Args: 
            key: key of the node to insert into the tree.
        """
        raise NotImplementedError("Class %s doesn't implement insert()" % (self.__class__.__name__))

    @abc.abstractmethod
    def delete(self, key: T):
        """Delete the node with the given key in the tree

        Args: 
            key: key of the node to delete from the tree.
        """
        raise NotImplementedError("Class %s doesn't implement delete()" % (self.__class__.__name__))