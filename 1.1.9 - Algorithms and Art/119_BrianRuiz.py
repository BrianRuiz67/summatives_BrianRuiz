import turtle as trtl

#names
pizza=trtl


#color of pizza crust
pizza.color("wheat")
pizza.fillcolor("tomato")
#draw pizza shape
pizza.pensize(50)
pizza.penup()
pizza.goto(0,-250)
pizza.pendown()
pizza.begin_fill()
pizza.circle(275)
#draw crust
pizza.end_fill()
''''
pizza.penup()
pizza.goto(0,-225)
pizza.pendown()
pizza.circle(250)
'''





wn = trtl.Screen()
wn.mainloop()