import turtle as trtl
import time
import math

wn = trtl.Screen()
player = trtl.Turtle()
playerlist = []
playerlist.append(player)
player.color("white")
bullet_list = []
enemybullet_list = []
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(400, 300)
score_writer.pencolor("white")
score_writer.pendown()
invader = "invader.gif"
wn.addshape(invader)
enemynumber = 5
row1 = []
row2 = []
row3 = []
row4 = []
row5 = []
row6 = []
i = 0
gameover = "false"
level = 1
font_setup = ("Arial", 20, "normal")
score = 0
player.penup()
wn.bgcolor("black")
player.setheading(90)
def setup_player():
  player.hideturtle()
  player.penup()
  player.goto(-400,-220)
  player.pendown()
  player.setheading(0)
  player.pencolor("white")
  player.forward(800)
  player.penup()
  player.goto(0,-200)
  player.setheading(90)
  player.showturtle()
def player_right():
  x = player.xcor()
  if x <= 400:
    player.goto(player.xcor() + 10, player.ycor())
  else:
    print("you cannot go off the screen.")
def player_left():
  x = player.xcor()
  if x >= -400:
    player.goto(player.xcor() - 10, player.ycor())
  else:
    print("you cannot go off the screen.")

def update_score():
  global score
  score += 10
  score_writer.clear()
  scorestr = "Score: " + str(score)
  score_writer.write(scorestr, font=font_setup)

def generateplayerbullet():
  global bullets
  bullets = trtl.Turtle()
  bullets.penup()
  bullets.speed(0)
  bullets.hideturtle()
  bullets.color("red")
  bullets.turtlesize(0.2)
  bullets.shape("circle")
  bullets.setheading(90)
  bullets.goto(player.xcor(), player.ycor())
  bullets.showturtle()
  bullet_list.append(bullets)

def isCollision(t1,t2):
  distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
  if distance < 30:
    return True
  else:
    return False

def generateenemybullet():
  enemyindex = 0
  global enemybullet
  global i
  enemybullet = trtl.Turtle()
  enemybullet_list.append(enemybullet)
  enemybullet.penup()
  enemybullet.speed(0)
  enemybullet.hideturtle()
  enemybullet.color("green")
  enemybullet.turtlesize(0.2)
  enemybullet.shape("circle")
  enemybullet.setheading(270)
  if level == 1:
    enemybullet.goto(row1[enemyindex].xcor(), row1[enemyindex].ycor())
  if level == 2:
    if len(row1) > 0:
      enemybullet.goto(row1[enemyindex].xcor(), row1[enemyindex].ycor())
    if len(row1) + len(row2) > 5 and i == 1:
      enemybullet_list[1].goto(row2[enemyindex].xcor(), row2[enemyindex].ycor())
  if level == 3:
    if len(row1) > 0:
      enemybullet.goto(row1[enemyindex].xcor(), row1[enemyindex].ycor())
    if len(row1) + len(row2) > 5 and i == 1:
      enemybullet_list[1].goto(row2[enemyindex].xcor(), row2[enemyindex].ycor())
    if len(row1) + len(row2) + len(row3) > 10 and i == 2:
      enemybullet_list[2].goto(row3[enemyindex].xcor(), row3[enemyindex].ycor())
  if level == 4:
    if len(row1) > 0:
      enemybullet.goto(row1[enemyindex].xcor(), row1[enemyindex].ycor())
    if len(row1) + len(row2) > 5 and i == 1:
      enemybullet_list[1].goto(row2[enemyindex].xcor(), row2[enemyindex].ycor())
    if len(row1) + len(row2) + len(row3) > 10 and i == 2:
      enemybullet_list[2].goto(row3[enemyindex].xcor(), row3[enemyindex].ycor())
    if len(row1) + len(row2) + len(row3) + len(row4) > 15 and i == 3:
      enemybullet_list[3].goto(row4[enemyindex].xcor(), row4[enemyindex].ycor())
  if level == 5:
    if len(row1) > 0:
      enemybullet.goto(row1[enemyindex].xcor(), row1[enemyindex].ycor())
    if len(row1) + len(row2) > 5 and i == 1:
      enemybullet_list[1].goto(row2[enemyindex].xcor(), row2[enemyindex].ycor())
    if len(row1) + len(row2) + len(row3) > 10 and i == 2:
      enemybullet_list[2].goto(row3[enemyindex].xcor(), row3[enemyindex].ycor())
    if len(row1) + len(row2) + len(row3) + len(row4) > 15 and i == 3:
      enemybullet_list[3].goto(row4[enemyindex].xcor(), row4[enemyindex].ycor())
    if len(row1) + len(row2) + len(row3) + len(row4) + len(row5) > 20 and i == 4:
      enemybullet_list[4].goto(row5[enemyindex].xcor(), row5[enemyindex].ycor())
  if level == 6:
    if len(row1) > 0:
      enemybullet.goto(row1[enemyindex].xcor(), row1[enemyindex].ycor())
    if len(row1) + len(row2) > 5 and i == 1:
      enemybullet_list[1].goto(row2[enemyindex].xcor(), row2[enemyindex].ycor())
    if len(row1) + len(row2) + len(row3) > 10 and i == 2:
      enemybullet_list[2].goto(row3[enemyindex].xcor(), row3[enemyindex].ycor())
    if len(row1) + len(row2) + len(row3) + len(row4) > 15 and i == 3:
      enemybullet_list[3].goto(row4[enemyindex].xcor(), row4[enemyindex].ycor())
    if len(row1) + len(row2) + len(row3) + len(row4) + len(row5) > 20 and i == 4:
      enemybullet_list[4].goto(row5[enemyindex].xcor(), row5[enemyindex].ycor())
    if len(row1) + len(row2) + len(row3) + len(row4) + len(row5) + len(row6) > 25 and i == 5:
      enemybullet_list[5].goto(row6[enemyindex].xcor(), row6[enemyindex].ycor())
  enemybullet.showturtle()
  i += 1

