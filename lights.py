class Lights:
    # constructor for the class
    def __init__(self, colour):
        self._colour = colour
        self._state = False

    # returns a string to represent the variables of the light e.g Red Light On
    def __str__(self):
        return "{} Light {}".format(self._colour, "Off" if not self._state else "On")
    
    # sets variable colour of the object
    def set_colour(self, colour):
        self._colour = colour
    
    # flips the switch between true and false
    def toggleState(self):
        self._state = not self._state

    colour = property(set_colour)