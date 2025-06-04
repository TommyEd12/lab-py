class Node:
    """Узел дерева выражения"""
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
        Node: Указатель на корень построенного дерева
    """
    stack = []
    tokens = rpn_expression.split()
    
    for token in tokens:
        if token.isdigit():
            # Операнд - создаем узел с числом
            stack.append(Node(int(token)))
        else:
            # Операция - создаем узел операции
            if token == '+':
                node = Node(-1)
            elif token == '-':
                node = Node(-2)
            elif token == '*':
                node = Node(-3)
            elif token == '/':
                node = Node(-4)
            else:
                raise ValueError(f"Неизвестная операция: {token}")
            
            # Берем два последних операнда из стека
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    
    return stack.pop()

def remove_additions(root):
    """
    Рекурсивно удаляет операции сложения из дерева, заменяя их вычисленным значением
    
    Args:
        root (Node): Корень дерева (или поддерева)
    
    Returns:
        Node: Новый корень поддерева (без операций сложения)
    """
    if root is None:
        return None
    
    # Рекурсивно обрабатываем левое и правое поддеревья
    root.left = remove_additions(root.left)
    root.right = remove_additions(root.right)
    
    # Если текущий узел - операция сложения
    if root.value == -1:
        # Вычисляем значение поддерева
        left_val = evaluate_tree(root.left)
        right_val = evaluate_tree(root.right)
        # Заменяем на узел с вычисленным значением
        return Node(left_val + right_val)
    
    return root

def evaluate_tree(node):
    """
    Вычисляет значение выражения, представленного деревом
    
    Args:
        node (Node): Корень дерева (или поддерева)
    
    Returns:
        int: Результат вычисления
    """
    if node.value >= 0:
        return node.value
    
    left_val = evaluate_tree(node.left)
    right_val = evaluate_tree(node.right)
    
    if node.value == -1:   # +
        return left_val + right_val
    elif node.value == -2: # -
        return left_val - right_val
    elif node.value == -3: # *
        return left_val * right_val
    elif node.value == -4: # /
        return left_val // right_val

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
        Node: Указатель на корень преобразованного дерева
    """
    rpn_expression = read_rpn_from_file(filename)
    root = build_expression_tree(rpn_expression)
    new_root = remove_additions(root)
    return new_root

# Пример использования
if __name__ == "__main__":
    filename = "input_rpn.txt"  # Файл с выражением в RPN
    try:
        root = solve_problem(filename)
        print(f"Указатель на корень преобразованного дерева: {root}")
        print(f"Значение в корне: {root.value}")
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")
    except Exception as e:
        print(f"Ошибка при обработке выражения: {e}")