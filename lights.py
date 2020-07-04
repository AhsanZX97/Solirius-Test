class Lights:
    def __init__(self, colour):
        self._colour = colour
        self._state = False

    def __str__(self):
        return "{} Light {}".format(self._colour,self._state)
    
    def set_colour(self, colour):
        self._colour = colour

    colour = property(set_colour)

light = Lights("Yellow")

print(light)