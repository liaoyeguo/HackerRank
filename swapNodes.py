#!/bin/python
from __future__ import print_function
import math


class Node:

    def __init__(self, value, depth):
        self.value = value
        self.left = None
        self.right = None
        self.depth = depth


def swapNodes(indexes, queries):
    root = Node(1, 1)
    nodes = [root]
    for idx, val in enumerate(indexes):
        if val[0] > 0:
            nodes[idx].left = Node(val[0], nodes[idx].depth + 1)
            nodes.append(nodes[idx].left)
        if val[1] > 0:
            nodes[idx].right = Node(val[1], nodes[idx].depth + 1)
            nodes.append(nodes[idx].right)

    results = []
    for que in queries:
        stack = [root]
        while len(stack) > 0:
            cur = stack.pop()
            if cur.depth % que == 0:
                cur.left, cur.right = cur.right, cur.left
            if cur.right is not None:
                stack.append(cur.right)
            if cur.left is not None:
                stack.append(cur.left)

        result = []
        cur = root
        while True:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            elif len(stack) > 0:
                cur = stack.pop()
                result.append(cur.value)
                cur = cur.right
            else:
                break
        results.append(result)
    return results


print(swapNodes([[2, 3],
                 [-1, 4],
                 [-1, 5],
                 [-1, -1],
                 [-1, -1]], [2]))
