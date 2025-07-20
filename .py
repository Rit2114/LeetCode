from collections import defaultdict

class Node:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.signature = ""

