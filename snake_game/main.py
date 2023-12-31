import random
from tkinter import Tk,Label,Canvas
# from custom_objects import *

screen_w = screen_h  = 600
speed = 50
shape_size = 20
length_of_snake = 5 #body size
colors = ["green","red","blue","black"]
possible_directions = ["up","Down","Right","Left"]

class Player:
    
    def __init__(self):
        self.length_of_snake = length_of_snake
        self.cur_position = []
        self.squares = []
        for i in range(0,length_of_snake):
            self.cur_position.append([90,90])
        for x,y in self.cur_position:
            square =  canvas.create_rectangle(x,y,x+shape_size,y+shape_size,fill = "green",tag="food")
            self.squares.append(square)
    
def Points(canvas):
    x = random.randint(0,(screen_w//shape_size)-1)*shape_size
    
    y = random.randint(0,(screen_h//shape_size)-1)*shape_size
    
    position = [x,y]
    vertices = [50, 50, 150, 50, 100, 150]
    # canvas.create_polygon(vertices, fill='blue')    
    canvas.create_rectangle(x,y,x+shape_size,y+shape_size,fill = "red",tag="food")
def score_counter(score_tag, score):
    score_tag.config(text=f"Best Score: {score}")
def game_end():
    pass
def movement(points,player):
    x,y = player.cur_position[0]
    
    pass

root = Tk()
root.title("Bug eater",)
root.resizable(False,False)
score = 0
label = Label(root,text=f"Best Score: {score}")
label.pack()
canvas  = Canvas(root,bg=colors[-1],height=screen_h,width=screen_w)
canvas.pack()

root.update()

window_w = canvas.winfo_reqwidth()
window_h = canvas.winfo_reqheight()

x = int((screen_w/2)-(window_w/2))
y = int((screen_h/2)-(window_h/2))
root.geometry(f"{window_w}x{window_h}+{x}+{y}")

player = Player()
player = Player()
movement([],player)
Points(canvas)
root.mainloop()

