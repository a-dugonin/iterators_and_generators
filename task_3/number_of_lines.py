import os
import logging
from itertools import tee
from typing import Iterator

logger = logging.getLogger(__name__)


def numbers_of_lines(path: str) -> Iterator[str]:
    """
    Функция генератора, выдает количество строк кода во всех файлах с расширением .py в указанном каталоге
    :param path: адрес каталога
    :return: Iterator[str]
    """
    logger.info("Запуск функции numbers_of_lines")
    try:
        files, my_files = tee(os.scandir(path), 2)
        if not any(map(lambda file_py: file_py.name.endswith(".py"), files)):
            logger.info("В указанной директории отсутствуют файлы с расширением .py")
        else:
            for file in my_files:
                if file.is_file and file.name.endswith(".py"):
                    with open(file.path, encoding="utf-8") as python_file:
                        count = 0
                        for line in python_file:
                            if line.rstrip() and not line.lstrip().startswith("#"):
                                count += 1
                        yield f"В файле {file.path} - {count} строк кода"
            logger.info("Функция numbers_of_lines отработала корректно")
    except FileNotFoundError:
        logger.error("Указанного каталога не существует")


def get_files_path() -> str:
    """ Функция запрашивает у пользователя адрес каталога """
    logger.info("Запрос каталога пользователя")
    path_name = input("Введите адрес каталога: ")
    logger.info(f"Функция {get_files_path.__name__} отработала корректно. Получено имя каталога: {path_name}")
    return path_name
