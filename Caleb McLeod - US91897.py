import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import tkinter as tk
import os
import random
main_window = tk.Tk()
main_window.title("Julie's Party Hire Store")
main_window.configure(background='#ccf2ff')

details_window =tk.Toplevel(main_window)
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
    for widget in details_frame.grid_slaves():
        widget.grid_forget() #Hides widget
        
    tkinter.Label(details_frame, text="Customer Name", bg="#ccf2ff").grid(row=6, column=0)
    tkinter.Label(details_frame, text="\t", bg="#ccf2ff").grid(row=6, column=1)
    tkinter.Label(details_frame, text="Item Hired", bg="#ccf2ff").grid(row=6, column=2)
    tkinter.Label(details_frame, text="\t", bg="#ccf2ff").grid(row=6, column=3)
    tkinter.Label(details_frame, text="Quantity", bg="#ccf2ff").grid(row=6, column=4)
    tkinter.Label(details_frame, text="\t", bg="#ccf2ff").grid(row=6, column=5)
    tkinter.Label(details_frame, text="Receipt number", bg="#ccf2ff").grid(row=6, column=6)

    try:
        with open("Julie's Party Hire Store Database.txt","r") as database:# With opens and closes file
            database_list = database.read().split(",")
            
        row = 1
        for entry in database_list:
            if len (database_list) ==4:
                tkinter.Label(details_frame, text=database_list[0], bg="#ccf2ff").grid(row=row, column=0)
                tkinter.Label(details_frame, text=database_list[1], bg="#ccf2ff").grid(row=row, column=1)
                tkinter.Label(details_frame, text=database_list[2], bg="#ccf2ff").grid(row=row, column=2)
                tkinter.Label(details_frame, text=database_list[3], bg="#ccf2ff").grid(row=row, column=3)
                row +=1

    except:
        print ("No data to display")

    
      #  row = 0
       # i = 0
     #   col = 0
    #while i < len(database_list):
        col = 0
       ## while col < 8 and i < len(database_list):
            #tkinter.Label (details_frame, text= database_list[i], bg="#ccf2ff").grid(row=7+row, column=col)
        #    i+=1
         #   col+=2
      #  row+=1

#Append Details Functions        
def append_details():
    #Receipt Number
    global receipt_no
    customer_receipt = customer_name_entry.get()
    receipt_no = random.randint(100,9999) * ord(customer_receipt[0])

    #Appends Details
    customer_name_data=str(customer_name_entry.get())
    item_hired_data=","+str(item_hired_combobox.get())
    
    item_quantity_data=","+str(item_quantity_spinbox.get())
    
    receipt_number = ","+str(receipt_no)+','"\n"
    customer_data=(customer_name_data+item_hired_data+item_quantity_data+receipt_number)
    database = open("Julie's Party Hire Store Database.txt","a")
    database.write(customer_data)
    database.close()
   
    
def delete_details():
    delete_receipt = delete_item_entry.get()
    database = open("Julie's Party Hire Store Database.txt","r")
    temp_data = open("Temp.txt","w")
    for line in database:
        database_list = line.split(",")
        if database_list[3] != delete_receipt:
            temp_data.write(line)
            print(database_list)
    database.close()
    temp_data.close()

    database = open("Julie's Party Hire Store Database.txt","w")
    temp_data = open("Temp.txt","r")
    
    database.write(temp_data.read())
    database.close()
    temp_data.close()
    print_details()
def main():
    database = open("Julie's Party Hire Store Database.txt","a")
    database.close()

    #details_window.withdraw()
    
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
    
    delete_item = tkinter.Label(delete_frame, text="Receipt Number",bg='#ccf2ff')
    delete_item.grid(row=0, column=0)

    global delete_item_entry
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
