#Author: Caleb McLeod
#Date: 16/08/24
#Purpose: To allow the user to hire and return items from a store
#------------------------

import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askyesno
import os
import random
main_window = tkinter.Tk() # Creating the main Window.
main_window.title("Julie's Party Hire Store")
main_window.configure(background='#ccf2ff')

details_window =tkinter.Toplevel(main_window) # Creating the details Window.
details_window.title("Details")
details_window.configure(background='#ccf2ff')


def quit(): # Main Window Quit Function.
    main_window.destroy()


def details_quit(): # Details Window quit Function.
    details_window.withdraw()
    

def display_details(): # Print details function.
    for widget in details_frame.grid_slaves():
        widget.grid_forget() # Hides widget.
        
    tkinter.Label(details_frame, text="Customer Name", bg="#ccf2ff", font='courier').grid(row=6, column=0)
    tkinter.Label(details_frame, text="\t", bg="#ccf2ff").grid(row=6, column=1)
    tkinter.Label(details_frame, text="Item Hired", bg="#ccf2ff", font='courier').grid(row=6, column=2)
    tkinter.Label(details_frame, text="\t", bg="#ccf2ff").grid(row=6, column=3)
    tkinter.Label(details_frame, text="Quantity", bg="#ccf2ff", font='courier').grid(row=6, column=4)
    tkinter.Label(details_frame, text="\t", bg="#ccf2ff").grid(row=6, column=5)
    tkinter.Label(details_frame, text="Receipt number", bg="#ccf2ff", font='courier').grid(row=6, column=6)

    try:
        with open("Julie's Party Hire Store Database.txt","r") as database:# With opens and closes file.
            database_list = database.read().strip().split("\n")
            
        row = 17
        for entry in database_list:
            data = entry.split(",")
            if len (data) ==5:
                tkinter.Label(details_frame, text=data[0], bg="#ccf2ff").grid(row=row, column=0)
                tkinter.Label(details_frame, text=data[1], bg="#ccf2ff").grid(row=row, column=2)
                tkinter.Label(details_frame, text=data[2], bg="#ccf2ff").grid(row=row, column=4)
                tkinter.Label(details_frame, text=data[3], bg="#ccf2ff").grid(row=row, column=6)
                row +=1

    except FileNotFoundError:
        print ("File not found")



def append_validation():# User Input Validation Function.
    CustomerName_TempOne = customer_name_entry.get().strip()# Name validation.
    CustomerName_TempTwo = CustomerName_TempOne.replace(" ", "")
    customer_name_check = CustomerName_TempTwo.isalpha()
 
    item_check = item_hired_combobox.get()# Item validation.
    
    ItemQuantity_TempOne = item_quantity_spinbox.get().strip()# Quantity validation.
    item_quantity_check = ItemQuantity_TempOne.isdigit()

    if customer_name_check == False: # Name validation.
        messagebox.showerror(title="Error", message="Please enter only text in the name field")

    elif len(item_check) == 0:# Item Validation.
        messagebox.showerror(title="Error", message="Please select an item")
 
    elif item_quantity_check == False:# Quantity validation.
        messagebox.showerror(title="Error", message="Item quantity must only contain integers and be between 1-500")

    elif item_quantity_check == True:
        item_quantity_temp = int(item_quantity_spinbox.get())
        if not item_quantity_temp <=500 or not item_quantity_temp >=1:
            messagebox.showerror(title="Error", message="Item quantity must only contain integers and be between 1-500")
        else:
            confirm_append()

    else:
        confirm_append()
        
def delete_validation():# Delete validation.
    receipt_error = 0
    delete_receipt = delete_item_entry.get()
    database = open("Julie's Party Hire Store Database.txt","r")
    for line in database:
        database_list = line.split(",")
        if database_list[3] != delete_receipt:
            receipt_error = True
    
        else:
            receipt_error = False
            confirm_delete()
            break
            
    if receipt_error == True:
        messagebox.showerror(title="Error", message="No data found matching that receipt number")
        

def confirm_append():# Append Confirmation Function.
   confirm_append = askyesno(title="Append Confirmation", message="Do you want to append this information?")
   if confirm_append == True:
       append_details()

       
