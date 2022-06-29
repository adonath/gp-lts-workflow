import astropy.units as u

class Square:
    """Implement a square.

    Parameters
    ----------
    x : `~astropy.units;Quantity`
        x size
    y : `~astropy.units;Quantity`
        y size
    """
    @u.quantity_input
    def __init__(self, x: u.cm, y: u.cm):
        self.x = x
        self.y = y

    @property
    def area(self):
        return self.x * self.y
    