# --- Imports ---
import turtle as trtl
import random as rand

# --- Screen setup -------------
wn = trtl.Screen()
wn.setup(width=560, height=360)   # no need to call setup twice

# --- Add images ---------------+
hippo_image = "background.gif"
wn.addshape(hippo_image)          # register the image as a turtle shape
wn.bgpic("background.gif")             # set background image
# --- Create hippo turtle -------------+
hippo = trtl.Turtle(shape=hippo_image)

# --- Ask for player name -------------------------------+
player_name = trtl.textinput("Name", "Enter your name:")

# Validate input (no commas or blank names)
while not player_name or "," in player_name:
    player_name = trtl.textinput("Name", "Please enter a valid name (no commas):")

# --- Keep window open ---
wn.cv._rootwindow.resizanle(False,False)
wn.mainloop()