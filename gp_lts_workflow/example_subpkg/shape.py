import astropy.units as u


class Rectangle:
    """Implement a square.

    Parameters
    ----------
    x : `~astropy.units.Quantity`
        x size
    y : `~astropy.units.Quantity`
        y size
    """

    @u.quantity_input
    def __init__(self, x: u.cm, y: u.cm):
        if x.value <= 0 or y.value <= 0:
            raise ValueError("Dimensions should be positive.")
        self.x = x
        self.y = y

    @property
    def area(self):
        """Rectangle area."""
        return self.x * self.y
