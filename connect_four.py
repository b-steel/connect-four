
from frame import Frame      

class Game():
    def __init__(self):
        self._frame = Frame()
        self._markers = {0: 'O', 1: 'X'}
        self._players = {0: 'Black', 1: 'White'}
        self._turn = 0

    @property
    def game_over(self):
        pass

    def show(self):
        t = self._frame._print_text()
        t += f'\n\tRound: {self._turn}\n\t{self._players[self._turn%2]}\'s Turn'
        print(t)
        return t

    def take_turn(self):
        '''shows, then prompts, then does'''
        pass

    def prompt(self):
        '''prompts user for input'''
        pass
    
    def play(self):
        pass

f = Frame()
f.check_win()