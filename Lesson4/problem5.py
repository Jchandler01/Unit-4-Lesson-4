from turtle import *

Tahleek = Turtle()

Tahleek.color('orange')
Tahleek.pensize()
Tahleek.speed(3)
Tahleek.shape('turtle')

def drawHexagon():
	for x in range(6):
		Tahleek.forward(30)
		Tahleek.left(60)

for x in range(12):
	drawHexagon()
	Tahleek.left(30)

	

mainloop()