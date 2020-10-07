class Place():
    def __init__(self):
        self._slot = None
        self._row = None
        self._open = True
        self._color = None
        self._left = None
        self._right = None
        self._up = None
        self._down = None
        self._upright = None
        self._upleft = None
        self._downright = None
        self._downleft = None
    
    def place_marker(self, color):
        '''Sets color attribute and open attribute'''
        self._color = color
        self._open = False
