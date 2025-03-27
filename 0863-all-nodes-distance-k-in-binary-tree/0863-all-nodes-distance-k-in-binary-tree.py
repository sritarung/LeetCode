# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Step 1: Build an adjacency list (Graph Representation)
        graph = defaultdict(list)

        def build_graph(node: Optional[TreeNode], parent: Optional[TreeNode]):
            if not node:
                return
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            build_graph(node.left, node)
            build_graph(node.right, node)

        build_graph(root, None)

        # Step 2: BFS from the target node
        queue = deque([target.val])
        visited = set([target.val])
        distance = 0

        while queue:
            if distance == k:
                return list(queue)  # Nodes at distance K
            for _ in range(len(queue)):  # Process all nodes at the current level
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            distance += 1

        return []