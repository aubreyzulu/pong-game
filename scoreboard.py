


from turtle import Turtle

FONT = ('Courier',80, 'normal')

class ScoreBoard(Turtle):
  def __init__(self) -> None:
    super().__init__()
    self.color('white')
    self.penup()
    self.hideturtle()
    self.l_score = 0
    self.r_score = 0
    
    self.update_scoreboard()
    
  def update_scoreboard(self)-> None:
    self.clear()
    self.goto(-100,200)
    self.write(self.l_score,False,'center', FONT)
    self.goto(100,200)
    self.write(self.r_score,False,'center', FONT)
    
  def l_point(self)->None:
    self.l_score +=1
    self.update_scoreboard()
    
  def r_point(self)->None:
    self.r_score += 1
    self.update_scoreboard()
    