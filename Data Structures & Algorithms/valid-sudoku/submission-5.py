class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Traverse through sudoku board like reading
        #Store each integers coords in a hash map.
        #Compare coords with hash map coords everytime an integer
        #is found to check for conflicts.
        hash_map = dict()
        
        row_limit = 3
        col_limit = 3
        while row_limit <= 9:
            while col_limit <= 9:
                cell = []
                for i in range(row_limit - 3, row_limit):
                    for j in range(col_limit - 3, col_limit):
                        c = board[i][j]
                        if c != ".":
                            coords = (i, j)
                            if c not in hash_map:
                                if c not in cell:
                                    hash_map[c] = [coords]
                                    cell.append(c)
                                else:
                                    return False
                            elif not self.conflict(coords, hash_map[c]):
                                if c not in cell:
                                    hash_map[c].append(coords)
                                    cell.append(c)
                                else:
                                    return False
                            else:
                                return False
                col_limit += 3  
            col_limit = 3
            row_limit += 3
                 
        return True

    def conflict(self, coords, all_coords):
        for ccoords in all_coords:
            if coords[0] == ccoords[0]:
                return True
            elif coords[1] == ccoords[1]:
                return True
        return False
            



        