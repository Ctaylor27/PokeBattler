import tkinter as tk
from Util import *
from Battle import Battle
from PIL import Image, ImageTk
from urllib.request import urlopen

class GUI():
    def __init__(self):
        self.root = tk.Tk()

        self.title = tk.Label(self.root, text="Pokemon Battler!", font=("Arial", 18))
        self.title.pack(padx=10, pady=10)

        self.frame = tk.Frame(self.root)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.pack(fill="x")


        self.init_frame = tk.Frame(self.root)
        self.init_frame.pack(fill="x")

        self.label = tk.Label(self.init_frame, text="Enter a combatant: ", font=("Arial", 16))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.init_frame, height=1, width=15, font=("Arial", 18))
        self.textbox.pack(padx=10, pady=10)

        self.button = tk.Button(self.init_frame, text="Enter", command=self.submit)
        self.button.pack(padx=10, pady=10)

        self.battle_frame = tk.Frame(self.root)
        self.battle_frame.pack(fill="x")

        self.log = tk.Frame(self.root)
        self.log.pack(fill="x")

        self.root.mainloop()

    def clear_textbox(self):
        self.textbox.delete("0.1", tk.END)

    def hide_init_frame(self):
        for widget in self.init_frame.winfo_children():
            widget.destroy()

        self.init_frame.destroy()

    def show_battle_frame(self):
        

        self.label = tk.Label(self.battle_frame, text="BATTLE!", font=("Arial", 20))
        self.label.pack(padx=10, pady=10)

        self.button = tk.Button(self.battle_frame, text="Take Turn", command=self.battle)
        self.button.pack(padx=10, pady=10)

    def getImage(self, target):

        if target == 0:
            imageUrl = data.pk1.sprites[1]
        else:
            imageUrl = data.pk2.sprites[0]

        openedUrl = urlopen(imageUrl)
        image_data = openedUrl.read()
        openedUrl.close()

        photo = ImageTk.PhotoImage(data=image_data)
        label = tk.Label(self.frame, image=photo)
        label.image=photo

        if target == 0:
            label.grid(row=2, column=0, sticky=("W", "E"))
        else:
            label.grid(row=0, column=2, sticky=("W", "E"))
            self.hide_init_frame()
            self.show_battle_frame()
        
    def submit(self):

        if data.num_selected == 0: 
            data.pk1 = reqPokemon(self.textbox.get("0.1", tk.END).replace("\n", ''))
            data.num_selected += 1
            self.clear_textbox()
            self.getImage(0)
            

        elif data.num_selected == 1: 
            data.pk2 = reqPokemon(self.textbox.get("0.1", tk.END).replace("\n", ''))
            data.num_selected += 1
            self.clear_textbox()
            self.getImage(1)
        
        if data.num_selected == 2:
            data.battle = Battle(data.pk1, data.pk2)

    def end_battle(self):
        

        print(data.battle_over_text)
        self.log.destroy()
        for widget in self.battle_frame.winfo_children():
            widget.destroy()

        self.label = tk.Label(self.battle_frame, text=data.battle_over_text, font=("Arial", 20))
        self.label.pack(padx=10, pady=10)

        self.button = tk.Button(self.battle_frame, text="Reset", command=self.battle)
        self.button.pack(padx=10, pady=10)

        imageUrl = data.winner.sprites[0]
        print(imageUrl)

        for widget in self.frame.winfo_children():
            widget.destroy()



        openedUrl = urlopen(imageUrl)
        image_data = openedUrl.read()
        openedUrl.close()

        photo = ImageTk.PhotoImage(data=image_data)
        label = tk.Label(self.frame, image=photo)
        label.image=photo
        label.pack(fill="x")

    def reset(self):
        data = Data()
        pass


    def battle(self):
        self.label = tk.Label(self.log, text="Battle", font=("Arial", 10))
        self.label.config(text=data.battle.take_turn())
        self.label.pack()
        if len(self.log.winfo_children()) > 5 : self.log.winfo_children()[0].destroy()
        if "Battle Over" in data.battle_over_text:
            print(data.battle_over_text)
            self.end_battle()
