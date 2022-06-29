import numpy as np
import astropy.units as u


class Rectangle:
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
        if x.value <= 0 or y.value <= 0:
            raise ValueError("Dimensions should be positive.")
        self.x = x
        self.y = y

    @property
    def area(self):
        """Rectangle area."""
        return self.x * self.y

class Circle:
    """Implement a circle.

    Parameters
    ----------
    r : `~astropy.units;Quantity`
        radius
   """

    @u.quantity_input
    def __init__(self, r: u.cm):
        if r.value <= 0:
            raise ValueError("Dimensions should be positive.")
        self.r = r

    @property
    def area(self):
        """Circle area."""
        return np.pi*self.r**2
