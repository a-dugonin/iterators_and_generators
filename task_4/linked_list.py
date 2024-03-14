import logging
from typing import Any, Iterator

logger = logging.getLogger(__name__)


class Node:
    """
    Класс для создания узла односвязного списка
    Аргументы:
        value - значение узла, по умолчанию None
    """

    def __init__(self, value: Any = None) -> None:
        logger.info("Создание узла с использованием инициализации экземпляра класса Node")
        self.value = value
        self.next_node = None
        logger.info(f"Узел создан со значением {self.value}")

    def __str__(self) -> str:
        return f'[{self.value}] -> {self.next_node}'


class LinkedList:
    """ Класс для создания односвязного списка """

    def __init__(self) -> None:
        logger.info(f"Создание односвязного списка посредством инициализации экземпляра класса LinkedList")
        self.head = None
        self.length = 0
        logger.info(f"Создан пустой односвязный список")

    def __iter__(self) -> Iterator[Any]:
        """ Метод для итерирования по односвязному списку на основе генератора """
        current = self.head
        while current is not None:
            yield current.value
            current = current.next_node

    def append(self, value: Any) -> None:
        """ Метод позволяет добавить новый узел в конец связного списка
        Аргументы:
            value - значение узла
        """
        logger.info(f"Добавление элемента {value} в конец списка")
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node
        self.length += 1
        logger.info(f"Элемент {value} добавлен в конец списка")

    def get(self, index: int) -> Any:
        """
        Метод позволяет получить значение элемента узла списка по его индексу
        Аргументы:
            index - индекс узла, элемент которого необходимо получить
        """
        logger.info("Получение элемента по индексу")
        last_node = self.head
        node_index = 0
        try:
            while node_index <= index:
                if node_index == index:
                    element = last_node.value
                    logger.info(f"Элемент успешно получен. Значение элемента - {element}")
                    return element
                node_index += 1
                last_node = last_node.next_node
        except TypeError:
            logger.error(f"Передаваемый индекс должен быть числовой. В функцию передано значение {index}")

    def remove(self, index: int) -> None:
        """
        Метод позволяет удалить узел из списка по его индексу
        Аргументы:
            index - индекс узла, который необходимо удалить из списка
        """
        logger.info("Удаление узла по индексу")
        current_node = self.head
        prev_node = current_node
        node_index = 0
        try:
            if self.length == 0 or self.length < index:
                raise IndexError

            if index == 0:
                self.head = current_node.next_node
                self.length -= 1
                return

            while node_index <= index:
                if node_index == index:
                    break
                prev_node = current_node
                current_node = current_node.next_node
                node_index += 1
            prev_node.next_node = current_node.next_node
            self.length -= 1
            logger.info("Узел успешно удален")
        except TypeError:
            logger.error(f"Передаваемый индекс должен быть числовой. В функцию передано значение {index}")
        except IndexError:
            logger.error(f"Элемент под указанным индексом отсутствует в списке")

    def __str__(self) -> str:
        linked_list_str = '['
        current_node = self.head
        while current_node.next_node:
            linked_list_str += str(current_node.value) + ', '
            current_node = current_node.next_node
        linked_list_str += str(current_node.value) + ']'
        return f'{linked_list_str}'
