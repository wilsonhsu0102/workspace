from typing import Any
from trees.binary_search_tree import BSTNode

class BalancedBSTNode(BSTNode):
    """This is a Balanced BST Node.

    Attributes:
        key: Key of this Balanced BST Node
        left: Left child of this Balanced BST Node
        right: Right child of this Balanced BST Node
    """
    left: 'BalancedBSTNode'
    right: 'BalancedBSTNode'

    def is_balanced(self) -> bool:
        """Checks if this tree is balanced.

        Returns:
            A boolean value. True is tree is balanced, False otherwise.
        """
        left_height = right_height = 0 
        left_balanced = right_balanced = True
        if self.left is not None:
            left_height, left_balanced = self.left.height(), self.left.is_balanced()
        if self.right is not None:
            right_height, right_balanced = self.right.height(), self.right.is_balanced()
        return all([left_balanced, right_balanced, abs(left_height - right_height) <= 1])
    
if __name__ == "__main__":
    root = BalancedBSTNode(2)
    root.insert(5)
    root.insert(-1)
    root.insert(0)
    root.insert(-2)
    root.insert(-3)
    print(root)
    print(root.is_balanced())
    print(root.degree())
    print(type(root.search(-2)))
    print(type(root))
    root2 = BalancedBSTNode(2)
    print(root2.degree())