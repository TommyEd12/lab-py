def count_numbers_with_two_consecutive_zeros(N, K):
    # dp[i][0] - заканчивается на 0, без двух подряд нулей
    # dp[i][1] - заканчивается на не-0, без двух подряд нулей
    dp = [[0, 0] for _ in range(N+1)]

    dp[1][0] = 1
    dp[1][1] = K - 1

    for i in range(2, N+1):
        dp[i][0] = dp[i-1][1] * 1  # поставить 0 после не-0
        dp[i][1] = (dp[i-1][0] + dp[i-1][1]) * (K - 1)  # поставить не-0 после любого

    total = K ** N
    without_two_zeros = dp[N][0] + dp[N][1]
    result = total - without_two_zeros
    return result

# Пример использования:
N = 5
K = 3
print(f"Количество чисел длины {N} в системе с основанием {K} с двумя и более подряд идущими нулями:", count_numbers_with_two_consecutive_zeros(N, K))

