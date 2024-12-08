def all_variants(text):
    n = len(text)
    # Перебираем все числа от 0 до 2^n - 1
    for i in range(1, 1 << n):
        subsequence = ""
        # Проверяем каждый бит числа
        for j in range(n):
            if i & (1 << j):
                subsequence += text[j]
        yield subsequence


# Пример использования
a = all_variants("abc")
for i in a:
    print(i)
