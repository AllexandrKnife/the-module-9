def is_prime(func):
    def wrapper(*args, **kwargs):
        # Вызываем функцию, которую декорируем
        result = func(*args, **kwargs)

        # Проверяем, является ли результат простым числом
        if result > 1:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        else:
            print("Составное")

        # Возвращаем результат функции
        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


# Пример использования
result = sum_three(2, 3, 6)
print(result)
