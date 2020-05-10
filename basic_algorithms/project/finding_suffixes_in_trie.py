from collections import defaultdict
from ipywidgets import interact


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)

    def insert(self, char):
        return self.children[char]

    def suffixes(self, suffix=''):
        suffix_list = []

        if self.is_word and suffix:
            suffix_list.append(suffix)

        for char, trie_node in self.children.items():
            suffix_list.extend(trie_node.suffixes(suffix + char))

        return suffix_list


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            node = node.insert(char)

        node.is_word = True

    def find(self, prefix):
        node = self.root

        for char in prefix:
            node = node.children[char]

        return node


trie = Trie()

words = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]

for word in words:
    trie.insert(word)


def f(prefix):
    if prefix != '':
        prefix_node = trie.find(prefix)
        if prefix_node:
            print('\n'.join(prefix_node.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


interact(f, prefix='')
f(prefix='t')
