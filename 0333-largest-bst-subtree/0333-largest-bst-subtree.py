# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        # bst
        # for each node -> min_val_so_far < node.left < curr_node and max_val_sofar >node.right > curr_node
        self.max_size = 0
        def dfs(node: Optional[TreeNode]) -> tuple[float, float, int]:
            
            if not node:
                return (float('inf'), float('-inf'), 0)

            left_min, left_max, left_size = dfs(node.left)
            right_min, right_max, right_size = dfs(node.right)

            if left_max < node.val < right_min:
                current_size = left_size + right_size + 1
                self.max_size = max(self.max_size, current_size)
                
                new_min = min(left_min, node.val)
                new_max = max(right_max, node.val)
                
                return (new_min, new_max, current_size)
            else:
                return (float('-inf'), float('inf'), 0)

        dfs(root)
        return self.max_size