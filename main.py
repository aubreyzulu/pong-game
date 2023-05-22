from turtle import Screen
import time
from paddle import Paddle
from scoreboard import ScoreBoard
from ball import Ball
screen = Screen()
screen.bgcolor('black')
screen.setup(800,600)
screen.title('Pong Game')
screen.tracer(0)
r_paddle = Paddle((360,0))
l_paddle = Paddle((-360,0))
ball = Ball()
scoreboard = ScoreBoard()




  
screen.listen()
screen.onkey(r_paddle.go_up,'Up')
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,'w')
screen.onkey(l_paddle.go_down,"s")

game_on=True

while game_on:
  time.sleep(ball.ball_speed)
  screen.update()
  ball.move()
  
  #Detect collusion with wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()
    
  # Detect collusion with r paddle
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()
    
  # Detect R paddle misses
  if ball.xcor() > 380:
    ball.reset_position()
    scoreboard.l_point()
    
    
  #Detect L paddle misses
  if ball.xcor() < -380:
    ball.reset_position()
    scoreboard.r_point()

screen.exitonclick()