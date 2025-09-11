class TrieNode:
    def __init__(self):  # Fixed: __init__ not _init_
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):  # Fixed: __init__ not _init_
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]  # Fixed: indentation
        node.isEnd = True  # Fixed: indentation, moved outside loop
    
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.isEnd  # Fixed: indentation

# Example usage
trie = Trie()
trie.insert("apple")
trie.insert("app")
print(trie.search("app"))    # True
print(trie.search("apple"))  # True
print(trie.search("appl"))   # False