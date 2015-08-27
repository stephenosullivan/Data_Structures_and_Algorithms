__author__ = 'stephenosullivan'

import re, string


class Trie:
    def __insert(node, item):
        if not item:
            return None
        elif node is None:
            node = Trie.TrieNode(item[0])
            node.follows = Trie.__insert(node.follows, item[1:])
        elif item[0] == node.item:
            node.follows = Trie.__insert(node.follows, item[1:])
        else:
            node.next = Trie.__insert(node.next, item)
        return node

    def __contains(node, item):
        if len(item) == 0:
            return True
        elif node is None:
            return False
        elif item[0] == node.item:
            return Trie.__contains(node.follows, item[1:])
        else:
            return Trie.__contains(node.next, item)

    class TrieNode:
        def __init__(self, item, next=None, follows=None):
            self.item = item
            self.next = next
            self.follows = follows

    def __init__(self):
        self.start = None

    def insert(self, item):
        self.start = Trie.__insert(self.start, item)

    def __contains__(self, item):
        return Trie.__contains(self.start, item)


if __name__ == '__main__':
    firstTrie = Trie()
    with open('./EnglishDict.txt', 'r') as f:
        for line in f:
            word = line.strip() + '$'
            firstTrie.insert(word)

    with open('./Declaration_of_Independence.txt') as f:
        for line in f:
            line = line.replace("'", "")
            punct = string.punctuation
            for s in punct:
                line = line.replace(s, " ")
            words = line.split()
           # punct = re.compile(r'([^A-Za-z0-9 ])')
           # words = punct.sub("", line).split()
            for word in words:
                if word.lower() + '$' not in firstTrie:
                    print(word.lower())