import sys

# Day 23: BST Level-Order Traversal
# https://www.hackerrank.com/challenges/30-binary-trees/problem


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data

class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        queue = []

        if root is not None:
            queue.insert(0, root)

            while len(queue) > 0:
                node = queue.pop()

                if node is not None:
                    print(node.data, end = " ")

                    if node.left is not None:
                        queue.insert(0, node.left)

                    if root.right is not None:
                        queue.insert(0, node.right)

if __name__ == "__main__":
    T = int(input())
    myTree = Solution()
    root = None
    for i in range(T):
        data = int(input())
        root = myTree.insert(root, data)
    myTree.levelOrder(root)
