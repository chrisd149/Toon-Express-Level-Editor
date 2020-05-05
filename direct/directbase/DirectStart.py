# This is a hack fix to get the graphics pipes to load with my
# hacked up Panda3D. If you want to load the level editor
# using DirectX 8 or DirectX 9, uncomment the import for the
# pipe you want to use. Make sure the pipe you want to load
# first is imported first.

# DirectX 9
#try:
#    import libpandadx9
#except:
#    pass

# DirectX 8
#try:
#    import libpandadx8
#except:
#    pass

# OpenGL
try:
    import libpandagl
except:
    pass

print 'DirectStart: Starting the game.'

from direct.showbase import ShowBase
base = ShowBase.ShowBase()
