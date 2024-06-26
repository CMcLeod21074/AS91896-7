import tkinter
from tkinter.ttk import *
from tkinter import ttk
import os
main_window = tkinter.Tk()
main_window.title("Julie's Party Hire Store")

def quit():
    main_window.destroy()

def print_details():
    database = open("Julie's Part Hire Store Database.txt","r")
    blahblahblah = database.read()
    print("test")
    Label (main_window, text= blahblahblah,).grid(row=0, column=1)

def append_details():
    print("Append")

def delete_details():
    print("Delete")
    
def main():
    database = open("Julie's Part Hire Store Database.txt","a")
    database.close()
    Button(main_window, text="Quit", command=quit).grid(column=0, row=0)
    
    #Customer name input
    customer_name = tkinter.Label(append_print_frame, text="Customer Name")
    customer_name.grid(row=0, column=0)

    #Item hired input
    item_hired = tkinter.Label(append_print_frame, text="Item Hired")
    item_hired.grid(row=1, column=0)

    #Item Quantity
    item_quantity = tkinter.Label(append_print_frame, text="Item Quantity")
    item_quantity.grid(row=2, column=0)

    item_quantity_spinbox = tkinter.Spinbox(append_print_frame, from_=1, to=500)
    item_quantity_spinbox.grid(row=2, column=1)

    #Buttons
    Button(append_print_frame, text="Print", command=print_details).grid(column=2, row=5)
    Button(append_print_frame, text="Append", command=append_details).grid(column=1, row=5)

    #Delete Frame
    delete_frame = tkinter.LabelFrame(frame, text="Delete Details")
    delete_frame.grid(row=1, column=5)
    
    delete_item = tkinter.Label(delete_frame, text="Row Number")
    delete_item.grid(row=0, column=0)

    delete_item_entry = tkinter.Entry(delete_frame)
    delete_item_entry.grid(row=0, column=1)
    Button(delete_frame, text="Delete", command=delete_details).grid(column=2, row=5)

    main_window.mainloop()


frame = tkinter.Frame(main_window)
frame.grid(row=1, column=1)

#Append/Print Frame
append_print_frame = tkinter.LabelFrame(frame, text="Append/Print Details")
append_print_frame.grid(row=1, column=1)

customer_name_entry = tkinter.Entry(append_print_frame)
customer_name_entry.grid(row=0, column=1)

item_hired_combobox = ttk.Combobox(append_print_frame, values=["Item 1","Item 2","Item 3"], state="readonly")
item_hired_combobox.grid(row=1, column =1)

item_quantity_spinbox = tkinter.Spinbox(append_print_frame, from_=1, to=500)
item_quantity_spinbox.grid(row=2, column=1)
main()
