
class Node:
	def __init__(self, data, left, right):
		self.data = data
		self.left = left
		self.right = right
def preOrder(node):
	print(node.data, end = '')
	if node.left != '.':
		preOrder(tree[node.left])
	if node.right != '.':
		preOrder(tree[node.right])

def inorder(node):
	if node.left != '.':
		inorder(tree[node.left])
	print(node.data, end = '')
	if node.right != '.':
		inorder(tree[node.right])
		
def postorder(node):
	if node.left != '.':
		postorder(tree[node.left])
	if node.right != '.':
		postorder(tree[node.right])
	print(node.data, end = '')


if __name__ == "__main__":
	n = int(input())
	tree = {}
	for i in range(n):
		data, left, right = map(str, input().split())
		tree[data] = Node(data = data, left = left, right = right)
	preOrder(tree['A'])
	print()
	inorder(tree['A'])
	print()
	postorder(tree['A'])

"""
전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
"""