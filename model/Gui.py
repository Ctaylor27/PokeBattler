import tkinter as tk

class GUI():
    def __init__(self):
        self.root = tk.Tk()

        self.title = tk.Label(self.root, text="Pokemon Battler!", font=("Arial", 18))
        self.title.pack(padx=10, pady=10)

        self.label = tk.Label(self.root, text="Enter the first combatant: ", font=("Arial", 16))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=1, width=15, font=("Arial", 18))
        self.textbox.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Enter", command=self.submit)
        self.button.pack(padx=10, pady=10)
        self.root.mainloop()

    def submit(self):
        print(self.textbox.get("0.1", tk.END))

GUI()