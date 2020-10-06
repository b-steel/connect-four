from mamba import description, context, it, before, after
from expects import *
from expects.aliases import *
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
    .place_marker(self, color) - sets marker attr, or raises error if already taken


Frame
    ATTRIBUTES
    ._slots - dict of all the slots with sub-dicts of all teh rows, indices are from left to right, bottom to top, each is a Place

    METHODS
    .is_valid - returns T/F for if a slot is full or if out of bounds
    .check_win - checks if a player has won, returns player or False
    .place_piece - places a piece in a slot
    .__str__ - prints the frame in prettyprint

Game
    ATTRIBUTES
    ._frame - the Frame instance
    ._markers - dict of the markers used
    ._turn - the turn count

    METHODS
    @property
    .game_over - checks if the game is over or not  - calls Frame.check_win
    .show - prints the frame along with the turn and who's playing next
    .take_turn - shows, then prompts, then does
    .promt - prompts user for input
    .play - plays a whole game


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

        with before.all:
            self.p.place_marker('Red')

        with it('changes the color'):
            expect(self.p._color).to(equal('Red'))

        with it('changes _open'):
            expect(self.p._open).to(be(False))

        with it('accepts even if not open'):
            self.p.place_marker('Blue')
            expect(self.p._color).to(equal('Blue'))

# Frame Tests
# with description('Frame Class') as self:
    
#     with before.each:
#         #initialize a new frame before every test
#         self.f = Frame()

#     with context('Attributes'):

#         with context('._slots'):
            
#             with it('Has the right length (number of columns)'):
#                 expect(len(self.f._slots)).to(equal(7))

#             with it('has sub-dicts of length 6 for the rows'):
#                 expect(len(self.f._slots[0])).to(equal(6))

#     with context('Methods'):

