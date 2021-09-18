# coding=utf-8
# author=tom

import collections as _collections

# dfs
def node_print(current_node, current_str):
    if len(current_node.children) == 0:
        print (current_str)

    for k,v in current_node.children.items():
        current_str += k
        node_print(v, current_str)
        current_str = current_str[0:-1]

class TrieNode(object):
    def __init__(self) -> None:
        self.children = _collections.defaultdict(TrieNode)
        self.is_word = False

class Trie(object):
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word) -> None:
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True
    
    def search(self, word) -> bool:
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.is_word

    def starts_with(self, prefix) -> bool:
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True    

    def find_one(self, word) -> str:
        for i in range(len(word)):
            node = self.root.children.get(word[i])
            if not node:
                continue
            for j in range(i+1, len(word)):
                cnode = node.children.get(word[j])
                if cnode and cnode.is_word:
                    return word[i: j+1]
                else:
                    break
        return None

if __name__ == "__main__":
    t = Trie()
    t.insert("123")
    t.insert("456")
    t.insert("451")
    t.insert("789")

    node_print(t.root, "")

    query = "123qqqqq"
    print (t.search(query))
    print (t.starts_with(query))
    














                