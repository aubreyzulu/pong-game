from turtle import Turtle

class Paddle(Turtle):
  
  def __init__(self,position:tuple) -> None:
    super().__init__()
    self.shape('square')
    self.color('white')
    self.shapesize(5,1)
    self.penup()
    self.goto(position)
    
    
  def go_up(self)->None:
   new_y = self.ycor() + 20
   self.goto(self.xcor(), new_y)
   
  def go_down(self)->None:
    new_y = self.ycor() - 20
    self.goto(self.xcor(), new_y)
      
    