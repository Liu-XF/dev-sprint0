# Polygon excercise from Week 0

# Name:Xuefeng Liu
# I didn't refactor code for this exercise, but instead wrote a function for each step of exercises

from TurtleWorld import * 		
if __name__ == '__main__':
   world = TurtleWorld()							
   bob_polygon = Turtle()
   bob_square = Turtle()
   bob_circle = Turtle()
   bob_arc = Turtle()
    


# This is where you put code to move bob
def square (t, length):
    for x in range(4):
     fd (t, length)
     lt (t)
pass

def polygon (t,length, n):
	for x in range(n):
	  t.fd (length)
	  t.lt (360.0/n)

def circle (t,radius):      #use 30 side polygon to mimic
	for x in range(30):
		t.fd(radius*2*3.1415/30)
		t.lt(360.0/30)

def arc(t,radius, theta):
	for x in range (10):
		distance = radius*2*3.1415*theta/360
		t.fd(distance/10)
		t.lt(theta/10.0)


square (bob_square,50)

bob_polygon.pu()
bob_polygon.fd(100)
bob_polygon.pd ()
polygon (bob_polygon,50,5)

bob_circle.pu ()
bob_circle.bk (100)
bob_circle.pd ()
circle (bob_circle,50)

bob_arc.pu()
bob_arc.lt()
bob_arc.fd(100)
bob_arc.pd()
arc(bob_arc, 30, 120)

wait_for_user()		
		
