import random
import math
import sys
sys.path.append(r"C:\Temp\devel\cTurtle")
import cTurtle



def lsystem(axiom,rules,depth,initialPosition,heading,angle,length):
	aTurtle = cTurtle.Turtle()
	aTurtle.up()
	aTurtle.setposition(initialPosition)
	aTurtle.down()
	aTurtle.setheading(heading)
	newRules = applyProduction(axiom,rules,depth)
	drawLS(aTurtle,newRules,angle,length)
	aTurtle.exitOnClick()

def drawLS(aTurtle,instructions,angle,distance):
	stateSaver = []
	for cmd in instructions:
		if cmd == 'F' :
			aTurtle.forward(distance)
		elif cmd == 'B' :
			aTurtle.backward(distance)
		elif cmd == '+' :
			aTurtle.right(angle)
		elif cmd == '-' :
			aTurtle.left(angle)
		elif cmd == '[' :
			pos = aTurtle.position()
			head = aTurtle.heading()
			stateSaver.append((pos,head))
		elif cmd ==	']' :
			pos,head = stateSaver.pop()
			aTurtle.up()
			aTurtle.setposition(pos)
			aTurtle.setheading(head)
			aTurtle.down()

def applyProduction(axiom,rules,n):
	for i in range(n):
		newString = ""
		for ch in axiom:
			newString = newString + rules.get(ch,ch)
		axiom = newString
	return axiom			
			
myRules={'X' : 'F[-X]+X', 'F':'FF'}

myRules={'H' : 'HFX[+H][−H]', 'X':'X[−FFF][+FFF]FX'}
axiom= 'H'
lsystem(axiom,myRules,7,(0,-200),90,30,2)

#donut
myRules={ 'F':'F–F–F–GG', 'G':'GG'}
axiom= 'F–F–F'

#tree/leaves
myRules={ 'F':'F–F–F–GG', 'F':'FF+[+F–F–F]–[–F+F+F]'}
axiom= 'F–F–F'
lsystem(axiom,myRules,7,(0,-200),60,30,10)


lsystem(axiom,myRules,7,(0,-200),90,30,2)


