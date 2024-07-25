import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import os
import random
main_window = tkinter.Tk()
main_window.title("Julie's Party Hire Store")
main_window.configure(background='#ccf2ff')
details_window = Toplevel(main_window)
details_window.title("Details")
details_window.configure(background='#ccf2ff')

#Main Window Quit Function
def quit():
    main_window.destroy()

#details Window quit Function
def details_quit():
    details_window.withdraw()
    
#Print details function
def print_details():
    details_window.deiconify()
    tkinter.Label(details_frame, text="Customer Name", bg="#ccf2ff").grid(row=6, column=0)
    tkinter.Label (details_frame, text="\t", bg="#ccf2ff").grid(row=6, column=1)
    tkinter.Label (details_frame, text="Item Hired", bg="#ccf2ff").grid(row=6, column=2)
    tkinter.Label (details_frame, text="\t", bg="#ccf2ff").grid(row=6, column=3)
    tkinter.Label (details_frame, text="Quantity", bg="#ccf2ff").grid(row=6, column=4)
    tkinter.Label (details_frame, text="\t", bg="#ccf2ff").grid(row=6, column=5)
    tkinter.Label (details_frame, text="Receipt number", bg="#ccf2ff").grid(row=6, column=6)
    database = open("Julie's Part Hire Store Database.txt","r")
    database_list = database.read().split(",")

    #Formats Data Labels
    row = 0
    i = 0
    col = 0
    while i < len(database_list):
        col = 0
        while col < 8 and i < len(database_list):
            tkinter.Label (details_frame, text= database_list[i], bg="#ccf2ff").grid(row=7+row, column=col)
            i+=1
            col+=2
        row+=1

#Append Details Functions        
def append_details():
    customer_name_data=str(customer_name_entry.get())
    item_hired_data=","+str(item_hired_combobox.get())
    
    item_quantity_data=","+str(item_quantity_spinbox.get())


    
    receipt_number = ","+str(random.randint(10000,99999))+','"\n"
    customer_data=(customer_name_data+item_hired_data+item_quantity_data+receipt_number)
    database = open("Julie's Part Hire Store Database.txt","a")
    database.write(customer_data)
    
    
def delete_details():
    print("Delete")
    
def main():
    database = open("Julie's Part Hire Store Database.txt","a")
    database.close()

    details_window.withdraw()
    
    #Main Window Quit Button
    Button(main_window, text="Quit", command=quit).grid(column=0, row=0)

    #Details Window Quit Button
    Button(details_window, text="Quit", command=details_quit).grid(column=0, row=0)

    
    #Customer name input
    customer_name = tkinter.Label(append_print_frame, text="Customer Name",bg='#ccf2ff', font='arial')
    customer_name.grid(row=0, column=0)

    #Item hired input
    item_hired = tkinter.Label(append_print_frame, text="Item Hired",bg='#ccf2ff')
    item_hired.grid(row=1, column=0)

    #Item Quantity
    
    item_quantity = tkinter.Label(append_print_frame, text="Item Quantity",bg='#ccf2ff')
    item_quantity.grid(row=2, column=0)

    global item_quantity_spinbox
    item_quantity_spinbox = tkinter.Spinbox(append_print_frame, from_=1, to=500)
    item_quantity_spinbox.grid(row=2, column=1)

    #Print Button
    Button(append_print_frame, text="Print", command=print_details).grid(column=2, row=5)

    #Append Button
    Button(append_print_frame, text="Append", command=append_details).grid(column=1, row=5)

    #Delete Frame
    delete_frame = tkinter.LabelFrame(frame,bg='#ccf2ff', text="Delete Details")
    delete_frame.grid(row=1, column=2)
    
    delete_item = tkinter.Label(delete_frame, text="Row Number",bg='#ccf2ff')
    delete_item.grid(row=0, column=0)

    delete_item_entry = tkinter.Entry(delete_frame)
    delete_item_entry.grid(row=0, column=1)

    #Delete Button
    Button(delete_frame, text="Delete", command=delete_details).grid(column=2, row=5)

    main_window.mainloop()
    


frame = tkinter.Frame(main_window,bg='#ccf2ff')
frame.grid(row=1, column=1)

#Details Frame
details_frame = tkinter.LabelFrame(details_window,bg='#ccf2ff', text="Details")
details_frame.grid(row=2, column=1)

#Append/Print Frame
append_print_frame = tkinter.LabelFrame(frame,bg='#ccf2ff', text="Append/Print Details")
append_print_frame.grid(row=1, column=1)

customer_name_entry = tkinter.Entry(append_print_frame)
customer_name_entry.grid(row=0, column=1)

item_hired_combobox = ttk.Combobox(append_print_frame, values=["Item 1","Item 2","Item 3"], state="readonly")
item_hired_combobox.grid(row=1, column =1)

item_quantity_spinbox = tkinter.Spinbox(append_print_frame, from_=1, to=500)
item_quantity_spinbox.grid(row=2, column=1)
main()
