from trees.tree import TreeNode
import abc

class BalancedTree(Tree, metaclass=abc.ABCMeta):
    """Represents a Balanced Tree
    """
    @abc.abstractmethod
    def is_balanced(self) -> bool:
        """Checks if the tree rooted at node is balanced.

        Class method, does not based on instances.

        Returns:
            A boolean value. True is tree is balanced, False otherwise.
        """
        raise NotImplementedError("Class %s doesn't implement is_balanced()" % (self.__class__.__name__))
