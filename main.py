import customtkinter
from CTkMessagebox import CTkMessagebox
from pymongo.mongo_client import MongoClient
from tkinter import ttk
from datetime import datetime
import pandas as pd
from PIL import Image
from util import UpdateFrame, ButtonFrame, MyFrame


url = "mongodb+srv://mongodb:mongodb@tally.i6wfrlt.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

# Database Name and Collection Name
db = client['Punekar']
collec = db['Tally']

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("950x750")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.resizable(False, False)

        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=10, pady=20, sticky="nsew")

        self.button_frame = ButtonFrame(master=self)
        self.button_frame.grid(row=0, column=1, padx=10, pady=20,sticky='nsew')


app = App()
app.mainloop()