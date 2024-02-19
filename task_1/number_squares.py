import logging
from collections.abc import Iterator

logger = logging.getLogger(__name__)


def get_user_data() -> int:
    """ Функция для получения пользовательских данных """
    logger.info("Получение пользовательских данных")
    try:
        user_input = int(input("Введите числовое значение: "))
        logger.info(f"Получено корректное значение: {user_input} ")
        return user_input
    except ValueError:
        logger.error("Введено значение отличное от числового")


class NumberSquares:
    """
    Класс для реализации итератора, который вычисляет квадраты чисел от 1 до числа введенного пользователем.
    Аргументы:
        number - пользовательское число, до значения которого будут вычислены квадраты чисел.
    """

    def __init__(self, number: int) -> None:
        try:
            logger.info("Инициализация экземпляра класса NumberSquares для создания итератора")
            self.number = number
            logger.info("Экземпляр класса NumberSquares успешно инициализирован")
        except ValueError:
            logger.error("Ошибка инициализации объекта класса NumberSquares. Переданный аргумент имеет "
                         "не корректное значение")
        self.start = 0

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        logger.info("Запуск метода next итератора NumberSquares")
        if self.start >= self.number:
            logger.info(f"Итератор NumberSquares пустой, возбуждено исключение StopIteration")
            raise StopIteration
        self.start += 1
        logger.info(f"Результат выполнения метода next - {self.start ** 2}")
        return self.start ** 2


def number_squares_generator(number: int) -> Iterator[int]:
    """ Функция генератор для вычисления квадратов чисел от 1 до числа введенного пользователем """
    try:
        logger.info("Запуск функции number_squares_generator")
        for item in range(1, number + 1):
            yield item ** 2
        logger.info("Функция number_squares_generator отработала корректно")
    except ValueError:
        logger.error(f"Функция number_squares_generator получила аргумент отличный от ожидаемого: {number}")
