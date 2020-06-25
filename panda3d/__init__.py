"Python bindings for the Panda3D libraries"

__version__ = '1.11.0'

if __debug__:
    import sys
    if sys.version_info < (3, 0):
        sys.stderr.write("WARNING: Python 2.7 will reach EOL after December 31, 2019.\n")
        sys.stderr.write("To suppress this warning, upgrade to Python 3.\n")
        sys.stderr.flush()
    del sys
