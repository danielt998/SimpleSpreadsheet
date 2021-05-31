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
        self.recursive_to_str(indent=0)

    def recursive_to_str(self, indent):
        print(' ' * indent, end='')
        print('|' + self.value)
        for child_node in self.child_nodes:
            child_node.recursive_to_str(indent + 1)

    child_nodes = []
    type = NodeType.ROOT_NODE
    value = ''

def construct_ast(expression):
    return Node(NodeType.ROOT_NODE, '', recursive_parse(expression))


def recursive_parse(expression):
    # return list of nodes
    #start with + as a test

    plus_sections = expression.split('+')
    if len(plus_sections) == 1:
        return Node(NodeType.OTHER, expression)

    nodeList = []
    for i in range(len(plus_sections) -1):
        lhs = Node(NodeType.OTHER, plus_sections[i -1])
        rhs = Node(NodeType.OTHER, plus_sections[i])
        plusNode = Node(NodeType.OPERATOR, '+', [lhs, rhs])
        nodeList.append(plusNode)
    return nodeList