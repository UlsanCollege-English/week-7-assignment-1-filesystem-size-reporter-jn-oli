from collections import deque

class Node:
    def __init__(self, name, size, children=None):
        self.name = name
        self.size = size
        self.children = children if children is not None else []


def total_size(root):
    """Return total size of a node (sum of its own size and all descendants)."""
    if root is None:
        return 0

    total = root.size
    for child in root.children:
        total += total_size(child)
    return total


def folder_sizes(root):
    """
    Return a map: folder_name -> total size of folder contents.
    Only folders that have children count, files never included.
    """
    if root is None:
        return {}

    result = {}

    def dfs(node):
        # Only folders (nodes with children)
        if node.children:
            result[node.name] = total_size(node)
            for c in node.children:
                dfs(c)

    dfs(root)
    return result


def level_order(root):
    """
    Return list of lists by BFS, each level containing node names.
    """
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.name)
            for c in node.children:
                queue.append(c)
        result.append(level)

    return result
