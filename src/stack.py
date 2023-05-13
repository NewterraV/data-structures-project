class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.head = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        if self.head is None:
            node = Node(data)
        else:
            node = Node(data, self.head.next_node)
        if self.head:
            node.next_node = self.head
        self.head = node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        result = self.head.data
        self.head = self.top.next_node
        return result

    @property
    def top(self):
        """
        Метод возвращает экземпляр класса
        """
        return self.head
