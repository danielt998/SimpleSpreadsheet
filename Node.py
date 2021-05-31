from enum import Enum

class NodeType(Enum):
    OPERATOR = 1
    REFERENCE = 2
    RAW_VALUE = 3
    ROOT_NODE = 4
    OTHER = 5

class Node:
    def __init__(self, nodeType, value, childNodes = []):
        self.nodeType=nodeType
        self.value = value
        self.child_nodes = childNodes

    def __str__(self):
        return self.recursive_to_str(indent=0)

    def recursive_to_str(self, indent):
        str = ''
        str += ' ' * indent
        str += ('|' + self.value + '\n')
        for child_node in self.child_nodes:
            str += child_node.recursive_to_str(indent + 1)
        return str

    child_nodes = []
    type = NodeType.ROOT_NODE
    value = ''

def construct_ast(expression):
    # return Node(NodeType.ROOT_NODE, '', recursive_parse(expression))
    # Do we even need ROOT_NODE type??
    return recursive_parse(expression)

def recursive_parse(expression):
    # return list of nodes
    #start with + as a test

    plus_sections = expression.split('+', maxsplit=1)
    if len(plus_sections) == 1:
        return Node(NodeType.RAW_VALUE, expression)

    lhs = recursive_parse(plus_sections[0])
    rhs = recursive_parse(plus_sections[1])
    plus_node = Node(NodeType.OPERATOR, '+', [lhs, rhs])
    return plus_node

def evaluate(root_node):
    if root_node.nodeType == NodeType.OPERATOR:
        if root_node.value == '+':
            return evaluate(root_node.child_nodes[0]) + evaluate(root_node.child_nodes[1])
    if root_node.nodeType == NodeType.RAW_VALUE:
        return int(root_node.value)