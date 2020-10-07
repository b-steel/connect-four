from mamba import description, context, it, before, after
from expects import *
from expects.aliases import *
from connect_four import Game
from frame import Frame
from place import Place
doc = '''

Place
    ATTRIBUTES
    ._slot - which slot it's in
    ._row - which row it's in
    ._open - if a marker is not there
    ._color - what the color is
    ._left - plce to the left
    ._right - place to the right
    ._up - place above
    ._down - place below
    ._upright - place up and right
    ._upleft -
    ._downright - 
    ._downleft - 



    
    METHODS
    .place_marker(self, color) - sets color attribute and open attribute


Frame
    ATTRIBUTES
    ._slots - dict of all the slots with sub-dicts of all the rows, indices are from left to right, bottom to top, each is a Place

    METHODS
    ._create_places(self) - creates Place instances and fills the _slots dictionary.  Assigns the adjacent attributes of each place
    .is_valid(self, slot) - returns T/F for if a slot is full or if out of bounds
    .check_win(self) - checks if a player has won, returns player or False
    .place_piece(self, slot, color) - places a piece in a slot
    .__str__(self) - prints the frame in prettyprint

Game
    ATTRIBUTES
    ._frame - the Frame instance
    ._markers - dict of the markers used
    ._players - dict of the players used
    ._turn - the turn count

    METHODS
    @property
    .game_over(self) - checks if the game is over or not  - calls Frame.check_win
    .show(self) - prints the frame along with the turn and who's playing next
    .take_turn(self) - shows, then prompts, then does
    .prompt(self) - prompts user for input
    .play(self) - plays a whole game


'''


#Place Tests
with description('Place Class') as self:
    
    with before.each:
        #initialize a new frame before every test
        self.p = Place()

    with context('Attributes'):

        with it('Initialized to None'):
            expect(self.p._slot).to(be(None))
            expect(self.p._row).to(be(None))
            expect(self.p._open).to(be(True))
            expect(self.p._color).to(be(None))
            expect(self.p._left).to(be(None))
            expect(self.p._right).to(be(None))
            expect(self.p._up).to(be(None))
            expect(self.p._down).to(be(None))
            expect(self.p._upright).to(be(None))
            expect(self.p._upleft).to(be(None))
            expect(self.p._downright).to(be(None))
            expect(self.p._downleft).to(be(None))

    with context('Methods: .place_marker'):

        with before.each:
            self.p = Place()
            self.p.place_marker('Red')

        with it('changes the color'):
            expect(self.p._color).to(equal('Red'))

        with it('changes _open'):
            expect(self.p._open).to(be(False))

        with it('accepts even if not open'):
            self.p.place_marker('Blue')
            expect(self.p._color).to(equal('Blue'))

