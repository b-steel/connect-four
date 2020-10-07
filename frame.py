from place import Place
class Frame():
    def __init__(self):
        '''self._slots is dict of all the slots with sub-dicts of all the rows, indices are from left to right, bottom to top, each is a Place'''
        self._slots = {}
        self._create_places()
        self._set_place_info()


    def _create_places(self):
        '''creates Place instances and fills the _slots dictionary'''  
        
        #Fill dict w/ blank Places
        for col in range(7):
            self._slots[col] = {}
            for row in range(6):
                self._slots[col][row] = Place()
                self._slots[col][row]._slot = col
                self._slots[col][row]._row = row


    def _set_place_info(self):  
        '''Assigns the adjacent attributes of each place'''

        #Set adjacents - internal
        for col in range(1,6):
            for row in range(1,5):
                p = self._slots[col][row]
                p._left = self._slots[col-1][row]
                p._right= self._slots[col+1][row]
                p._up = self._slots[col][row+1]
                p._down  = self._slots[col][row-1]
                p._upright  = self._slots[col+1][row+1]
                p._upleft = self._slots[col-1][row+1]
                p._downright = self._slots[col+1][row-1]
                p._downleft = self._slots[col-1][row-1]

        #set adjacents - top row
        for col in range(1,6):
            row = 5
            p = self._slots[col][row]
            p._left = self._slots[col-1][row]
            p._right= self._slots[col+1][row]
            p._down  = self._slots[col][row-1]
            p._downright = self._slots[col+1][row-1]
            p._downleft = self._slots[col-1][row-1]

        #set adjacents - bottom row
        for col in range(1,6):
            row = 0
            p = self._slots[col][row]
            p._left = self._slots[col-1][row]
            p._right= self._slots[col+1][row]
            p._up = self._slots[col][row+1]
            p._upright  = self._slots[col+1][row+1]
            p._upleft = self._slots[col-1][row+1]

        #set adjacents - right side
        col = 6
        for row in range(1,5):
            p = self._slots[col][row]
            p._left = self._slots[col-1][row]
            p._up = self._slots[col][row+1]
            p._down  = self._slots[col][row-1]
            p._upleft = self._slots[col-1][row+1]
            p._downleft = self._slots[col-1][row-1]

        #set adjacents - left side
        col = 0
        for row in range(1,5):
            p = self._slots[col][row]
            p._right= self._slots[col+1][row]
            p._up = self._slots[col][row+1]
            p._down  = self._slots[col][row-1]
            p._upright  = self._slots[col+1][row+1]
            p._downright = self._slots[col+1][row-1]
        
        #set topleft
        p = self._slots[0][5]
        p._right= self._slots[1][5]
        p._down  = self._slots[0][4]
        p._downright = self._slots[1][4]

        #set topright
        p = self._slots[6][5]
        p._left = self._slots[5][5]
        p._down  = self._slots[6][4]
        p._downleft = self._slots[5][4]

        #set bottomleft
        p = self._slots[0][0]
        p._right= self._slots[1][0]
        p._up = self._slots[0][1]
        p._upright  = self._slots[1][1]

        #set bottomright
        p = self._slots[6][0]
        p._left = self._slots[5][0]
        p._up = self._slots[6][1]
        p._upleft = self._slots[5][1]
                

    def is_valid(self, slot):
        '''returns T/F for if a slot is full or if out of bounds'''
        if slot < 0 or slot > 6: 
            return False
        elif self._slots[slot][5]._open == False:
            return False
        return True

    def check_win(self):
        '''checks if a player has won, returns player or False'''
        # create list of zip objects.  Each zip object represents a potential win.  The zip object has 4 pairs of col,row indices
        wins = []
        rowset = [[0,1,2,3] , [1,2,3,4] , [2,3,4,5]]
        colset = [[0,1,2,3] , [1,2,3,4] , [2,3,4,5] , [3,4,5,6]]
        #vertical wins
        for col in range(7):
            for item in rowset:
               wins.append(zip([col]*4, item))
        #horizontal wins
        for row in range(6):
            for item in colset:
                wins.append(zip(item, [row]*4))
        #rising Diagonal wins
        for row in rowset:
            for col in colset:
                wins.append(zip(col, row))
        #sinking diagonal wins
        for row in rowset:
            for col in colset:
                wins.append(zip(col,row[::-1]))

        #check each
        for w in wins:
            colors = [self._slots[col][row]._color for (col, row) in w]
            if None in colors:
                pass
            elif colors.count(colors[0])==4:
                return colors[0]
        return False


    def place_piece(self, slot, color):
        '''places a piece in a slot.  Assumed to be a valid play'''
        spot = 0
        for row in range(4,-1,-1):
            if not self._slots[slot][row]._open:
                spot = row+1
                break
        self._slots[slot][spot].place_marker(color)


    def _print_text(self):
        #for creating the text template
        # s = '\t  0 1 2 3 4 5 6\n'  
        # for row in range(5, -1, -1):
        #     s += '\t_'
        #     for col in range(7):
        #         s+=f'|{{self._slots[{col}][{row}]._color or "  "}}'
        #     s+='|_\n'
        # blank = '\t  0 1 2 3 4 5 6\n\t_| | | | | | | |_\n\t_| | | | | | | |_\n\t_| | | | | | | |_\n\t_| | | | | | | |_\n\t_| | | | | | | |_\n\t_| | | | | | | |_\n'

        #It's gonna get MESSY lookin'
        text = f'  0  1  2  3  4  5  6\n_|{self._slots[0][5]._color or "  "}|{self._slots[1][5]._color or "  "}|{self._slots[2][5]._color or "  "}|{self._slots[3][5]._color or "  "}|{self._slots[4][5]._color or "  "}|{self._slots[5][5]._color or "  "}|{self._slots[6][5]._color or "  "}|_\n_|{self._slots[0][4]._color or "  "}|{self._slots[1][4]._color or "  "}|{self._slots[2][4]._color or "  "}|{self._slots[3][4]._color or "  "}|{self._slots[4][4]._color or "  "}|{self._slots[5][4]._color or "  "}|{self._slots[6][4]._color or "  "}|_\n_|{self._slots[0][3]._color or "  "}|{self._slots[1][3]._color or "  "}|{self._slots[2][3]._color or "  "}|{self._slots[3][3]._color or "  "}|{self._slots[4][3]._color or "  "}|{self._slots[5][3]._color or "  "}|{self._slots[6][3]._color or "  "}|_\n_|{self._slots[0][2]._color or "  "}|{self._slots[1][2]._color or "  "}|{self._slots[2][2]._color or "  "}|{self._slots[3][2]._color or "  "}|{self._slots[4][2]._color or "  "}|{self._slots[5][2]._color or "  "}|{self._slots[6][2]._color or "  "}|_\n_|{self._slots[0][1]._color or "  "}|{self._slots[1][1]._color or "  "}|{self._slots[2][1]._color or "  "}|{self._slots[3][1]._color or "  "}|{self._slots[4][1]._color or "  "}|{self._slots[5][1]._color or "  "}|{self._slots[6][1]._color or "  "}|_\n_|{self._slots[0][0]._color or "  "}|{self._slots[1][0]._color or "  "}|{self._slots[2][0]._color or "  "}|{self._slots[3][0]._color or "  "}|{self._slots[4][0]._color or "  "}|{self._slots[5][0]._color or "  "}|{self._slots[6][0]._color or "  "}|_\n'

        return text

    def __str__(self):
        return self._print_text()


        

