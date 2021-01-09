#   a123_apple_1.py
import turtle as trtl
import random as rand
import math

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

apple = trtl.Turtle()
drawer = trtl.Turtle()

apple_list = []
active_letters = []

#completedletters = 0
drawx = -200
drawy = 200


#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  trtl.penup()
  drawer.penup()
  apple.penup()
  active_apple = trtl.Turtle()
  apple_list.append(active_apple)
  active_apple.shape(apple_image)
  active_apple.speed(0)
  wn.update()

def fall():
  for i in range (20):
    active_apple.penup()
    active_apple.setheading(-90)
    active_apple.forward(10)
  active_apple.clear()
  active_apple.hideturtle()

def draw_a_letter(letter):
  drawer.penup()
  drawer.goto(drawx,drawy)
  drawer.pendown()
  drawer.color("blue")
  drawer.write(letter, font=("Arial", 55, "bold"))
  drawer.penup()

def letter1():
  fall()
  #active_letters.remove(active_letters[0])

def letter2():
  fall()
  #active_letters.remove(active_letters[0])

def letter3():
  fall()
  #active_letters.remove(active_letters[0])

def letter4():
  fall()
  #active_letters.remove(active_letters[0])

def letter5():
  fall()
  #active_letters.remove(active_letters[0])

#-----function calls-----

for i in range (5):
  draw_apple(apple)
  apple_list[i].penup()
  newxpos = rand.randint(-180,180)
  newypos = rand.randint(0,150)
  apple_list[i].goto(newxpos,newypos)

for active_apple in apple_list:
  i = rand.choice(letters)
  letters.remove(i)
  active_letters.append(i)
  draw_a_letter(i)
  drawx = drawx + 60

for active_apple in apple_list:
  wn.onkeypress(letter1, active_letters[0])
  wn.onkeypress(letter2, active_letters[1])
  wn.onkeypress(letter3, active_letters[2])
  wn.onkeypress(letter4, active_letters[3])
  wn.onkeypress(letter5, active_letters[4])

#while completedletters != 5:
  #active_letters.remove(active_letters[0])
  #completedletters = completedletters + 1

wn.listen()
wn.mainloop()
