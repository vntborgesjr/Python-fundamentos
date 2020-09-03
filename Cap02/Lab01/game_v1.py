# Game Ping-Pong

from tkinter import * # equivalente a importar pacotes
import random
import time

level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n")) # variável level
length = 500/level # variável length


root = Tk() # Variável
root.title("Ping Pong") # função title() sobre variável root
root.resizable(0,0) # função resizable() sobre variável root
root.wm_attributes("-topmost", -1) # função wm_attributes() sobre variável root

canvas = Canvas(root, width=800, height=600, bd=0,highlightthickness=0) # variável canvas
canvas.pack() # função pack() sobre variável canvas

root.update() # função update() sobre variável root

# o bloco  de código até aqui cria a janela onde o jogo acontece

# Variável
count = 0
lost = False

class Bola: # define as configurações e o movimento da bola????
    def __init__(self, canvas, Barra, color): 
        self.canvas = canvas
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)

        starts_x = [-3, -2, -1, 1, 2, 3] # cria uma lista
        random.shuffle(starts_x) # aleatoriza os valores da lista starts_x

        self.x = starts_x[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()


    def draw(self): # define o movimento da Barra???
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3
            
        if pos[2] >= self.canvas_width:
            self.x = -3

        self.Barra_pos = self.canvas.coords(self.Barra.id)


        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]: # define a contagem dos pontos???
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                self.y = -3
                global count
                count +=1
                score()


        if pos[3] <= self.canvas_height: # definie a perda do jogo quando a Barra erra a Bola????
            self.canvas.after(10, self.draw)
        else:
            game_over()
            global lost
            lost = True


class Barra: # define as configurações e movimento da barra????
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)

        self.pos = self.canvas.coords(self.id)

        if self.pos[0] <= 0:
            self.x = 0
        
        if self.pos[2] >= self.canvas_width:
            self.x = 0
        
        global lost
        
        if lost == False:
            self.canvas.after(10, self.draw)

    def move_left(self, event):
        if self.pos[0] >= 0:
            self.x = -3

    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3


def start_game(event):
    global lost, count
    lost = False
    count = 0
    score()
    canvas.itemconfig(game, text=" ")

    time.sleep(1)
    Barra.draw()
    Bola.draw()


def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))

def game_over():
    canvas.itemconfig(game, text="Game over!")


Barra = Barra(canvas, "orange") # definie a cor da barra
Bola = Bola(canvas, Barra, "purple") # define a cor da bola


score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))


canvas.bind_all("<Button-1>", start_game)

root.mainloop()
