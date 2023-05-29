class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if self.head is None:
            node = Node(data)
        else:
            node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        cur_node = self.head
        if cur_node is None:
            self.head = self.tail = new_node
            return
        while cur_node.next_node is not None:
            cur_node = cur_node.next_node
        cur_node.next_node = new_node
        self.tail = new_node

    def to_list(self):
        """Возвращает список с данными"""
        node = self.head
        data_lst = []
        if node is None:
            data_lst.append(None)

        while node:
            data_lst.append(node.data)
            node = node.next_node

        return data_lst

    def get_data_by_id(self, user_id):
        """Возвращает первый найденный словарь с ключом 'id',
        значение которого равно переданному в метод значению"""
        node = self.head
        while node:
            try:
                if node.data['id'] == user_id:
                    return node.data
                node = node.next_node
            except TypeError:
                print('Данные не являются словарем или в словаре нет id')
                node = node.next_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string[1:]