def append_details():# Append Details Function.
    global receipt_no# Receipt Number.
    customer_receipt = customer_name_entry.get()
    receipt_no = random.randint(100,9999)* ord(customer_receipt[0])

    
    customer_name_data=str(customer_name_entry.get())# Appends Details.
    item_hired_data=","+str(item_hired_combobox.get())
    item_quantity_data=","+str(item_quantity_spinbox.get())
    receipt_number = ","+str(receipt_no)+','"\n"
    customer_data=(customer_name_data+item_hired_data+item_quantity_data+receipt_number)
    database = open("Julie's Party Hire Store Database.txt","a")
    database.write(customer_data)
    database.close()

    
def confirm_delete():
    confirm_delete = askyesno(title="Delete Confirmation", message="Do you want to delete this information? (This action cannot be undone)")
    if confirm_delete == True:
        delete_details()
    
def delete_details():
    delete_receipt = delete_item_entry.get()
    database = open("Julie's Party Hire Store Database.txt","r")
    temp_data = open("Temp.txt","w")
    for line in database:
        database_list = line.split(",")
        if database_list[3] != delete_receipt:
            temp_data.write(line)
    database.close()
    temp_data.close()

    database = open("Julie's Party Hire Store Database.txt","w")
    temp_data = open("Temp.txt","r")
    
    database.write(temp_data.read())
    database.close()
    temp_data.close()
    display_details()
    
def main():
    database = open("Julie's Party Hire Store Database.txt","a")
    database.close()



    icon = tkinter.PhotoImage(file="icon1.png")# Image.
    icon_label = tkinter.Label(append_print_frame,image=icon, bg="#ccf2ff")
    icon_label.grid()
    
    
    Button(main_window, text="Quit", command=quit).grid(column=0, row=0)# Main Window Quit Button.

    
    customer_name = tkinter.Label(append_print_frame, text="Customer Name",bg='#ccf2ff', font='courier')# Customer name.
    customer_name.grid(row=0, column=0)

    
    item_hired = tkinter.Label(append_print_frame, text="Item Hired",bg='#ccf2ff', font='courier')# Item hired.
    item_hired.grid(row=1, column=0)

    
    item_quantity = tkinter.Label(append_print_frame, text="Item Quantity",bg='#ccf2ff', font='courier')# Item Quantity.
    item_quantity.grid(row=2, column=0)

    global item_quantity_spinbox
    item_quantity_spinbox = tkinter.Spinbox(append_print_frame, from_=1, to=500)
    item_quantity_spinbox.grid(row=2, column=1)

    
    Button(append_print_frame, text="Display", command=display_details).grid(column=2, row=5)# Display Button.

    
    Button(append_print_frame, text="Append", command=append_validation).grid(column=1, row=5)# Append Button.

    
    delete_frame = tkinter.LabelFrame(frame,bg='#ccf2ff', text="Delete Details", font='courier')# Delete Frame.
    delete_frame.grid(row=1, column=2)
    
    delete_item = tkinter.Label(delete_frame, text="Receipt Number",bg='#ccf2ff', font='courier')# Receipt Number to delete.
    delete_item.grid(row=0, column=0)

    global delete_item_entry
    delete_item_entry = tkinter.Entry(delete_frame)
    delete_item_entry.grid(row=0, column=1)

    
    Button(delete_frame, text="Delete", command=delete_validation).grid(column=2, row=5)# Delete Button.

    
    main_window.mainloop()
    


frame = tkinter.Frame(main_window,bg='#ccf2ff')
frame.grid(row=1, column=1)


details_frame = tkinter.LabelFrame(details_window,bg='#ccf2ff', text="Details", font='courier')# Details Frame.
details_frame.grid(row=2, column=1)


append_print_frame = tkinter.LabelFrame(frame,bg='#ccf2ff', text="Append/Display Details", font='courier')# Append/Print Frame.
append_print_frame.grid(row=1, column=1)


customer_name_entry = tkinter.Entry(append_print_frame)# Customer Name Entry.
customer_name_entry.grid(row=0, column=1)


global item_hired_combobox
item_hired_combobox = ttk.Combobox(append_print_frame, values=["Table(s)","Chair(s)","Bouncy Castle(s)"], state="readonly")# Item Hired Combobox.
item_hired_combobox.grid(row=1, column =1)


item_quantity_spinbox = tkinter.Spinbox(append_print_frame, from_=1, to=500)# Item Quantity Spinbox.
item_quantity_spinbox.grid(row=2, column=1)

main()
