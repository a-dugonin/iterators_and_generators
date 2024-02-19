import logging
from task_1.number_squares import get_user_data, NumberSquares, number_squares_generator

logger = logging.getLogger(__name__)
fileHandler = logging.FileHandler(filename='application_log.log', encoding='utf-8')
logging.basicConfig(format='[%(levelname)-10s] [модуль:%(name)22s] %(asctime)-25s - %(message)s',
                    handlers=[fileHandler], level=logging.INFO)

if __name__ == '__main__':
    logger.info("Скрипт запущен")
    user_data = get_user_data()
    num_squares = NumberSquares(user_data)
    print(next(num_squares))

    print(*number_squares_generator(user_data))

    try:
        logger.info("Создание генераторного выражения")
        generator_expression = (num ** 2 for num in range(1, user_data + 1))
        logger.info(f"Успешно создано генераторное выражение - generator_expression")
        print(*generator_expression)
    except ValueError as err:
        logger.exception(f"Не удалось создать генераторное выражение из за следующей ошибки: {err}")
