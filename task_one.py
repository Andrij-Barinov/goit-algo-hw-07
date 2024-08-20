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

def find_max_value(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.val

# Створення дерева і вставка ключів
root = None
keys = [10, 20, 5, 3, 7, 30]
for key in keys:
    root = insert(root, key)

# Пошук найбільшого значення
max_value = find_max_value(root)
print(f"Найбільше значення в дереві: {max_value}")