def checkforcollision():
  global gameover
  for item in bullet_list:
      for invader in row1:
        if isCollision(item, invader):
          update_score()
          invader.hideturtle()
          item.hideturtle()
          bulletindex = bullet_list.index(item)
          enemyindex = row1.index(invader)
          row1.pop(enemyindex)
          bullet_list.pop(bulletindex)
      for invader in row2:
        if isCollision(item, invader):
          update_score()
          invader.hideturtle()
          item.hideturtle()
          bulletindex = bullet_list.index(item)
          enemyindex = row2.index(invader)
          row2.pop(enemyindex)
          bullet_list.pop(bulletindex)
      for invader in row3:
        if isCollision(item, invader):
          update_score()
          invader.hideturtle()
          item.hideturtle()
          bulletindex = bullet_list.index(item)
          enemyindex = row3.index(invader)
          row3.pop(enemyindex)
          bullet_list.pop(bulletindex)
      for invader in row4:
        if isCollision(item, invader):
          update_score()
          invader.hideturtle()
          item.hideturtle()
          bulletindex = bullet_list.index(item)
          enemyindex = row4.index(invader)
          row4.pop(enemyindex)
          bullet_list.pop(bulletindex)
      for invader in row5:
        if isCollision(item, invader):
          update_score()
          invader.hideturtle()
          item.hideturtle()
          bulletindex = bullet_list.index(item)
          enemyindex = row5.index(invader)
          row5.pop(enemyindex)
          bullet_list.pop(bulletindex)
      for invader in row6:
        if isCollision(item, invader):
          update_score()
          invader.hideturtle()
          item.hideturtle()
          bulletindex = bullet_list.index(item)
          enemyindex = row6.index(invader)
          row6.pop(enemyindex)
          bullet_list.pop(bulletindex)
      for invaderbullet in enemybullet_list:
        for turtle in playerlist:
          if isCollision(invaderbullet, turtle):
            print("You died.")
            turtle.hideturtle()
            enemy.hideturtle()
            gameover = "true"

