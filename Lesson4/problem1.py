from turtle import *

Tahleek = Turtle()

Tahleek.color('orange')
Tahleek.pensize(5)
Tahleek.speed(8)
Tahleek.shape('turtle')
Tahleek.turtlesize(5,5,5)

for x in range(4):
	Tahleek.forward(80)
	Tahleek.left(50)
	Tahleek.forward(200)
	Tahleek.right(150)
	Tahleek.forward(50)
	Tahleek.circle(25)
	Tahleek.backward(30)
	Tahleek.circle(50)

mainloop()

