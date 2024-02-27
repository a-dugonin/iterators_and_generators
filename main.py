import logging
# from task_1.number_squares import get_user_data, NumberSquares, number_squares_generator
# from task_2.file_paths import gen_files_path, get_files_path
# from task_3.number_of_lines import numbers_of_lines, get_files_path
from task_4.linked_list import Node, LinkedList


logger = logging.getLogger(__name__)
fileHandler = logging.FileHandler(filename='application_log.log', encoding='utf-8')
logging.basicConfig(format='[%(levelname)-10s] [модуль:%(name)22s] %(asctime)-25s - %(message)s',
                    handlers=[fileHandler], level=logging.INFO)

if __name__ == '__main__':
    logger.info("Скрипт запущен")
    # Ниже код для запуска скрипта реализованного в рамках task_1
    # user_data = get_user_data()
    # num_squares = NumberSquares(user_data)
    # print(next(num_squares))
    #
    # print(*number_squares_generator(user_data))
    #
    # try:
    #     logger.info("Создание генераторного выражения")
    #     generator_expression = (num ** 2 for num in range(1, user_data + 1))
    #     logger.info(f"Успешно создано генераторное выражение - generator_expression")
    #     print(*generator_expression)
    # except ValueError as err:
    #     logger.exception(f"Не удалось создать генераторное выражение из за следующей ошибки: {err}")

    # Ниже код для запуска скрипта реализованного в рамках task_2
    # path_name = get_files_path()
    # print(*gen_files_path(path_name), sep='\n')

    # Ниже код для запуска скрипта реализованного в рамках task_3
    # path_name = get_files_path()
    # print(*numbers_of_lines(path_name), sep='\n')

    # Ниже код для запуска скрипта реализованного в рамках task_3
    my_list = LinkedList()
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)
    print('Текущий список:', my_list, "\n")
    print("Перебор списка в цикле: ")
    for index, item in enumerate(my_list, 1):
        print(f'{index} значение односвязного списка - {item}')
    print()
    print('Получение третьего элемента:', my_list.get(2))
    print('Удаление второго элемента.')
    my_list.remove(1)
    print('Новый список:', my_list)
