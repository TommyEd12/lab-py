def count_numbers_with_double_zeros(K, N):
    """
    Подсчитывает количество K-ичных чисел из N разрядов, содержащих два или более подряд идущих нуля.
    
    Args:
        K (int): Основание системы счисления (2 ≤ K ≤ 10)
        N (int): Количество разрядов (1 < N < 20, N + K < 26)
    
    Returns:
        int: Количество чисел с двумя и более подряд нулями
    """
    # Общее количество K-ичных чисел из N разрядов
    total_numbers = (K - 1) * (K ** (N - 1))  # Первая цифра не может быть 0
    
    # Количество чисел без двух подряд нулей
    no_double_zeros = count_numbers_without_double_zeros(K, N)
    
    # Искомое количество = общее количество - количество без двух подряд нулей
    return total_numbers - no_double_zeros

def count_numbers_without_double_zeros(K, N):
    """
    Подсчитывает количество K-ичных чисел из N разрядов без двух подряд идущих нулей.
    
    Args:
        K (int): Основание системы счисления
        N (int): Количество разрядов
    
    Returns:
        int: Количество чисел без двух подряд нулей
    """
    if N == 1:
        return K  # Все однозначные числа подходят
    
    # Динамическое программирование:
    # dp0[i] - количество чисел длины i, оканчивающихся на 0
    # dp1[i] - количество чисел длины i, оканчивающихся не на 0
    dp0 = [0] * (N + 1)
    dp1 = [0] * (N + 1)
    
    # Базовые случаи:
    dp0[1] = 1  # Числа: 0
    dp1[1] = K - 1  # Числа: 1..K-1
    
    for i in range(2, N + 1):
        # Число, оканчивающееся на 0, можно получить только из числа, оканчивающегося не на 0
        dp0[i] = dp1[i - 1]
        
        # Число, оканчивающееся не на 0, можно получить из любого числа, добавив любую цифру кроме 0
        dp1[i] = (dp0[i - 1] + dp1[i - 1]) * (K - 1)
    
    return dp0[N] + dp1[N]

def solve():
    """
    Основная функция для решения задачи.
    Считывает входные данные, проверяет их корректность и выводит результат.
    """
    try:
        K = int(input("Введите основание системы счисления K (2 ≤ K ≤ 10): "))
        N = int(input("Введите количество разрядов N (1 < N < 20, N + K < 26): "))
        
        # Проверка входных данных
        if not (2 <= K <= 10):
            raise ValueError("Основание системы счисления K должно быть от 2 до 10")
        if not (1 < N < 20):
            raise ValueError("Количество разрядов N должно быть от 2 до 19")
        if N + K >= 26:
            raise ValueError("Сумма N + K должна быть меньше 26")
        
        result = count_numbers_with_double_zeros(K, N)
        print(f"Количество {K}-ичных чисел из {N} разрядов с двумя и более подряд нулями: {result}")
    
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    solve()