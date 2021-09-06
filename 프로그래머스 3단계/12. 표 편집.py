class Node:
    def __init__(self, data=None, state=1):
        self.data = data
        self.right = None
        self.left = None


class DoubleLinkedList:
    def __init__(self):
        self.header = Node()
        self.tail = Node()
        self.header.right = self.tail
        self.header.left = self.header

        self.tail.right = self.tail
        self.tail.left = self.header
        self.pointer = self.header

    def add(self, node):
        self.pointer.right = node
        node.left = self.pointer
        node.right = self.tail
        self.pointer = node

    def move(self, pointer, v, step):
        for _ in range(step):
            if v == 'D':
                pointer = pointer.right
            else:
                pointer = pointer.left
        return pointer

    def delete(self, pointer):
        if pointer.left == self.header:
            self.header.right = pointer.right
            pointer.right.left = self.header
            return self.header.right

        elif pointer.right == self.tail:
            _pointer = pointer.left
            self.tail.left = _pointer
            _pointer.right = self.tail
            return _pointer

        else:
            _pointer = pointer.right
            pointer.left.right = pointer.right
            pointer.right.left = pointer.left
            return _pointer

    def insert(self, pointer):
        pointer.left.right = pointer
        pointer.right.left = pointer


def get_answer(n, linkedlist):
    answer = ['X' for _ in range(n)]
    pointer = linkedlist.header.right
    while pointer != linkedlist.tail:
        answer[pointer.data] = 'O'
        pointer = pointer.right

    return ''.join(answer)


def solution(n, k, cmd):
    answer = ''
    linkedlist = DoubleLinkedList()
    pointer = linkedlist.header
    stack = []

    for i in range(n): linkedlist.add(Node(i))
    while pointer.data != k: pointer = pointer.right

    for string in cmd:
        if string == 'C':
            stack.append(pointer)
            pointer = linkedlist.delete(pointer)

        elif string == 'Z':
            _pointer = stack.pop()
            linkedlist.insert(_pointer)

        else:
            v, step = string.split()
            pointer = linkedlist.move(pointer, v, int(step))

    answer = get_answer(n, linkedlist)
    return answer