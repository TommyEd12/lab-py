def read_adjacency_matrix(filename):
    """
    Читает матрицу смежности из файла.
    
    Args:
        filename (str): Имя файла, содержащего матрицу смежности
        
    Returns:
        list: Матрица смежности в виде списка списков
    """
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
        adjacency_matrix = []
        for _ in range(n):
            row = list(map(int, file.readline().strip().split()))
            adjacency_matrix.append(row)
    return adjacency_matrix

def create_incidence_matrix(adjacency_matrix):
    """
    Создает матрицу инцидентности из матрицы смежности для неориентированного графа.
    
    Args:
        adjacency_matrix (list): Матрица смежности в виде списка списков
        
    Returns:
        tuple: Кортеж, содержащий количество вершин, количество ребер и матрицу инцидентности
    """
    n = len(adjacency_matrix)
    edges = []
    
    # Собираем все ребра согласно указанному порядку
    for i in range(n):
        for j in range(n):
            # Для неориентированного графа рассматриваем только ребра где i < j
            # чтобы избежать двойного подсчета каждого ребра
            if i < j and adjacency_matrix[i][j] != 0:
                edges.append((i, j))
    
    m = len(edges)
    incidence_matrix = [[0 for _ in range(m)] for _ in range(n)]
    
    # Заполняем матрицу инцидентности
    for edge_idx, (i, j) in enumerate(edges):
        incidence_matrix[i][edge_idx] = 1
        incidence_matrix[j][edge_idx] = 1
    
    return n, m, incidence_matrix

def write_incidence_matrix(filename, n, m, incidence_matrix):
    """
    Записывает матрицу инцидентности в файл.
    
    Args:
        filename (str): Имя файла для записи
        n (int): Количество вершин
        m (int): Количество ребер
        incidence_matrix (list): Матрица инцидентности в виде списка списков
    """
    with open(filename, 'w') as file:
        file.write(f"{n} {m}\n")
        for row in incidence_matrix:
            file.write(' '.join(map(str, row)) + '\n')

def main():
    """
    Главная функция для преобразования матрицы смежности в матрицу инцидентности.
    """
    input_filename = "FileName1"
    output_filename = "FileName2"
    
    adjacency_matrix = read_adjacency_matrix(input_filename)
    n, m, incidence_matrix = create_incidence_matrix(adjacency_matrix)
    write_incidence_matrix(output_filename, n, m, incidence_matrix)

if __name__ == "__main__":
    main()