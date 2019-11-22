from tkinter import *
import tkinter as tk
from client.clientmh import ClientUtil
from tkinter import font as tkfont  # python 3
#from client import Client
#from client_utils import *

WINDOW_GEOMETRY = "800x500"


class Application:
    root = None
    u = ClientUtil()

    def __init__(self, root, master=None):
        self.root = root

    def position(self, buttonName, choice):
        if (choice == 0):
           buttonName.place(relx=0.2, rely=0.5, anchor=CENTER)

        elif (choice == 1):
           buttonName.place(relx=0.5, rely=0.5, anchor=CENTER)

        else:
           buttonName.place(relx=0.8, rely=0.5, anchor=CENTER)

    def start_page(self):  # portas fechadas
        self.root.destroy()
        self.root = tk.Tk()
        print("start page")
        self.root.geometry(WINDOW_GEOMETRY)
        self.root.title("Portas Fechadas")
        img_portasfechadas = PhotoImage (file="assets/portas.png")
        print("start page2")
        image_portasfechadas=tk.Label(image=img_portasfechadas)
        image_portasfechadas.place(relx=0.5, rely=0.5, anchor=CENTER)

        #Botão Porta1
        img_porta1 = PhotoImage(file="assets/portas1.png")
        button_porta1 = tk.Button(image=img_porta1,
                                  command=lambda: self.trocar_ou_manter_porta(0))
        button_porta1.place(relx=0.2, rely=0.5, anchor=CENTER)

        # Botão Porta2
        img_porta2 = PhotoImage(file="assets/portas2.png")
        button_porta2 = tk.Button(image=img_porta2,
                                  command=lambda: self.trocar_ou_manter_porta(1))
        button_porta2.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Botão Porta3
        img_porta3 = PhotoImage(file="assets/portas3.png")
        button_porta3 = tk.Button(image=img_porta3,
                                  command=lambda: self.trocar_ou_manter_porta(2))  #aqui eu tmb usei pra testar command=self.nomedatela, tipo self.trocar_ou_manter, só pra ver como ficaram as outras telas
        button_porta3.place(relx=0.8, rely=0.5, anchor=CENTER)

        self.root.mainloop()


    def trocar_ou_manter_porta(self, door):
        self.root.destroy()
        goat = self.u.choose_door(door)
        self.root = tk.Tk()
        self.root.geometry(WINDOW_GEOMETRY)
        self.root.title("Trocar ou Manter a porta")
        img_portasfechadas = PhotoImage(file="assets/portasabertas.png")
        image_portasfechadas = tk.Label(image=img_portasfechadas)
        image_portasfechadas.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Bode
        print(door)
        img_goat = PhotoImage(file="assets/goat.png")
        button_goat = tk.Button(image=img_goat, command="")
        self.position(button_goat, goat)

        # Door
        img_door = PhotoImage(file="assets/doorselected.png")
        button_door = tk.Button(image=img_door, command="")
        self.position(button_door, door)

        #Other door
        door2 = 3-(door+goat)
        img_door2 = PhotoImage(file="assets/portas"+str(door2+1)+".png")
        button_door2 = tk.Button(image=img_door2, command="")
        self.position(button_door2, door2)

        # Botão de trocar porta
        img_change = PhotoImage(file="assets/trocar_porta.png")
        button_change = tk.Button(image=img_change,
                                  command=lambda: self.results('s'))
        button_change.place(relx=0.3, rely=0.92, anchor=CENTER)

        # Botão de manter porta
        img_keep = PhotoImage(file="assets/manter_porta.png")
        button_keep = tk.Button(image=img_keep,
                                command=lambda: self.results('n'))
        button_keep.place(relx=0.7, rely=0.92, anchor=CENTER)

        self.root.mainloop()

    def results(self, choice):
        print("eita")
        ganhou = False
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry(WINDOW_GEOMETRY)
        self.root.title("Resultado")
        door, car = self.u.keep_door(choice)
        img_portasfechadas = PhotoImage(file="assets/portasabertas.png")
        image_portasfechadas = tk.Label(image=img_portasfechadas)
        image_portasfechadas.place(relx=0.5, rely=0.5, anchor=CENTER)

        # porta escolhida
        if door == car:
            ganhou = True
            img_door = PhotoImage(file="assets/carselected.png")
            button_door = tk.Button(image=img_door, command="")
            self.position(button_door, door)

            goat = (door+1) % 3
            img_goat = PhotoImage(file="assets/goat.png")
            button_goat = tk.Button(image=img_goat, command="")
            self.position(button_goat, goat)

            goat2 = (goat+1) % 3
            img_goat2 = PhotoImage(file="assets/goat.png")
            button_goat2 = tk.Button(image=img_goat2, command="")
            self.position(button_goat2, goat2)

        else:
            img_door = PhotoImage(file="assets/goatselected.png")
            button_door = tk.Button(image=img_door, command="")
            self.position(button_door, door)

            img_car = PhotoImage(file="assets/car.png")
            button_car = tk.Button(image=img_car, command="")
            self.position(button_car, car)

            goat = 3-(car+door)
            img_goat = PhotoImage(file="assets/goat.png")
            button_goat = tk.Button(image=img_goat, command="")
            self.position(button_goat, goat)


        # Botão para última página
        img_next = PhotoImage(file="assets/next.png")
        if ganhou:
            button_next = tk.Button(image=img_next,
                                    command=self.won)
        else:
            button_next = tk.Button(image=img_next,
                                    command=self.lost)

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
        # self.u.disconnect()

        # Botão de voltar para o início
        img_begin = PhotoImage(file="assets/again.png")
        button_begin = tk.Button(image=img_begin,
                                 command=self.restart)
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
        # self.u.disconnect()

        #Botão de voltar para o início
        img_begin = PhotoImage(file="assets/again.png")
        button_begin = tk.Button(image=img_begin,
                                 command=self.restart)
        button_begin.place(relx=0.962, rely=0.058, anchor=CENTER)

        self.root.mainloop()

    def restart(self):
        print("restart")
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry(WINDOW_GEOMETRY)
        self.main_screen()

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
        # self.u.disconnect()
        self.root.mainloop()

    def game(self):
        self.main_screen()
        self.root.mainloop()


root = tk.Tk()
root.geometry(WINDOW_GEOMETRY)
app = Application(root)

app.game()
