# Flower excercise (4.2) from Week 0

# Name: Xuefeng Liu

from sib_polygon import *

from TurtleWorld import * 	
if __name__ == '__main__':	
	world = TurtleWorld()			
	bob = Turtle ()	

# This is where you put code to move bob


def Flower_piece(t, radius, theta):
    arc(t, radius, theta)
    t.lt(180-theta)
    arc(t, radius, theta)
    t.lt(180-theta)

def Flower (t, radius, theta, n):
	for x in range (n):
		Flower_piece (t,radius, theta)
		t.lt (360/n) 
		

Flower (bob,100,50,4)   

wait_for_user()

