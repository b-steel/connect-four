
from frame import Frame      

class Game():
    def __init__(self):
        self._frame = Frame()
        self._markers = {0: u'\u26AB', 1: u'\u26AA'}
        self._players = {0: 'Black', 1: 'White'}
        self._turn = 0

    @property
    def game_over(self):
        '''Returns a Player marker or False'''
        return self._frame.check_win()
    
    @property
    def player(self):
        return self._turn%2

    @property
    def other_player(self):
        return (self._turn + 1)%2

    def _switch_first_player(self):
        if self._players[0] == 'Black':
            self._players = {1: 'Black', 0: 'White'}
            self._markers = {1: u'\u26AB', 0: u'\u26AA'}
        else:
            self._players = {0: 'Black', 1: 'White'}
            self._markers = {0: u'\u26AB', 1: u'\u26AA'}

    def show(self):
        t = self._frame._print_text()
        t += f'\nRound: {self._turn}\n{self._players[self.player]}\'s Turn'
        print(t)
        return t

    def take_turn(self):
        '''shows, then prompts, then does'''
        self.show()
        choice = self.prompt()
        self._frame.place_piece(choice, self._markers[self.player])
        self._turn +=1

    def prompt(self):
        '''prompts user for input'''
        while True:
            choice = input(f'{self._players[self.player]}, please select which Slot you\'d like to play\n')
            try:
                choice = int(choice)
                if choice < 7 and choice >= 0:
                    return choice
                print('Please choose a number between 0 and 6')
            except ValueError as e:
                print(f'{choice} is not a valid input')
        
    def ask_to_play_again(self):
        while True:
            choice = input('Would you like to play again??? <Y/N>\n')
            if choice.lower() == 'y':
                return True
            elif choice.lower() == 'n':
                return False
            print('Please choose either Y or N')

    def play(self):
        print(f'Welcome to Connect Four\n{self._players[self.player]} will play first')
        game = True
        while game:
            self.take_turn()
            if self.game_over:
                self.show()
                print(f'CONGRATULATIONS {self._players[self.other_player]}, you WIN!')
                game = self.ask_to_play_again()
                self._frame = Frame()
                self._turn = 0
                self._switch_first_player()
        print('Thanks for playing!')




if __name__ == '__main__':
    g = Game()
    g.play()
    