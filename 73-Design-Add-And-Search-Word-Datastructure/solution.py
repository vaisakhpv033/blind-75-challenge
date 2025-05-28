# link:https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        current = self.root
        for val in word:
            if val not in current.children:
                current.children[val] = TrieNode()
            current = current.children[val]
        current.is_end = True
        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            current = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in current.children.values():
                        if dfs(i+1, child):
                            return True
                    return False

                else:
                    if c in current.children:
                        current = current.children[c]
                    else:
                        return False
            return current.is_end
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)