from collections import defaultdict

class Node:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.signature = ""

class Solution:
    def deleteDuplicateFolder(self, paths):
        root = Node("")
        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = Node(folder)
                node = node.children[folder]
        
