# read version from installed package
from importlib.metadata import version
from .juskata import *

__version__ = version("juskata")
