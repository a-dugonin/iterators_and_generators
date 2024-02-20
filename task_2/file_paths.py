import logging
import os.path

logger = logging.getLogger(__name__)


def gen_files_path(path):
    logger.info(f"Запуск функции {gen_files_path.__name__}")
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(path)
        for address, dirs, files in os.walk(path):
            for file in files:
                yield os.path.join(address, file)
        logger.info("Функция gen_files_path отработала корректно")
    except FileNotFoundError:
        logger.error("Указанного каталога не существует")


def get_files_path():
    logger.info("Запрос каталога пользователя")
    path_name = input("Введите адрес каталога: ")
    logger.info(f"Функция {get_files_path.__name__} отработала корректно. Получено имя каталога: {path_name}")
    return path_name




