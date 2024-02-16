from collections.abc import Iterator


class NumberSquares:
    """
    Класс для реализации итератора, который вычисляет квадраты чисел от 1 до числа введенного пользователем.
    Аргументы:
        number - пользовательское число, до значения которого будут вычислены квадраты чисел.
    """
    def __init__(self, number: int) -> None:
        self.number = number
        self.start = 0

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.start >= self.number:
            raise StopIteration
        self.start += 1
        return self.start ** 2


def number_squares(number: int) -> Iterator[int]:
    """ Функция генератор для вычисления квадратов чисел от 1 до числа введенного пользователем """
    for item in range(1, number + 1):
        yield item ** 2


if __name__ == '__main__':
    user_value = int(input("Введите значение: "))
    # num_squares_iter = NumberSquares(user_value)
    # print(*num_squares_iter)

    # num_squares_func_generator = number_squares(user_value)
    # print(*num_squares_func_generator)

    # Генераторное выражение для вычисления квадратов чисел
    number_squares_gen_expression = (num ** 2 for num in range(1, user_value + 1))
    print(*number_squares_gen_expression)
