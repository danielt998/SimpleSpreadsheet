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