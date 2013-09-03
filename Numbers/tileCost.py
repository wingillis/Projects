#Calculates the cost of tiles based on user input for 
#width, height, and tile cost

def tileCost(cost, w, h):
	return w*h*cost

print "How much does a square foot of tile cost?"
c = raw_input()

print "What is the width and height in feet, separated by a space?"

w,h = raw_input().split()

try:
	c = float(c)
	w = float(w)
	h = float(h)
	print tileCost(c,w,h)

except:
	print "I'm sorry, you entered invalid arguments,\nplease restart the program and try again.\nExiting"