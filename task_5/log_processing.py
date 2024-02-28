import logging
import os
from typing import Iterator

logger = logging.getLogger(__name__)


def error_log_generator(path: str) -> Iterator[str]:
    logger.info("Запуск функции error_log_generator")
    if not os.path.isfile(path):
        raise FileNotFoundError(path)
    with open(path, encoding="utf-8") as log_file:
        for line in log_file:
            if "ERROR" in line:
                yield line
    logger.info("Функция error_log_generator отработала корректно")


def get_files_path() -> str:
    """ Функция запрашивает у пользователя путь к файлу с логами """
    logger.info("Запрос пути к файлу с логами")
    path_name = input("Введите путь к файлу с логами: ")
    logger.info(f"Функция {get_files_path.__name__} отработала корректно. Получено путь: {path_name}")
    return path_name
