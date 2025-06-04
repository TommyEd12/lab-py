def count_numbers_without_consecutive_zeros(N, K):
    """
    Подсчитывает количество N-разрядных чисел в системе счисления с основанием K,
    которые НЕ содержат два подряд идущих нуля.
    
    Args:
        N (int): Количество разрядов (1 < N < 20)
        K (int): Основание системы счисления (2 ≤ K ≤ 10)
        
    Returns:
        int: Количество чисел без двух подряд идущих нулей
    """
    # dp[i][0] - количество i-разрядных чисел, заканчивающихся на 0
    # dp[i][1] - количество i-разрядных чисел, заканчивающихся на ненулевую цифру
    dp = [[0, 0] for _ in range(N + 1)]
    
    # Базовые случаи для 1-разрядных чисел
    dp[1][0] = 0        # Первая цифра не может быть 0
    dp[1][1] = K - 1    # Первая цифра может быть любой из K-1 ненулевых цифр
    
    # Заполняем таблицу динамического программирования
    for i in range(2, N + 1):
        # Можем добавить 0 только после ненулевой цифры
        dp[i][0] = dp[i-1][1]
        
        # Можем добавить любую ненулевую цифру после любой цифры
        dp[i][1] = dp[i-1][0] * (K - 1) + dp[i-1][1] * (K - 1)
    
    return dp[N][0] + dp[N][1]

def count_total_n_digit_numbers(N, K):
    """
    Подсчитывает общее количество N-разрядных чисел в системе счисления с основанием K.
    
    Args:
        N (int): Количество разрядов
        K (int): Основание системы счисления
        
    Returns:
        int: Общее количество N-разрядных чисел
    """
    # Первая цифра может быть любой из K-1 ненулевых цифр
    # Остальные N-1 цифр могут быть любыми из K цифр
    return (K - 1) * (K ** (N - 1))

def count_numbers_with_consecutive_zeros(N, K):
    """
    Подсчитывает количество N-разрядных чисел в системе счисления с основанием K,
    которые содержат два и более подряд идущих нуля.
    
    Args:
        N (int): Количество разрядов (1 < N < 20)
        K (int): Основание системы счисления (2 ≤ K ≤ 10)
        
    Returns:
        int: Количество чисел с двумя и более подряд идущими нулями
    """
    total_numbers = count_total_n_digit_numbers(N, K)
    numbers_without_consecutive_zeros = count_numbers_without_consecutive_zeros(N, K)
    
    return total_numbers - numbers_without_consecutive_zeros

def validate_input(N, K):
    """
    Проверяет корректность входных данных.
    
    Args:
        N (int): Количество разрядов
        K (int): Основание системы счисления
        
    Returns:
        bool: True если входные данные корректны, False иначе
    """
    if not (1 < N < 20):
        print(f"Ошибка: N должно быть в диапазоне (1, 20), получено N = {N}")
        return False
    
    if not (2 <= K <= 10):
        print(f"Ошибка: K должно быть в диапазоне [2, 10], получено K = {K}")
        return False
    
    if N + K >= 26:
        print(f"Ошибка: N + K должно быть меньше 26, получено N + K = {N + K}")
        return False
    
    return True

def analyze_problem(N, K):
    """
    Анализирует задачу и выводит подробную информацию о решении.
    
    Args:
        N (int): Количество разрядов
        K (int): Основание системы счисления
    """
    print(f"Анализ для {N}-разрядных чисел в системе счисления с основанием {K}:")
    print("=" * 60)
    
    total = count_total_n_digit_numbers(N, K)
    without_consecutive = count_numbers_without_consecutive_zeros(N, K)
    with_consecutive = count_numbers_with_consecutive_zeros(N, K)
    
    print(f"Общее количество {N}-разрядных чисел: {total}")
    print(f"Числа без двух подряд идущих нулей: {without_consecutive}")
    print(f"Числа с двумя и более подряд идущими нулями: {with_consecutive}")
    print(f"Проверка: {without_consecutive} + {with_consecutive} = {without_consecutive + with_consecutive}")
    
    percentage = (with_consecutive / total) * 100 if total > 0 else 0
    print(f"Процент чисел с подряд идущими нулями: {percentage:.2f}%")

def demonstrate_dp_table(N, K):
    """
    Демонстрирует таблицу динамического программирования.
    
    Args:
        N (int): Количество разрядов
        K (int): Основание системы счисления
    """
    print(f"\nТаблица динамического программирования для N={N}, K={K}:")
    print("i\tdp[i][0]\tdp[i][1]\tВсего")
    print("-" * 40)
    
    dp = [[0, 0] for _ in range(N + 1)]
    dp[1][0] = 0
    dp[1][1] = K - 1
    
    print(f"1\t{dp[1][0]}\t\t{dp[1][1]}\t\t{dp[1][0] + dp[1][1]}")
    
    for i in range(2, N + 1):
        dp[i][0] = dp[i-1][1]
        dp[i][1] = dp[i-1][0] * (K - 1) + dp[i-1][1] * (K - 1)
        total = dp[i][0] + dp[i][1]
        print(f"{i}\t{dp[i][0]}\t\t{dp[i][1]}\t\t{total}")

def main():
    """
    Главная функция программы.
    """
    print("Программа для подсчета K-ичных чисел с подряд идущими нулями")
    print("=" * 60)
    
    # Примеры для демонстрации
    test_cases = [
        (3, 2),   # 3-разрядные двоичные числа
        (4, 3),   # 4-разрядные троичные числа
        (5, 10),  # 5-разрядные десятичные числа
        (3, 5),   # 3-разрядные пятеричные числа
    ]
    
    for N, K in test_cases:
        if validate_input(N, K):
            analyze_problem(N, K)
            demonstrate_dp_table(N, K)
            print("\n" + "=" * 60 + "\n")
    
    # Интерактивный режим
    print("Интерактивный режим:")
    try:
        N = int(input("Введите количество разрядов N (1 < N < 20): "))
        K = int(input("Введите основание системы счисления K (2 ≤ K ≤ 10): "))
        
        if validate_input(N, K):
            result = count_numbers_with_consecutive_zeros(N, K)
            print(f"\nОтвет: {result}")
            print(f"Среди {N}-разрядных чисел в системе счисления с основанием {K}")
            print(f"имеется {result} чисел, содержащих два и более подряд идущих нуля.")
            
            analyze_problem(N, K)
        
    except ValueError:
        print("Ошибка: Введите корректные целые числа!")
    except KeyboardInterrupt:
        print("\nПрограмма завершена пользователем.")

if __name__ == "__main__":
    main()
