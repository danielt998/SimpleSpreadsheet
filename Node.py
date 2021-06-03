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
    operators = ['+', '*'] # BODMAS
    for operator in operators:
        sections = expression.split(operator, maxsplit=1)
        if len(sections) > 1:
            lhs = recursive_parse(sections[0])
            rhs = recursive_parse(sections[1])
            operator_node = Node(NodeType.OPERATOR, operator, [lhs, rhs])
            return operator_node
    return Node(NodeType.RAW_VALUE, expression)



def evaluate(root_node):
    if root_node.nodeType == NodeType.OPERATOR:
        if root_node.value == '+':
            return evaluate(root_node.child_nodes[0]) + evaluate(root_node.child_nodes[1])
        elif root_node.value == '*':
            return evaluate(root_node.child_nodes[0]) * evaluate(root_node.child_nodes[1])

    if root_node.nodeType == NodeType.RAW_VALUE:
        return int(root_node.value)