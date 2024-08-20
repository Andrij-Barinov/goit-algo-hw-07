class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def sum_tree_values(root):
    if root is None:
        return 0
    return root.val + sum_tree_values(root.left) + sum_tree_values(root.right)

# Створення дерева і вставка ключів
root = None
keys = [10, 20, 5, 3, 7, 30]
for key in keys:
    root = insert(root, key)

# Знаходження суми значень
total_sum = sum_tree_values(root)
print(f"Сума всіх значень у дереві: {total_sum}")
