# Figure out which widget set we are using and import those canvas types
from ginga import toolkit
tkname = toolkit.get_family()

if tkname == 'gtk':
    from ginga.gtkw.ColorBar import *

elif tkname == 'qt':
    from ginga.qtw.ColorBar import *

else:
    # Possible TODO: replace above colorbar implementations with this
    # generic one.
    from .colorbar import *
