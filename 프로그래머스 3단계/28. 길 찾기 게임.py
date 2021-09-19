import sys


class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.y
        return self.y > other.y


def addNode(parent, child):
    # left
    if parent.x > child.x:
        if parent.left == None:
            parent.left = child
        else:
            addNode(parent.left, child)
    # right
    else:
        if parent.right == None:
            parent.right = child
        else:
            addNode(parent.right, child)


def preorder(ans, node):
    if node is None:
        return
    ans.append(node.id)
    preorder(ans, node.left)
    preorder(ans, node.right)


def postorder(ans, node):
    if node is None:
        return
    postorder(ans, node.left)
    postorder(ans, node.right)
    ans.append(node.id)


def solution(nodeinfo):
    # 트리깊이 1000 제약 해제(파이썬 기본 1000)
    sys.setrecursionlimit(1500)

    Nodelist = []
    for i in range(len(nodeinfo)):
        Nodelist.append(Node(i + 1, (nodeinfo[i])[0], (nodeinfo[i])[1]))
    Nodelist.sort()

    root = Nodelist[0]
    for i in range(1, len(nodeinfo)):
        addNode(root, Nodelist[i])

    answer = [[], []]
    preorder(answer[0], root)
    postorder(answer[1], root)
    return answer