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

def find_min_value(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.val

# Створення дерева і вставка ключів
root = None
keys = [10, 20, 5, 3, 7, 30]
for key in keys:
    root = insert(root, key)

# Пошук найменшого значення
min_value = find_min_value(root)
print(f"Найменше значення в дереві: {min_value}")
