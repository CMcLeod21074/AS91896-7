import tkinter
from tkinter.ttk import *
from tkinter import ttk
import os
import random
main_window = tkinter.Tk()
main_window.title("Julie's Party Hire Store")

def quit():
    main_window.destroy()

def print_details():
    Label (main_window, text="Customer Name\tItem Hired\tQuantity\t Receipt number").grid(row=6, column=0)
    database = open("Julie's Part Hire Store Database.txt","r")
    print_database = database.read()
    Label (main_window, text= print_database,).grid(row=7, column=0)

def append_details():
    customer_name_data="\n"+str(customer_name_entry.get())
    item_hired_data="\t"+str(item_hired_combobox.get())
    item_quantity_data="\t"+str(item_quantity_spinbox.get())
    receipt_number = "\t"+str(random.randint(1,10000))
    customer_data=(customer_name_data+item_hired_data+item_quantity_data+receipt_number)
    database = open("Julie's Part Hire Store Database.txt","a")
    database.write(customer_data)

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
