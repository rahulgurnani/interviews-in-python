class TreeNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TreeNode()

    def add_string(self, s):
        current = self.root
        for ch in s:
            if ch in current.children:
                current = current.children[ch]
                continue
            else:
                current.children[ch] = TreeNode()
                current = current.children[ch]
        current.end = True

    def search_string(self, s):
        current = self.root
        for ch in s:
            if ch in current.children:
                current = current.children[ch]
            else:
                return False

        return current.end


trie = Trie()
trie.add_string("rahul")
trie.add_string("ramma")
print(trie.search_string("ram"))
