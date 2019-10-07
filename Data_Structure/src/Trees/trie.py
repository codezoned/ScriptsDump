"""
Trie implementation in Python by @Tr-Jono

A trie is a type of search tree that is used for storing strings.
Visual representation of a trie with strings "ab", "ac", "ace", "ba", "boom":

      [root]
      /    \
   "a"     "b"
   / \     / \
 "b" "c" "a" "o"
      |       |
     "e"     "o"
              |
             "m"

The time complexities of addition, removal and querying existence/count of a string are all O(|target string|).

A trie could be used in place of a string list used for searching.
Time complexity of searching a string in:
    - a list: O(|list|)
    - a trie: O(|target string|)

This implementation of the trie relies on recursively stored _TrieNode instances.
The Trie class, acting as the root, implements typical data structure methods.
"""


class _TrieNode:
    def __init__(self):
        self.words = 0
        self.children = {}

    def __len__(self):
        return self.words + sum(len(c) for c in self.children.values())

    def add(self, s):
        if not s:
            self.words += 1
            return
        if s[0] not in self.children:
            self.children[s[0]] = _TrieNode()
        self.children[s[0]].add(s[1:])

    def remove(self, s):
        if not s:
            if not self.words:
                raise ValueError
            self.words -= 1
            return
        if s[0] not in self.children:
            raise ValueError
        self.children[s[0]].remove(s[1:])

    def count(self, s):
        if not s:
            return self.words
        if s[0] not in self.children:
            return 0
        return self.children[s[0]].count(s[1:])

    def get_words(self):
        words = [""] * self.words
        for c in self.children:
            for w in self.children[c].get_words():
                words.append(c + w)
        return words


class Trie:
    def __init__(self, *words):
        self.children = {}
        for w in words:
            self.add(w)

    def __contains__(self, item):
        return bool(self.count(item))

    def __len__(self):
        return sum(len(c) for c in self.children.values())

    def __bool__(self):
        return bool(len(self))

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, ", ".join([repr(w) for w in self.get_words()]))

    def add(self, s):
        if not s:
            raise ValueError("Empty strings disallowed")
        if s[0] not in self.children:
            self.children[s[0]] = _TrieNode()
        self.children[s[0]].add(s[1:])

    def remove(self, s):
        if not s:
            raise ValueError("Empty strings disallowed")
        try:
            if s[0] not in self.children:
                raise ValueError
            self.children[s[0]].remove(s[1:])
        except ValueError:
            raise ValueError("{} not in trie".format(repr(s))) from None

    def count(self, s):
        if s[0] not in self.children:
            return 0
        return self.children[s[0]].count(s[1:])

    def get_words(self):
        words = []
        for c in self.children:
            for w in self.children[c].get_words():
                words.append(c + w)
        return words


def main():
    trie = Trie("dog", "dog", "cat", "tiger")
    trie.add("bird")
    trie.remove("bird")
    print("repr(trie):", trie)
    print("len(trie):", len(trie))
    print("trie.count('dog'):", trie.count("dog"))
    print("'bird' in trie:", "bird" in trie)


if __name__ == "__main__":
    main()
