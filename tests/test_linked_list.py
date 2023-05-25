from src.linked_list import LinkedList
import unittest


class TestStack(unittest.TestCase):

    def test_linked_list(self):
        """Тест кейс класса LinkedList"""
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})

        self.assertEqual(str(ll), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")

