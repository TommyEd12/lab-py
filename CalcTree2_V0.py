class TreeNode:
    """
    Класс для представления узла дерева выражения.
    """
    def __init__(self, value):
        """
        Инициализация узла дерева.
        
        Args:
            value: Значение узла (число или код операции)
        """
        self.value = value
        self.left = None
        self.right = None
    
    def is_operation(self):
        """
        Проверяет, является ли узел операцией.
        
        Returns:
            bool: True если узел содержит операцию, False если число
        """
        return self.value in [-1, -2, -3, -4]
    
    def is_addition(self):
        """
        Проверяет, является ли узел операцией сложения.
        
        Returns:
            bool: True если узел содержит операцию сложения
        """
        return self.value == -1

def read_rpn_expression(filename):
    """
    Читает выражение в обратной польской записи из файла.
    
    Args:
        filename (str): Имя файла с выражением
        
    Returns:
        list: Список токенов выражения
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read().strip()
        tokens = content.split()
        return tokens

def build_tree_from_rpn(tokens):
    """
    Строит дерево выражения из обратной польской записи.
    
    Args:
        tokens (list): Список токенов в RPN
        
    Returns:
        TreeNode: Корень построенного дерева
    """
    stack = []
    
    # Словарь для кодирования операций
    operation_codes = {'+': -1, '-': -2, '*': -3, '/': -4}
    
    for token in tokens:
        if token in operation_codes:
            # Создаем узел операции
            node = TreeNode(operation_codes[token])
            # Берем два операнда из стека (правый, затем левый)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
        else:
            # Создаем узел с числом
            node = TreeNode(int(token))
            stack.append(node)
    
    return stack[0] if stack else None

def evaluate_tree(node):
    """
    Вычисляет значение выражения, представленного деревом.
    
    Args:
        node (TreeNode): Корень дерева или поддерева
        
    Returns:
        int: Результат вычисления
    """
    if not node.is_operation():
        return node.value
    
    left_val = evaluate_tree(node.left)
    right_val = evaluate_tree(node.right)
    
    if node.value == -1:  # сложение
        return left_val + right_val
    elif node.value == -2:  # вычитание
        return left_val - right_val
    elif node.value == -3:  # умножение
        return left_val * right_val
    elif node.value == -4:  # деление нацело
        return left_val // right_val

def remove_additions(node):
    """
    Удаляет операции сложения из дерева, заменяя их вычисленными значениями.
    
    Args:
        node (TreeNode): Корень дерева или поддерева
        
    Returns:
        TreeNode: Преобразованный узел
    """
    if not node or not node.is_operation():
        return node
    
    # Рекурсивно обрабатываем детей
    node.left = remove_additions(node.left)
    node.right = remove_additions(node.right)
    
    # Если текущий узел - операция сложения, заменяем его значением
    if node.is_addition():
        result_value = evaluate_tree(node)
        return TreeNode(result_value)
    
    return node

def print_tree(node, level=0, prefix="Root: "):
    """
    Выводит дерево в удобном для чтения формате.
    
    Args:
        node (TreeNode): Узел дерева
        level (int): Уровень вложенности
        prefix (str): Префикс для вывода
    """
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.value))
        if node.left is not None or node.right is not None:
            if node.left:
                print_tree(node.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if node.right:
                print_tree(node.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

def get_operation_name(code):
    """
    Возвращает название операции по коду.
    
    Args:
        code (int): Код операции
        
    Returns:
        str: Название операции
    """
    operations = {-1: "сложение", -2: "вычитание", -3: "умножение", -4: "деление"}
    return operations.get(code, str(code))

def print_tree_detailed(node, level=0, prefix="Root: "):
    """
    Выводит дерево с подробным описанием операций.
    
    Args:
        node (TreeNode): Узел дерева
        level (int): Уровень вложенности
        prefix (str): Префикс для вывода
    """
    if node is not None:
        if node.is_operation():
            display_value = f"{node.value} ({get_operation_name(node.value)})"
        else:
            display_value = str(node.value)
        
        print(" " * (level * 4) + prefix + display_value)
        if node.left is not None or node.right is not None:
            if node.left:
                print_tree_detailed(node.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if node.right:
                print_tree_detailed(node.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

def main():
    """
    Главная функция программы.
    """
    filename = "filename"
    
    try:
        # Читаем выражение из файла
        tokens = read_rpn_expression(filename)
        print(f"Исходное выражение в RPN: {' '.join(tokens)}")
        
        # Строим дерево
        root = build_tree_from_rpn(tokens)
        
        print("\nИсходное дерево:")
        print_tree_detailed(root)
        
        # Вычисляем значение исходного выражения
        original_value = evaluate_tree(root)
        print(f"\nЗначение исходного выражения: {original_value}")
        
        # Удаляем операции сложения
        transformed_root = remove_additions(root)
        
        print("\nПреобразованное дерево (без операций сложения):")
        print_tree_detailed(transformed_root)
        
        # Проверяем значение преобразованного выражения
        transformed_value = evaluate_tree(transformed_root)
        print(f"\nЗначение преобразованного выражения: {transformed_value}")
        
        print(f"\nУказатель на коре��ь преобразованного дерева: {id(transformed_root)}")
        print(f"Значение корня: {transformed_root.value}")
        
        return transformed_root
        
    except FileNotFoundError:
        print(f"Файл {filename} не найден!")
        return None
    except Exception as e:
        print(f"Ошибка при обработке: {e}")
        return None

if __name__ == "__main__":
    result_root = main()
