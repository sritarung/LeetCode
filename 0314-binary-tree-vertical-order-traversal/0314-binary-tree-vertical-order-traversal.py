# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hm = defaultdict(list)

        def helper(node, row, col):
            if not node:
                return

            hm[col].append((row, node.val))
            helper(node.left, row + 1, col - 1)
            helper(node.right, row + 1, col + 1)

        helper(root, 0, 0)

        answer = []

        for col in sorted(hm.keys()):
            a = []
            temp = sorted(hm[col], key= lambda x: x[0])
            for _, val in temp:
                a.append(val)
            answer.append(a)

        return answer
                    