class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def right_rotate(y):
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

# Пошук мінімального
def min_value_node(node):
    if not node:
        return None
    current = node
    while current.left:
        current = current.left
    return current

# Пошук максимального
def max_value_node(node):
    if not node:
        return None
    current = node
    while current.right:
        current = current.right
    return current

# Знаходження суми всіх значень
def sum_values(node):
    if not node:
        return 0
    return node.key + sum_values(node.left) + sum_values(node.right)

def insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

# Тест
avl_tree = None
avl_tree = insert(avl_tree, 10)
avl_tree = insert(avl_tree, 20)
avl_tree = insert(avl_tree, 30)
avl_tree = insert(avl_tree, 25)
avl_tree = insert(avl_tree, 28)
avl_tree = insert(avl_tree, 27)
avl_tree = insert(avl_tree, -1)

print("Найбільше значення в AVL-дереві:", max_value_node(avl_tree).key)
print("Найменше значення в AVL-дереві:", min_value_node(avl_tree).key)
print("Сума всіх значень в AVL-дереві:", sum_values(avl_tree))
