# A drunk pirate makes a random turn and then takes 100 steps forward, makes another random turn, takes another 100 steps, turns another random amount, etc.
# A social science student records the angle of each turn before the next 100 steps are taken.
# Her experimental data is 160, -43, 270, -97, -43, 200, -940, 17, -86. (Positive angles are counter-clockwise.) 
# Use a turtle to draw the path taken by our drunk friend.

import turtle
exp_data_angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

wn = turtle.Screen()
drunk_walk = turtle.Turtle()

for angle in exp_data_angles:
  drunk_walk.forward(100)
  drunk_walk.left(angle)

wn.exitonclick()