def generate_enemies():
  global enemy
  x= -375
  increment = 0
  while increment < level:
    y= 275
    for i in range(enemynumber):
      enemy = trtl.Turtle()
      enemy.color("red")
      enemy.shape(invader)
      enemy.penup()
      enemy.speed(0)
      enemy.setheading(270)
      enemy.setposition(x,y)
      if increment == 0:
        row1.append(enemy)
      if increment == 1:
        row2.append(enemy)
      if increment == 2:
        row3.append(enemy)
      if increment == 3:
        row4.append(enemy)
      if increment == 4:
        row5.append(enemy)
      if increment == 5:
        row6.append(enemy)
      y -= 25
    x += 25
    increment += 1

def moveenemiesright():
  global enemy
  if (enemy.xcor() <= 375) and (enemy.xcor() >= -375):
    for enemy in row1:
      enemy.goto(enemy.xcor() + 25, enemy.ycor())
    for enemy in row2:
      enemy.goto(enemy.xcor() + 25, enemy.ycor())
    for enemy in row3:
      enemy.goto(enemy.xcor() + 25, enemy.ycor())
    for enemy in row4:
      enemy.goto(enemy.xcor() + 25, enemy.ycor())
    for enemy in row5:
      enemy.goto(enemy.xcor() + 25, enemy.ycor())
    for enemy in row6:
      enemy.goto(enemy.xcor() + 25, enemy.ycor())
  else:
    for enemy in row1:
      enemy.goto(enemy.xcor(), enemy.ycor() - 25)
      enemy.goto(enemy.xcor() - 25, enemy.ycor())
    for enemy in row2:
      enemy.goto(enemy.xcor(), enemy.ycor() - 25)
      enemy.goto(enemy.xcor() - 25, enemy.ycor())
    for enemy in row3:
      enemy.goto(enemy.xcor(), enemy.ycor() - 25)
      enemy.goto(enemy.xcor() - 25, enemy.ycor())
    for enemy in row4:
      enemy.goto(enemy.xcor(), enemy.ycor() - 25)
      enemy.goto(enemy.xcor() - 25, enemy.ycor())
    for enemy in row5:
      enemy.goto(enemy.xcor(), enemy.ycor() - 25)
      enemy.goto(enemy.xcor() - 25, enemy.ycor())
    for enemy in row6:
      enemy.goto(enemy.xcor(), enemy.ycor() - 25)
      enemy.goto(enemy.xcor() - 25, enemy.ycor())

def moveenemiesleft():
  global enemy
  if (enemy.xcor() <= 375) and (enemy.xcor() >= -375):
    for enemy in row1:
      enemy.goto(enemy.xcor() - 25, enemy.ycor())
    for enemy in row2:
      enemy.goto(enemy.xcor() - 25, enemy.ycor())
    for enemy in row3:
      enemy.goto(enemy.xcor() - 25, enemy.ycor())
    for enemy in row4:
      enemy.goto(enemy.xcor() - 25, enemy.ycor())
    for enemy in row5:
      enemy.goto(enemy.xcor() - 25, enemy.ycor())
    for enemy in row6:
      enemy.goto(enemy.xcor() - 25, enemy.ycor())
  else:
    for enemy in row1:
      enemy.goto(enemy.xcor(), enemy.ycor() - 25)
      enemy.goto(enemy.xcor() + 25, enemy.ycor())
    for enemy in row2:
      enemy.goto(enemy.xcor(), enemy.ycor() - 25)
      enemy.goto(enemy.xcor() + 25, enemy.ycor())
    for enemy in row3:
      enemy.goto(enemy.xcor(), enemy.ycor() - 25)
      enemy.goto(enemy.xcor() + 25, enemy.ycor())
    for enemy in row4:
      enemy.goto(enemy.xcor(), enemy.ycor() - 25)
      enemy.goto(enemy.xcor() + 25, enemy.ycor())
    for enemy in row6:
      enemy.goto(enemy.xcor(), enemy.ycor() - 25)
      enemy.goto(enemy.xcor() + 25, enemy.ycor())

def noenemiesleft():
  if len(row1) + len(row2) + len(row3) + len(row4) + len(row5) + len(row6)== 0:
    return True
  else:
    return False

