import os
import sys
import customtkinter
from CTkMessagebox import CTkMessagebox
from pymongo.mongo_client import MongoClient
from tkinter import ttk
from datetime import datetime
import pandas as pd
from PIL import Image
from exception import TallyException

try:
    # MongoDB Atlas URL
    url = "mongodb+srv://mongodb:mongodb@tally.i6wfrlt.mongodb.net/?retryWrites=true&w=majority"

    client = MongoClient(url)

    # Database Name and Collection Name
    db = client['Punekar']
    collec = db['Tally']
except Exception as e:
    raise TallyException(e, sys) from e

class UpdateFrame(customtkinter.CTkFrame):
    try:
        def __init__(self, resort_name, amount, reason, master, **kwargs):
            super().__init__(master, **kwargs)
            self.resort_name = resort_name
            self.amount = amount
            self.reason = reason

            self.label_heading = customtkinter.CTkLabel(self, text="Entered Details", font=('Monospace', 30), width=10, justify='center')
            self.label_heading.place(relx=0.5, rely=0.1, anchor='n')

            self.label_name = customtkinter.CTkLabel(self, text="Resort Name:")
            self.label_name.place(relx=0.15, rely=.2, anchor='nw')
            self.entry_name = customtkinter.CTkEntry(self, placeholder_text=self.resort_name, width=200)
            self.entry_name.place(relx=.15, rely=.25, anchor='nw')

            self.label_person = customtkinter.CTkLabel(self, text="Person Name:")
            self.label_person.place(relx=0.55, rely=.2, anchor='nw')
            self.payment_person = customtkinter.CTkEntry(self, placeholder_text="Person Paid To")
            self.payment_person.place(relx=.55, rely=.25, anchor='nw')

            self.label_amount = customtkinter.CTkLabel(self, text="Amount (Rs.)")
            self.label_amount.place(relx=0.15, rely=.3, anchor='nw')
            self.entry_amount = customtkinter.CTkEntry(self, placeholder_text=self.amount, width=140)
            self.entry_amount.place(relx=.15, rely=.35, anchor='nw')

            self.label_reason = customtkinter.CTkLabel(self, text="Reason:")
            self.label_reason.place(relx=0.15, rely=.4, anchor='nw')
            self.textbox_reason = customtkinter.CTkTextbox(master=self, width=400, corner_radius=8)
            self.textbox_reason.insert('end', self.reason)
            self.textbox_reason.place(relx=.15, rely=.45, anchor='nw')

            self.button_save = customtkinter.CTkButton(self, text="Add Signature")
            self.button_save.place(relx=0.3, rely=0.90, anchor='s')

            self.button_update = customtkinter.CTkButton(self, text="Approve", command=self.approved_and_paid)
            self.button_update.place(relx=0.7, rely=0.90, anchor='s')
    except Exception as e:
        raise TallyException(e, sys) from e
    
    def approved_and_paid(self):
        try:
            print(collec.find_one_and_update({"Client Name": str(self.resort_name), "Amount": str(self.amount), "Reason": str(self.reason)}, {"$set": {"Paid": 1, "Person Name": self.payment_person.get()}}))
            CTkMessagebox(title='Success', message="The Voucher has been successfully updated")
        except Exception as e:
            CTkMessagebox(title='Error', message="There was an error while updating the Voucher")
            raise TallyException(e, sys) from e



class ButtonFrame(customtkinter.CTkFrame):
    try:
        def __init__(self, master, **kwargs):
            super().__init__(master, **kwargs)
            self.edit_button = customtkinter.CTkButton(self, text="Edit (Not Working)", command=self.edit_button)
            self.edit_button.pack(pady=10)
            self.update_button = customtkinter.CTkButton(self, text="Update", command=self.update_selected)
            self.update_button.pack(pady=10)

            self.update_window = None
        
        def update_selected(self):
            try:
                # trv is global data that contains
                x = trv.selection()
                self.update_window = customtkinter.CTkToplevel(self)
                self.update_window.geometry("637x637")
                self.update_window.focus()
                self.update_window.resizable(False, False)
                self.update_window.title("Update")

                #Finding the data from MongoDB
                selected_item = collec.find_one({'Department': trv.item(x)["values"][0], 'Date_time': trv.item(x)["values"][1], 'Client Name': trv.item(x)["values"][2]})


                #Initializing class UpdateFrame
                self.my_frame = UpdateFrame(master=self.update_window, resort_name=trv.item(x)["values"][2], amount=trv.item(x)["values"][4], reason=selected_item['Reason'], height=600, width=600)
                self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
            except Exception:
                print(Exception.__cause__)
                CTkMessagebox(title='Error', message="Please Select a Row")


        def edit_button(self):
            CTkMessagebox(title='Error', message="You are not allowed to Edit")
    except Exception as e:
        raise TallyException(e, sys) from e



class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        try:
            super().__init__(master, **kwargs)
            self.df = pd.DataFrame(columns=["Department", "Date_time", "Client Name", "Person Name", "Amount", "Payment_to", "Approved", "Paid"])
            self.order = True

            try:
                for one_collec in collec.find():
                    if one_collec["Approved"] == 1 and one_collec["Signature"] == 0 and one_collec["Paid"] == 0:
                        self.df.loc[len(self.df.index)] = [one_collec["Department"], one_collec["Date_time"], one_collec["Client Name"], one_collec["Person Name"], one_collec["Amount"], one_collec["Payment_to"], one_collec["Approved"], one_collec["Paid"]]
            except Exception:
                CTkMessagebox(title="Error", message=Exception)

            # This function displays data on screen
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

            self.update_window = None
        except Exception as e:
            raise TallyException(e, sys) from e


    # Function for sorting column 
    def sort_column(self, column):
        try:
            if self.order:
                self.order = False
            else:
                self.order = True
            
            self.df = self.df.sort_values(by=[column], ascending=self.order)
            self.display_data(self.df)
        except Exception as e:
            raise TallyException(e, sys) from e


    # The following function displays all the data in the database
    def display_data(self, dataframe):
        try:
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
        except Exception as e:
            raise TallyException(e, sys) from e

        
