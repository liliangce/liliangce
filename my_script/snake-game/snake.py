# /usr/bin/evn python=2.7
# coding=utf-8


import random
import threading

from Tkinter import *
import Queue
import time


class GUI(Tk):
    def __init__(self, queue):
        Tk.__init__(self)
        self.queue = queue
        self.is_game_over = False
        self.canvas = Canvas(self, width=495, height=305, bg='#000000')
        self.canvas.pack()
        self.snake = self.canvas.create_line((0, 0), (0, 0), fill='#FFCC4C', width=10)
        self.food = self.canvas.create_rectangle(0, 0, 0, 0, fill='#FFCC4C', outline='#FFCC4C')
        self.points_earned = self.canvas.create_text(455, 15, fill='white', text='score:0')
        self.queue_handler()

    def queue_handler(self):
        try:
            while True:
                task = self.queue.get(block=False)
                # print task
                if task.get('move'):
                    points = [x for point in task['move'] for x in point]
                    self.canvas.coords(self.snake, *points)
                if task.get('food'):
                    self.canvas.coords(self.food, *task['food'])
                elif task.get('points_earned'):
                    self.canvas.itemconfigure(self.points_earned,
                                              text='score:{}'.format(task['points_earned']))
                    self.queue.task_done()
        except:
            if not self.is_game_over:
                self.canvas.after(100, self.queue_handler)

    def game_over(self):
        self.is_game_over = True
        self.canvas.create_text(200, 150, fill='white', text='Game Over!')
        quitbtn = Button(self, text='Quit', command=self.destroy)
        rebtn = Button(self, text='Begin', command=self.__init__)
        self.canvas.create_window(200, 180, anchor='wn', window=quitbtn)


class Food():
    def __init__(self, queue):
        self.queue = queue
        self.generate_food()

    def generate_food(self):
        x = random.randrange(5, 480, 10)
        y = random.randrange(5, 295, 10)
        self.position = x, y
        self.exppos = x - 5, y - 5, x + 5, y + 5
        self.queue.put({'food': self.exppos})


class Snake(threading.Thread):
    def __init__(self, gui, queue):
        threading.Thread.__init__(self)
        self.gui = gui
        self.queue = queue
        self.daemon = True
        self.points_earned = 0
        self.snake_points = [(495, 55), (485, 55), (475, 55), (465, 55), (455, 55)]
        self.food = Food(queue)
        self.direction = 'Left'
        self.start()

    def run(self):
        if self.gui.is_game_over:
            pass
        while not self.gui.is_game_over:
            self.queue.put({'move': self.snake_points})
            time.sleep(0.5)
            self.move()

    def key_pressed(self, e):
        self.direction = e.keysym

    def move(self):
        new_snake_point = self.calculate_new_coordinates()
        if self.food.position == new_snake_point:
            self.points_earned += 1
            self.queue.put({'points_earned': self.points_earned})
            self.food.generate_food()

    def calculate_new_coordinates(self):
        new_snake_point = 0, 0
        last_x, last_y = self.snake_points[-1]
        if self.direction == 'Up':
            new_snake_point = last_x, (last_y - 10)
        elif self.direction == 'Down':
            new_snake_point = last_x, (last_y + 10)
        elif self.direction == 'Left':
            new_snake_point = (last_x - 10), last_y
        elif self.direction == 'Right':
            new_snake_point = (last_x + 10), last_y
        return new_snake_point

    def check_game_over(self, snake_point):
        x, y = snake_point[0], snake_point[1]
        if not -5 < x < 505 or not -5 < y < 315 or snake_point in self.snake_points:
            self.queue.put({'game_over': True})


def main():
    global q, gui
    q = Queue.Queue()
    gui = GUI(q)
    gui.title('我的第一个小游戏')

    snake = Snake(gui, q)
    gui.bind('<Key-Left>', snake.key_pressed)
    gui.bind('<Key-Right>', snake.key_pressed)
    gui.bind('<Key-Up>', snake.key_pressed)
    gui.bind('<Key-Down>', snake.key_pressed)
    gui.mainloop()


if __name__ == '__main__':
    main()
