class Node:
    """Класс для узла очереди"""

    def __init__(self, data=None, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

        # Set методы

    def set_data(self, data):
        self.data = data

    def set_next(self, nxt):
        self.next_node = nxt


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data)
        cur_node = self.head
        if cur_node is None:
            self.head = self.tail = new_node
            return
        while cur_node.next_node is not None:
            cur_node = cur_node.next_node
        cur_node.next_node = new_node
        self.tail = new_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        result = self.head.data
        self.head = self.head.next_node
        return result

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        node = self.head
        text = ''
        while True:
            if self.tail is None:
                break
            if node == self.tail:
                text += self.tail.data
                break
            text += f'{node.data}\n'
            node = node.next_node

        return text
