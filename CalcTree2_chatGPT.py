class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value  # число (0..9) или код операции (-1..-4)
        self.left = left
        self.right = right

    def __str__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return f"({self.left} {self.value} {self.right})"

# Функция для вычисления значения поддерева
def evaluate(node: Node) -> int:
    if node.left is None and node.right is None:
        return node.value
    left_val = evaluate(node.left)
    right_val = evaluate(node.right)
    if node.value == -1:  # +
        return left_val + right_val
    elif node.value == -2:  # -
        return left_val - right_val
    elif node.value == -3:  # *
        return left_val * right_val
    elif node.value == -4:  # /
        if right_val == 0:
            raise ZeroDivisionError("Деление на ноль")
        return left_val // right_val
    else:
        raise ValueError("Неизвестная операция")

# Рекурсивная функция для замены поддеревьев с операцией сложения на значение
def remove_additions(node: Node) -> Node:
    if node.left is None and node.right is None:
        return node
    node.left = remove_additions(node.left)
    node.right = remove_additions(node.right)
    if node.value == -1:  # если операция сложения
        val = evaluate(node)
        return Node(val)  # заменяем поддерево на лист с этим значением
    return node

# Функция для построения дерева из ОПЗ
def build_tree_from_rpn(tokens):
    op_codes = {'+': -1, '-': -2, '*': -3, '/': -4}
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(Node(int(token)))
        elif token in op_codes:
            if len(stack) < 2:
                raise ValueError("Неверное выражение")
            right = stack.pop()
            left = stack.pop()
            stack.append(Node(op_codes[token], left, right))
        else:
            raise ValueError(f"Неизвестный токен: {token}")
    if len(stack) != 1:
        raise ValueError("Неверное выражение")
    return stack[0]

def main():
    filename = "input.txt"

    with open(filename, "r") as f:
        content = f.read().strip()
    tokens = content.split()

    tree = build_tree_from_rpn(tokens)
    tree = remove_additions(tree)

    # Для вывода указателя на корень — выведем структуру дерева
    # или просто значение корня
    def print_tree(node):
        if node.left is None and node.right is None:
            return str(node.value)
        return f"({print_tree(node.left)} {node.value} {print_tree(node.right)})"

    print("Корень после замены сложения:")
    print(print_tree(tree))

if __name__ == "__main__":
    main()
