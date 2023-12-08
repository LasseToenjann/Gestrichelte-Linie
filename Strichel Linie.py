#Strichel Linie

from turtle import *

distanz = numinput("Länge","Wie lang soll die gestrichelte Linie sein?")
striche = int(numinput("Striche","Wie viele Striche soll ihre Linie haben?"))

def jump(strich):
    penup()
    forward(strich)
    pendown()

def strichel(distanz,striche):
    spruenge = striche - 1
    strich = distanz / (striche + spruenge)
    for i in range(spruenge):
        fd(strich)
        jump(strich)
    fd(strich)

strichel(distanz,striche)

done()