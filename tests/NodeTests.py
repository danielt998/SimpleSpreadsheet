import unittest

import Node

class TestNodeModule(unittest.TestCase):
    def test_addition_single(self):
        expression = '1+2'

        root_node = Node.construct_ast(expression);
        print(root_node)
        assert len(root_node.child_nodes) == 1
        assert len(root_node.child_nodes[0].child_nodes) == 2