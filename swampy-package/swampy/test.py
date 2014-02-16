import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *

def triangle(t, r, angle):
    y = r * math.sin(angle * math.pi / 360)
    fd (t,r)
    lt(t,90+angle/2.0)
    fd(t, 2*y)
    lt(t, 90+angle/2.0)
    fd(t, r)
    lt(t, 180)

def pie(t, r, n):
	angle=360/n
	for i in range (n):
		triangle(t,r,angle)



world=TurtleWorld()
bob =Turtle ()
triangle (bob,50,60)
bob2= Turtle ()
bob2.pu()
bob2.fd(100)
bob2.pd()
pie (bob2, 50, 8)
wait_for_user ()
