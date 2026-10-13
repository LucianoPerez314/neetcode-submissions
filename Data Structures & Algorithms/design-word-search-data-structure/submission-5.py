class WordDictionary:

    def __init__(self):
        # key: letter, value: (WordDictionary, length of branch (not including current node))
        self.leaves = {}

    def addWord(self, word: str) -> None:
        if len(word) == 0:
            return

        curr_leaves = self.leaves
        for i, c in enumerate(word):
            if c not in curr_leaves:
                curr_leaves[c] = (WordDictionary(), False)

            if i == len(word) - 1:
                curr_leaves[c] = (curr_leaves[c][0], True)
            curr_leaves = curr_leaves[c][0].leaves 
        

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return False
        elif word == '.':
            if any(val[1] for val in self.leaves.values()):
                return True
            return False

        curr_leaves = self.leaves
        for i, c in enumerate(word):
            if c != '.':
                if c not in curr_leaves:
                    return False
                if i == len(word)-1 and curr_leaves[c][1]:
                    return True
                curr_leaves = curr_leaves[c][0].leaves 
            else:   
                if i == len(word)-1:
                    if any(val[1] for val in curr_leaves.values()):
                        return True
                    return False 
                for worddict, term in curr_leaves.values():
                    if worddict.search(word[i+1:]):
                        return True
                return False
        return False

                
                    
                
            
            


            
            



            
            



        
