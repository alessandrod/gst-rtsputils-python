try:
    import gstlibtoolimporter
    gstlibtoolimporter.install()
except ImportError:
    pass

from _rtsputils import *
