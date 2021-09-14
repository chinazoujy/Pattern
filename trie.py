# coding=utf-8
# author=tom

import collections as _collections

class TrieNode(object):
    def __init__(self) -> None:
        self.children = _collections.defaultdict(TrieNode)
        self.is_word = False
    
    def __repr__(self) -> str:
        s = ''
        first = True
        for k, v in self.children.items():
            if first:
                if v.is_word:
                    s += '{} -> {}\n'.format(k, v)
                else:
                    s += '{} -> {}'.format(k, v)
                first = False
                continue
            if v.is_word:
                s += '{}\n'.format(k)
            else:
                s += '{} -> {}'.format(k, v)
        return s

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

    def __repr__(self) -> str:
        return repr(self.root).replace("\n\n", "\n").replace("\n\n", "\n")

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
    t.insert("天安门")
    t.insert("广渠门")
    t.insert("西直门")
    t.insert("西弯门")

    print(t)















                