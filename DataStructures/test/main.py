from trees.balanced_BST import BalancedBSTNode

# TODO: Fix package imports, would like to use a way 
# where I don't have to have a setup.py
root = BalancedBSTNode(2)
root.insert(5)
root.insert(-1)
root.insert(0)
root.insert(-2)
root.insert(-3)
print(root)
print(root.is_balanced())
print(type(root.search(-2)))
print(type(root))
