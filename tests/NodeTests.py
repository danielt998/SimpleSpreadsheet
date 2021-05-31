import unittest

import Node

class TestNodeModule(unittest.TestCase):
    def test_addition_single(self):
        expression = '1+2'

        root_node = Node.construct_ast(expression);
        print(root_node)
        assert len(root_node.child_nodes) == 1
        assert len(root_node.child_nodes[0].child_nodes) == 2

        result = Node.evaluate(root_node)
        assert result == 3

    def test_addition_multiple(self):
        expression = '1+2+3+4'

        root_node = Node.construct_ast(expression);
        print(root_node)
        assert len(root_node.child_nodes) == 2
        assert len(root_node.child_nodes[1].child_nodes) == 2

        result = Node.evaluate(root_node)
        assert result == 10