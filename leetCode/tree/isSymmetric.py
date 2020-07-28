# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetric(root: TreeNode) -> bool:
	def helper(left, right):
		if not left and not right:
			return True
		if not (left and right):
			return False
		if left.val != right.val:
			return False

		return helper(left.left, right.right) and helper(left.right, right.left)

	return helper(root.left, root.right) if root else True


if __name__ == '__main__':
    print(isSymmetric([1,2,2,3,4,4,3]))