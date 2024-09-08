from tkinter import *
import random
import time
tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0,
highlightthickness=0)
canvas.pack()
tk.update()

points = 0
points_label = Label(tk, text=f"Points: {points}", borderwidth=1, relief="solid", width=55, font=("", 12))
points_label.pack(side="top")

class Ball:
    def __init__(self, color, canvas, paddle):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if pos[3] >= self.canvas_height:
            self.y = -3
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = 3
            if pos[2] >= self.canvas_width:
                self.x = -3

    def hit_paddle(self, pos):
        global points
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                points += 1
                points_label.config(text=f"Points: {points}")
                return True
        return False

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.canvas_width = self.canvas.winfo_width()
        self.x = 0

        self.canvas.bind_all('<Key>', self.handle_key)
        self.canvas.bind_all('<KeyRelease>', self.on_key_release)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def on_key_release(self, event):
        self.x = 0
        print("hghgh")

    def handle_key(self, event):
        key = event.keysym.lower()
        if key == 'left':
            self.x = -2
        elif key == 'right':
            self.x = 2

    def move_left(self, evt):
        self.x = -2

    def move_right(self, evt):
        self.x = 2

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2


paddle = Paddle(canvas, 'blue')
bball = Ball('red', canvas, paddle)

while 1:
    if not bball.hit_bottom:
        bball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
