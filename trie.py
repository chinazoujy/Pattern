# coding=utf-8
# author=tom

import collections as _collections

class Trie(_collections.MutableMapping):
    
    def __init__(self) -> None:
        self.root = None 