# Frame Tests
with description('Frame Class') as self:
    
    with before.each:
        #initialize a new frame before every test
        self.f = Frame()

    with context('Attributes'):

        with it('Has the right length (number of columns)'):
            expect(len(self.f._slots)).to(equal(7))

        with it('has sub-dicts of length 6 for the rows'):
            expect(len(self.f._slots[0])).to(equal(6))


    with context('Methods'):
        with before.each:
            self.f = Frame()

        with context ('._create_places'):

            with it('has a Place in each dictionary'):
                expect(self.f._slots[0][0]).to(be_a(Place))
                expect(self.f._slots[1][0]).to(be_a(Place))
                expect(self.f._slots[2][5]).to(be_a(Place))
        
        with context('._set_place_info'):

            with it('a Place in the dictionary knows its place'):
                expect(self.f._slots[0][0]._slot).to(be(0))
                expect(self.f._slots[0][0]._row).to(be(0))
                expect(self.f._slots[2][3]._slot).to(be(2))
                expect(self.f._slots[2][3]._row).to(be(3))
            
            with it('has the correct adjacents'):
                expect(self.f._slots[3][3]._left._slot).to(be(2))
                expect(self.f._slots[3][3]._right._slot).to(be(4))
                expect(self.f._slots[3][3]._up._row).to(be(4))
                expect(self.f._slots[3][3]._down._row).to(be(2))
                expect(self.f._slots[3][3]._upright._row).to(be(4))
                expect(self.f._slots[3][3]._upright._slot).to(be(4))


            with it('Places at edges have None as some of their adjacents'):
                expect(self.f._slots[0][0]._left).to(be(None))
                expect(self.f._slots[0][0]._down).to(be(None))
                expect(self.f._slots[0][0]._right).to(be_a(Place))
                expect(self.f._slots[0][0]._right._slot).to(be(1))
                expect(self.f._slots[0][3]._right._slot).to(be(1))
                expect(self.f._slots[0][3]._right._row).to(be(3))
                expect(self.f._slots[3][0]._downright).to(be(None))
                expect(self.f._slots[3][5]._upleft).to(be(None))

        with context('.is_valid'):

            with it('returns True for a slot with open places'):
                expect(self.f.is_valid(2)).to(be(True))

            with it('returns False for a full slot'):
                self.f._slots[2][5]._open = False
                expect(self.f.is_valid(2)).to(be(False))

            with it('returns False for out of range calls'):
                expect(self.f.is_valid(-1)).to(be(False))
                expect(self.f.is_valid(7)).to(be(False))
        
        with context('.place_piece'):

            with before.each:
                self.f.place_piece(3, 'Red')

            with it('puts a piece in the right slot'):
                expect(self.f._slots[3][0]._open).to(be(False))
                expect(self.f._slots[3][0]._color).to(be('Red'))

            with it('puts a piece on top of other pieces'):
                self.f.place_piece(3, 'Blue')
                expect(self.f._slots[3][1]._open).to(be(False))
                expect(self.f._slots[3][1]._color).to(be('Blue'))

        with context('.check_win'):
            with before.each:
                self.f = Frame()
                self.f._create_places()

            with it('returns False for no win'):
                expect(self.f.check_win()).to(be(False))

            with it('accepts vertical sets'):
                self.f.place_piece(3, 'Red')
                self.f.place_piece(3, 'Red')
                self.f.place_piece(3, 'Red')
                self.f.place_piece(3, 'Red')
                expect(self.f.check_win()).to(be('Red'))

            with it('accepts horizontal sets'):
                self.f.place_piece(1, 'Red')
                self.f.place_piece(2, 'Red')
                self.f.place_piece(3, 'Red')
                self.f.place_piece(4, 'Red')
                expect(self.f.check_win()).to(be('Red'))

            with it('accepts diagonal sets'):
                self.f.place_piece(1, 'Red')

                self.f.place_piece(2, 'Blue')
                self.f.place_piece(2, 'Red')

                self.f.place_piece(3, 'Blue')
                self.f.place_piece(3, 'Blue')
                self.f.place_piece(3, 'Red')

                self.f.place_piece(4, 'Blue')
                self.f.place_piece(4, 'Blue')
                self.f.place_piece(4, 'Blue')
                self.f.place_piece(4, 'Red')
                expect(self.f.check_win()).to(be('Red'))

            with it('returns False if not all are same color'):
                self.f.place_piece(3, 'Red')
                self.f.place_piece(3, 'Red')
                self.f.place_piece(3, 'Blue')
                self.f.place_piece(3, 'Red')
                expect(self.f.check_win()).to(be(False))

        with context('__str__'):
            
            with it('prints blank game'):
                blank = '\t  0 1 2 3 4 5 6\n\t_| | | | | | | |_\n\t_| | | | | | | |_\n\t_| | | | | | | |_\n\t_| | | | | | | |_\n\t_| | | | | | | |_\n\t_| | | | | | | |_\n'
                expect(self.f.__str__()).to(equal(blank))

            with it('prints symbols in there as well'):
                test = '\t  0 1 2 3 4 5 6\n\t_| | | | | | | |_\n\t_| | | | | | | |_\n\t_| | | | | | | |_\n\t_| | | | | | | |_\n\t_| | | | | |R| |_\n\t_| | |R| | |R| |_\n'
                self.f.place_piece(5, 'R')
                self.f.place_piece(5, 'R')
                self.f.place_piece(2, 'R')
                expect(self.f.__str__()).to(equal(test))



# Game Tests

with description('Game Class') as self:

    with context('Attributes'):

        with before.each:
            self.g = Game()

        with it('has a frame'):
            expect(self.g._frame).to(be_a(Frame))     

        with it('starts with _turn as 0'):
            expect(self.g._turn).to(equal(0))

    with context('Methods'):

        with before.each:
            self.g = Game()
            #new instance

        with context('.show'):

            with it('prints the status of a new game'):
                s = '\t  0 1 2 3 4 5 6\n\t_| | | | | | | |_\n\t_| | | | | | | |_\n\t_| | | | | | | |_\n\t_| | | | | | | |_\n\t_| | | | | | | |_\n\t_| | | | | | | |_\n\n\tRound: 0\n\tBlack\'s Turn'
                expect(self.g.show()).to(equal(s))



            
                












            

