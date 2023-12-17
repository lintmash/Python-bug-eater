import random
from tkinter import Tk,Label,Canvas
# from custom_objects import *

screen_w = screen_h  = 600
speed = 50
shape_size = 4
length_of_snake = 5
colors = ["green","red","blue","black"]
possible_directions = ["up","Down","Right","Left"]

def Player():
    pass
    
def Points():
    x = random.randint(0,(screen_w/shape_size)-1)*shape_size
    
    y = random.randint(0,(screen_h/shape_size)-1)*shape_size
    
    position = [x,y]
    
    canvas.create_polygon(x,y,x+shape_size,y+shape_size,fill = "red",tag="food")
    

def game_end():
    pass
def movement():
    pass

root = Tk()
root.title("Bug eater")
root.resizable(False,False)
score = 0
label = Label(root,text=f"Best Score: {score}")
label.pack()
canvas  = Canvas(root,bg=colors[-1],height=screen_h,width=screen_w)
canvas.pack()
root.update()

window_w = root.winfo_width()
window_h = root.winfo_height()
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

x = int((screen_w/2)-(window_w/2))
y = int((screen_h/2)-(window_h/2))
root.geometry(f"{window_w}x{window_h}+{x}+{y}")

Player()
Points()
root.mainloop()

