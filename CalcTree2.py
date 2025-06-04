class NodeClass:
    """Класс узла дерева выражения"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_expression_tree(rpn_expression):
    """
    Строит дерево выражения из обратной польской записи
    
    Args:
        rpn_expression (str): Строка с выражением в RPN (например "3 4 + 2 *")
    
    Returns:
        NodeClass: Указатель на корень построенного дерева
    """
    stack = []
    tokens = rpn_expression.split()
    
    for token in tokens:
        if token.isdigit():
            stack.append(NodeClass(int(token)))
        else:
            if token == '+':
                node = NodeClass(-1)
            elif token == '-':
                node = NodeClass(-2)
            elif token == '*':
                node = NodeClass(-3)
            elif token == '/':
                node = NodeClass(-4)
            else:
                raise ValueError(f"Неизвестная операция: {token}")
            
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    
    return stack.pop()


def remove_additions(root):
    """
    Рекурсивно удаляет операции сложения из дерева, заменяя их вычисленным значением
    
    Args:
        root (NodeClass): Корень дерева (или поддерева)
    
    Returns:
        NodeClass: Новый корень поддерева (без операций сложения)
    """
    if root is None:
        return None
    
    root.left = remove_additions(root.left)
    root.right = remove_additions(root.right)
    
    # Если текущий узел - операция сложения
    if root.value == -1:
        left_value = evaluate_tree(root.left)
        right_value = evaluate_tree(root.right)
        return NodeClass(left_value + right_value)
    
    return root


def evaluate_tree(node):
    """
    Вычисляет значение выражения, представленного деревом
    
    Args:
        node (NodeClass): Корень дерева (или поддерева)
    
    Returns:
        int: Результат вычисления
    """
    if node.value >= 0:
        return node.value
    
    left_value = evaluate_tree(node.left)
    right_value = evaluate_tree(node.right)
    
    if node.value == -1:
        return left_value + right_value
    elif node.value == -2:
        return left_value - right_value
    elif node.value == -3:
        return left_value * right_value
    elif node.value == -4:
        return left_value // right_value


def read_rpn_from_file(filename):
    """
    Читает выражение в обратной польской записи из файла
    
    Args:
        filename (str): Имя файла для чтения
    
    Returns:
        str: Строка с выражением
    """
    with open(filename, 'r') as f:
        return f.readline().strip()
    

def solve_problem(filename):
    """
    Основная функция решения задачи:
    1. Читает RPN выражение из файла
    2. Строит дерево выражения
    3. Удаляет операции сложения
    4. Возвращает указатель на корень преобразованного дерева
    
    Args:
        filename (str): Имя файла с выражением
    
    Returns:
        NodeClass: Указатель на корень преобразованного дерева
    """
    rpn_expression = read_rpn_from_file(filename)
    root = build_expression_tree(rpn_expression)
    new_root = remove_additions(root)
    return new_root


def main():
    """
    Точка входа в программу
    """
    filename = "input_rpn.txt"
    try:
        root = solve_problem(filename)
        print(f"Указатель на корень преобразованного дерева: {root}")
        print(f"Значение в корне: {root.value}")
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")
    except Exception as e:
        print(f"Ошибка при обработке выражения: {e}")


if __name__ == "__main__":
    main()