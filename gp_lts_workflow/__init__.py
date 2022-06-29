# Licensed under a 3-clause BSD style license - see LICENSE.rst

# Packages may add whatever they like to this file, but
# should keep this content at the top.
# ----------------------------------------------------------------------------
from ._astropy_init import *   # noqa
# ----------------------------------------------------------------------------

__all__ = []
from .example_mod import *   # noqa
from .example_subpkg import Rectangle
# Then you can be explicit to control what ends up in the namespace,
__all__ += ['do_primes', 'Rectangle']   # noqa
# or you can keep everything from the subpackage with the following instead
# __all__ += example_mod.__all__