def enemyreachbase():
  global gameover
  for enemy in row1:
    if enemy.ycor() <= -220:
      player.hideturtle()
      enemy.hideturtle()
      gameover = "true"
  for enemy in row2:
    if enemy.ycor() <= -220:
      player.hideturtle()
      enemy.hideturtle()
      gameover = "true"
  for enemy in row3:
    if enemy.ycor() <= -220:
      player.hideturtle()
      enemy.hideturtle()
      gameover = "true"
  for enemy in row4:
    if enemy.ycor() <= -220:
      player.hideturtle()
      enemy.hideturtle()
      gameover = "true"
  for enemy in row5:
    if enemy.ycor() <= -220:
      player.hideturtle()
      enemy.hideturtle()
      gameover = "true"
  for enemy in row6:
    if enemy.ycor() <= -220:
      player.hideturtle()
      enemy.hideturtle()
      gameover = "true"

def enemymovement(iterate):
  if (iterator/(iterate)) < 1:
    moveenemiesright()
  else:
    if (iterator/(iterate)) <= 2:
      moveenemiesleft()

setup_player()
generate_enemies()
score_writer.write(score, font=font_setup)
wn.onkeypress(generateplayerbullet,"space")
wn.onkeypress(player_left, "Left")
wn.onkeypress(player_left,"a")
wn.onkeypress(player_right, "Right")
wn.onkeypress(player_right,"d")
wn.listen()
iterator = 0
movetime = 0.1
while gameover == "false" and level <= 6:
  for item in bullet_list:
    item.forward(50)
    if item.ycor() > 275:
      item.hideturtle()
      index = bullet_list.index(item)
      bullet_list.pop(index)
  if iterator % 2 == 0:
    if iterator % 128 == 0:
      iterator = 0
    if level == 1:
      enemymovement(64)
    elif level == 2:
      if len(row2) == 0:
        enemymovement(64)
      else:
        enemymovement(63)
    elif level == 3:
      if len(row3) == 0:
        if len(row2) == 0:
          enemymovement(64)
        else:
          enemymovement(63)
      else:
        enemymovement(62)
    elif level == 4:
      if len(row4) == 0:
        if len(row3) == 0:
          if len(row2) == 0:
            enemymovement(64)
          else:
            enemymovement(63)
        else:
          enemymovement(62)
      else:
        enemymovement(61)
    elif level == 5:
      if len(row5) == 0:
        if len(row4) == 0:
          if len(row3) == 0:
            if len(row2) == 0:
              enemymovement(64)
            else:
              enemymovement(63)
          else:
            enemymovement(62)
        else:
          enemymovement(61)
      else:
        enemymovement(60)
    elif level == 6:
      if len(row6) == 0:
          if len(row5) == 0:
            if len(row4) == 0:
              if len(row3) == 0:
                if len(row2) == 0:
                  enemymovement(64)
                else:
                  enemymovement(63)
              else:
                enemymovement(62)
            else:
              enemymovement(61)
          else:
            enemymovement(60)
      else:
        enemymovement(59)
    generateenemybullet()
    for item in enemybullet_list:
      item.forward(50)
      checkforcollision()
      if item.ycor() < -220:
        item.hideturtle()
        index = enemybullet_list.index(item)
        enemybullet_list.pop(index)
  checkforcollision()
  if noenemiesleft():
    for item in enemybullet_list:
      item.hideturtle()
    for item in bullet_list:
      item.hideturtle()
    enemybullet_list.clear()
    bullet_list.clear()
    level += 1
    i = 0
    iterator = 0
    movetime -= 0.1/6
    if level <= 6:
      generate_enemies()
  time.sleep(movetime)
  iterator += 1
endgame_message = trtl.Turtle()
endgame_message.hideturtle()
endgame_message.speed(0)
endgame_message.pencolor("white")
if noenemiesleft():
  endgame_message.write("You Win!", font=font_setup)
else:
  endgame_message.write("Game Over.", font=font_setup)
endgame_message.penup()
endgame_message.goto(0, -30)
scorestr = "Final Score:" + str(score)
endgame_message.write(scorestr, font=font_setup)
wn.mainloop()