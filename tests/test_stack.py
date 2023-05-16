import unittest
from src.stack import Stack, Node


class TestStack(unittest.TestCase):

    def test_node(self):
        item = Node(5, None)
        self.assertEqual(item.data, 5)
        self.assertEqual(item.next_node, None)

    def test_stack(self):
        item = Stack()
        self.assertEqual(item.top, None)
        item.push(5)
        item.push(25)
        item.push(225)
        self.assertEqual(item.top.data, 225)
        self.assertEqual(item.top.next_node.data, 25)
        self.assertEqual(item.top.next_node.next_node.data, 5)

    def test_stuck_push(self):
        item = Stack()
        self.assertEqual(item.push(5), None)

    def test_stuck_pop(self):
        item = Stack()
        item.push(5)
        item.push(55)
        self.assertEqual(item.pop(), 55)
        self.assertEqual(item.top.data, 5)

    def test_str(self):
        item = Stack()
        self.assertEqual(str(item), '')
        item.push(5)
        item.push(55)
        self.assertEqual(str(item), '55\n5\n')
