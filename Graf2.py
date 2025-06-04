def read_adjacency_matrix(filename):
    """
    Читает матрицу смежности из файла.

    Args:
        filename (str): Имя файла, содержащего матрицу смежности.

    Returns:
        tuple: Кортеж из двух элементов:
            - n (int): Количество вершин в графе.
            - matrix (list): Матрица смежности (список списков целых чисел).

    Raises:
        FileNotFoundError: Если файл не существует.
        ValueError: Если данные в файле некорректны.
    """
    with open(filename, "r") as file:
        n = int(file.readline())
        matrix = []
        for _ in range(n):
            row = list(map(int, file.readline().split()))
            if len(row) != n:
                raise ValueError("Некорректный формат матрицы смежности")
            matrix.append(row)
    return n, matrix


def build_incidence_matrix(n, adjacency):
    """
    Преобразует матрицу смежности в матрицу инцидентности для неориентированного графа.

    Args:
        n (int): Количество вершин в графе.
        adjacency (list): Матрица смежности (список списков целых чисел).

    Returns:
        tuple: Кортеж из двух элементов:
            - m (int): Количество ребер в графе.
            - incidence (list): Матрица инцидентности (список списков целых чисел).

    Note:
        Для неориентированного графа каждое ребро между вершинами i и j
        представляется один раз (i < j), а в матрице инцидентности
        соответствующий столбец содержит 1 в строках i и j.
    """
    edges = []
    # Собираем ребра (только верхний треугольник матрицы, чтобы избежать дублирования)
    for i in range(n):
        for j in range(i + 1, n):
            if adjacency[i][j] != 0:
                edges.append((i, j))

    m = len(edges)
    incidence = [[0] * m for _ in range(n)]

    for edge_idx, (u, v) in enumerate(edges):
        incidence[u][edge_idx] = 1
        incidence[v][edge_idx] = 1

    return m, incidence


def write_incidence_matrix(filename, n, m, incidence):
    """
    Записывает матрицу инцидентности в файл.

    Args:
        filename (str): Имя файла для записи.
        n (int): Количество вершин в графе.
        m (int): Количество ребер в графе.
        incidence (list): Матрица инцидентности (список списков целых чисел).

    Raises:
        IOError: Если возникла ошибка при записи в файл.
    """
    with open(filename, "w") as f:
        f.write(f"{n} {m}\n")
        for row in incidence:
            f.write(" ".join(map(str, row)) + "\n")


def main():
    """
    Основная функция программы. Выполняет преобразование матрицы смежности
    в матрицу инцидентности и записывает результат в файл.
    """
    input_filename = "input.txt"
    output_filename = "output.txt"

    try:
        n, adjacency = read_adjacency_matrix(input_filename)
        m, incidence = build_incidence_matrix(n, adjacency)
        write_incidence_matrix(output_filename, n, m, incidence)
        print(f"Матрица инцидентности успешно записана в файл '{output_filename}'")
        print(f"Граф содержит {n} вершин и {m} рёбер")
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_filename}' не найден")
    except ValueError as e:
        print(f"Ошибка в данных: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()