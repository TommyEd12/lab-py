def read_adjacency_matrix(filename):
    with open(filename, "r") as f:
        n = int(f.readline())
        matrix = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            matrix.append(row)
    return n, matrix

def build_incidence_matrix(n, adjacency):
    edges = []
    # Формируем список рёбер в нужном порядке
    for i in range(n):
        for j in range(i + 1, n):
            if adjacency[i][j] != 0:
                edges.append((i, j))

    m = len(edges)
    # Создаём матрицу нулей размером n x m
    incidence = [[0]*m for _ in range(n)]

    # Заполняем матрицу инцидентности
    for idx, (u, v) in enumerate(edges):
        incidence[u][idx] = 1
        incidence[v][idx] = 1

    return m, incidence

def write_incidence_matrix(filename, n, m, incidence):
    with open(filename, "w") as f:
        f.write(f"{n} {m}\n")
        for row in incidence:
            f.write(" ".join(map(str, row)) + "\n")

def main():
    FileName1 = "input.txt"  # исходный файл с матрицей смежности
    FileName2 = "output.txt" # файл для записи матрицы инцидентности

    n, adjacency = read_adjacency_matrix(FileName1)
    m, incidence = build_incidence_matrix(n, adjacency)
    write_incidence_matrix(FileName2, n, m, incidence)
    print(f"Матрица инцидентности записана в файл {FileName2}")

if __name__ == "__main__":
    main()

