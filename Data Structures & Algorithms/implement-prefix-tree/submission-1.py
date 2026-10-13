class PrefixTree:

    def __init__(self):
        # Leaves are a dictionary where the key is the char and the value is more trees.
        self.leaves = {}

    def insert(self, word: str) -> None:
        if len(word) == 0:
            return 
        terminal = len(word) == 1
        if word[0] not in self.leaves.keys():
            self.leaves[word[0]] = (PrefixTree(), terminal)
        
        if terminal and not self.leaves[word[0]][1]:
            self.leaves[word[0]] = (self.leaves[word[0]][0], terminal)
        self.leaves[word[0]][0].insert(word[1:])

    def search(self, word: str) -> bool:
        
        if len(word) == 0:
            return False
        #print("Word", word, self.leaves.keys())
        if word[0] not in self.leaves.keys():
            #print("F")
            return False
        
        #print("Word2", word, self.leaves[word[0]].leaves.keys())
        #print("Word2", word, len(word) == 1, not self.leaves[word[0]].leaves)
        if len(word) == 1 and self.leaves[word[0]][1]:
            #print("T")
            return True
        #print("R")
        return self.leaves[word[0]][0].search(word[1:])
        

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return False

        if prefix[0] not in self.leaves.keys():
            return False
        elif len(prefix) == 1:
            return True
        else:
            return self.leaves[prefix[0]][0].startsWith(prefix[1:])
        
        