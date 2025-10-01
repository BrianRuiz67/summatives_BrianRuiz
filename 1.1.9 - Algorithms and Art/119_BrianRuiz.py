import turtle as trtl
import random as rand
#names
pizza=trtl
#trtl.addshape("per",(()))
pep= trtl.Turtle(shape='circle')
mush=trtl.Turtle(shape='turtle')
pep.color("firebrick")
mush.color("olive")
#color of pizza crust
pizza.color("sandybrown")
pizza.fillcolor("gold")
#draw pizza shape
pizza.pensize(50)
pizza.penup()
pizza.goto(0,-250)
pizza.pendown()
pizza.begin_fill()
pizza.circle(275)
#draw crust
pizza.end_fill()
pizza.penup()
#pepperoni
#draw pep
pep_q=trtl.textinput('pep','would you like pepperoni?(y/n)')
if pep_q== 'y':
    pep_q2=trtl.textinput('pep','how much pepperoni do you want (little, normal,alot)')
    if pep_q2== 'alot':

        for r in range(100):
            pep.penup()
            pep.stamp()
            randx= rand.randint(-137,137)
            randy= rand.randint(-137,137)
            if pep.distance(0, 0) <= 225:
            
                pep.goto(randx, randy)
                pep.stamp()
    if pep_q2== 'normal':

        for r in range(20):
            pep.stamp()
            randx= rand.randint(-137,137)
            randy= rand.randint(-137,137)
            if pep.distance(0, 0) <= 225:
            
                pep.goto(randx, randy)
                pep.stamp()
    if pep_q2=='little':

        for r in range(10):
            pep.stamp()
            randx= rand.randint(-137,137)
            randy= rand.randint(-137,137)
            if pep.distance(0, 0) <= 225:
            
                pep.goto(randx, randy)
                pep.stamp()
mush_q=trtl.textinput('mush','would you like mushroom?(y/n)')
if mush_q == 'y':
    for r in range(5):
        mush.stamp()
        randx= rand.randint(-137,137)
        randy= rand.randint(-137,137)
        if mush.distance(0, 0) <= 225:
        
            mush.goto(randx, randy)
            mush.stamp()


#after this i want to stamp red circle and lines at random 
'''pizza.circle(2)
import random 
sauce_shapes =["circle", "turtle"]'''
''''
pizza.penup()
pizza.goto(0,-225)
pizza.pendown()
pizza.circle(250)
''' 





wn = trtl.Screen()
wn.mainloop()