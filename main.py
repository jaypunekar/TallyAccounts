import customtkinter
from CTkMessagebox import CTkMessagebox
from pymongo.mongo_client import MongoClient
from tkinter import ttk
from datetime import datetime
import pandas as pd
from PIL import Image


# MongoDB Atlas URL
url = "mongodb+srv://mongodb:mongodb@tally.i6wfrlt.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

# Database Name and Collection Name
db = client['Punekar']
collec = db['Tally']

class ButtonFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.edit_button = customtkinter.CTkButton(self, text="Edit", command=self.edit_button)
        self.edit_button.pack(pady=10)
        self.update_button = customtkinter.CTkButton(self, text="Update", command=self.update_selected)
        self.update_button.pack(pady=10)

        self.update_window = None
    
    def update_selected(self):
        self.update_window = customtkinter.CTkToplevel(self)
        self.update_window.geometry("600x600")
        self.update_window.focus()
        self.update_window.resizable = False
        # try:
        #     x = trv.selection()[0]
        #     print(trv.item(x)['values'])
        # except:
        #     CTkMessagebox(title='Error', message="Please Select a Row")

    def edit_button(self):
        CTkMessagebox(title='Error', message="You are not allowed to Edit")


class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.df = pd.DataFrame(columns=["Department", "Date_time", "Resort Name", "Person Name", "Amount", "Payment_type", "Approved", "Paid"])
        self.order = True

        try:
            for one_collec in collec.find():
                if one_collec["Approved"] == 1 and one_collec["Signature"] == 0:
                    self.df.loc[len(self.df.index)] = [one_collec["Department"], one_collec["Date_time"], one_collec["Resort Name"], one_collec["Person Name"], one_collec["Amount"], one_collec["Payment_type"], one_collec["Approved"], one_collec["Paid"]]
        except Exception:
            CTkMessagebox(title="Error", message=Exception)

        self.display_data(self.df)
        # self.my_tree.pack(pady=10)

        self.style = ttk.Style()
            
        self.style.theme_use("default")

        self.style.configure("Treeview",
                        background="#2a2d2e",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#343638",
                        bordercolor="#343638",
                        borderwidth=0)
        self.style.map('Treeview', background=[('selected', '#22559b')])

        self.style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat")
        self.style.map("Treeview.Heading",
                    background=[('active', '#3484F0')])
        
        self.style.configure("Treeview", height=700)

    # Function for sorting column 
    def sort_column(self, column):
        if self.order:
            self.order = False
        else:
            self.order = True
        
        self.df = self.df.sort_values(by=[column], ascending=self.order)
        self.display_data(self.df)

    def display_data(self, dataframe):
        l1 = list(self.df)
        r_set = self.df.to_numpy().tolist()
        global trv
        trv = ttk.Treeview(self, selectmode ='browse', show='headings', height=33, columns=l1)
        trv.grid(row=1,column=1,padx=30,pady=20)
        for col in l1:
            trv.column(col, width = 100, anchor ='c')
            trv.heading(col, text = col,command=lambda col=col :self.sort_column(col))

        for dt in r_set:  
            v = [r for r in dt] # creating a list from each row 
            trv.insert("", 'end' ,values=v) # adding row
        

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