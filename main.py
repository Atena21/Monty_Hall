from tkinter import *
import tkinter as tk
from tkinter import font as tkfont  # python 3
#from client import Client
#from client_utils import *

WINDOW_GEOMETRY = "800x500"


class Application:
    root = None

    def __init__(self, root, master=None):
        self.root = root

    def start_page(self):#portas fechadas
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry(WINDOW_GEOMETRY)
        self.root.title("Portas Fechadas")
        img_portasfechadas = PhotoImage (file="assets/portas.png")
        image_portasfechadas=tk.Label(image=img_portasfechadas)
        image_portasfechadas.place(relx=0.5,rely=0.5, anchor=CENTER)

        #Botão Porta1
        img_porta1 = PhotoImage(file="assets/portas1.png")
        button_porta1 = tk.Button(image=img_porta1,
                                command=#TEM QUE COLOCAR PRA ONDE VAI!!)
        button_porta1.place(relx=0.2, rely=0.5, anchor=CENTER)

        # Botão Porta2
        img_porta2 = PhotoImage(file="assets/portas2.png")
        button_porta2 = tk.Button(image=img_porta2,
                                  command=#TEM QUE COLOCAR PRA ONDE VAI!!)
        button_porta2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Botão Porta3
        img_porta3 = PhotoImage(file="assets/portas3.png")
        button_porta3 = tk.Button(image=img_porta3,
                                  command=#TEM QUE COLOCAR PRA ONDE VAI!!) #aqui eu tmb usei pra testar command=self.nomedatela, tipo self.trocar_ou_manter, só pra ver como ficaram as outras telas
        button_porta3.place(relx=0.8, rely=0.5, anchor=CENTER)


        self.root.mainloop()


    def trocar_ou_manter_porta(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry(WINDOW_GEOMETRY)
        self.root.title("Trocar ou Manter a porta")
        img_portasfechadas = PhotoImage(file="assets/portasabertas.png")
        image_portasfechadas = tk.Label(image=img_portasfechadas)
        image_portasfechadas.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Botão de trocar porta
        img_change = PhotoImage(file="assets/trocar_porta.png")
        button_change = tk.Button(image=img_change,
                                 command=#TEM QUE COLOCAR PRA ONDE VAI!!)
        button_change.place(relx=0.3, rely=0.92, anchor=CENTER)

        # Botão de manter porta
        img_keep = PhotoImage(file="assets/manter_porta.png")
        button_keep = tk.Button(image=img_keep,
                                  command=#TEM QUE COLOCAR PRA ONDE VAI!!)
        button_keep.place(relx=0.7, rely=0.92, anchor=CENTER)

        self.root.mainloop()


    def result(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry(WINDOW_GEOMETRY)
        self.root.title("Resultado")
        img_portasfechadas = PhotoImage(file="assets/portasabertas.png")
        image_portasfechadas = tk.Label(image=img_portasfechadas)
        image_portasfechadas.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Botão para última página
        img_next = PhotoImage(file="assets/next.png")
        button_next = tk.Button(image=img_next,
                                command=self.main_screen)
        button_next.place(relx=0.925, rely=0.942, anchor=CENTER)


        self.root.mainloop()

    def won(self):  # pagina ganhou
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry(WINDOW_GEOMETRY)
        self.root.title("Ganhou o jogo")
        img_won = PhotoImage(file="assets/ganhou.png")
        image_won = tk.Label(image=img_won)
        image_won.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Botão para sair do jogo
        img_quit = PhotoImage(file="assets/sair.png")
        button_quit = tk.Button(image=img_quit,
                                command=self.root.destroy)
        button_quit.place(relx=0.925, rely=0.942, anchor=CENTER)

        # Botão de voltar para o início
        img_begin = PhotoImage(file="assets/again.png")
        button_begin = tk.Button(image=img_begin,
                                 command=self.main_screen)
        button_begin.place(relx=0.962, rely=0.058, anchor=CENTER)

        self.root.mainloop()


    def lost(self):#pagina perdeu
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry(WINDOW_GEOMETRY)
        self.root.title("Perdeu o jogo")
        img_lost = PhotoImage(file="assets/perdeu.png")
        image_lost = tk.Label(image=img_lost)
        image_lost.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Botão para sair do jogo
        img_quit = PhotoImage(file="assets/sair.png")
        button_quit = tk.Button(image=img_quit,
                                command=self.root.destroy)
        button_quit.place(relx=0.925, rely=0.942, anchor=CENTER)

        #Botão de voltar para o início
        img_begin = PhotoImage(file="assets/again.png")
        button_begin = tk.Button(image=img_begin,
                                command=self.main_screen)
        button_begin.place(relx=0.962, rely=0.058, anchor=CENTER)

        self.root.mainloop()


    def main_screen(self):
        self.root.title("Página principal")
        img_inicio= PhotoImage (file="assets/mh1.png")
        image_inicial=tk.Label(image=img_inicio)
        image_inicial.place(relx=0.5,rely=0.5, anchor=CENTER)
       #Botão para iniciar o jogo
        img_start = PhotoImage(file="assets/jogar.png")
        button_start = tk.Button(
            image=img_start, command=self.start_page)
        button_start.place(relx=0.3, rely=0.5, anchor=CENTER)

        #Botão para sair do jogo
        img_quit = PhotoImage(file="assets/sair.png")
        button_quit = tk.Button(image=img_quit,
                                command=self.root.destroy)
        button_quit.place(relx=0.7, rely=0.5, anchor=CENTER)
        self.root.mainloop()

    def game(self):
        self.main_screen()
        self.root.mainloop()


root = tk.Tk()
root.geometry(WINDOW_GEOMETRY)
app = Application(root)

app.game()