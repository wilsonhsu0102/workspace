from trees.tree import TreeNode
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

class BinaryTreeNode(TreeNode):
    """Represents a Binary Tree Node

    Attributes:
        key: Key of the node.
        left: Left child of the node.
        right: Right child of the node.
    """
    left: 'BinaryTreeNode'
    right: 'BinaryTreeNode'

    def __init__(self, key: int):
        super().__init__(key)
        self.left, self.right = None, None

    def height(self) -> int:
        left_height, right_height = 0, 0
        if self.left is not None:
            left_height = self.left.height()
        if self.right is not None:
            right_height = self.right.height()
        return max(left_height, right_height) + 1

    def degree(self) -> int:
        root_degree, left_degree, right_degree = 0, 0, 0
        if self.left is not None:
            root_degree += 1
            left_degree = self.left.degree()
        if self.right is not None:
            root_degree += 1
            right_degree = self.right.degree()
        return max(root_degree, left_degree, right_degree)

    def __str__(self) -> str:
        return "\n".join(BinaryTreeNode.formatTree(self))

    @classmethod
    def formatTree(cls, node: 'BinaryTreeNode', level: int = 0) -> list[str]:
        result_string = []
        if node is not None:
            result_string.extend(cls.formatTree(node.right, level + 1))
            result_string.append(" " * 4 * level + f"{Fore.MAGENTA}->{Style.RESET_ALL} %s" % str(node.key))
            result_string.extend(cls.formatTree(node.left, level + 1))
        return result_string
        
if __name__ == "__main__":
    root = BinaryTreeNode(2)
    print(root)
