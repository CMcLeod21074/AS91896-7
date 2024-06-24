import tkinter
from tkinter.ttk import *
from tkinter import ttk
main_window = tkinter.Tk()
main_window.title("Julie's Party Hire Store")

def quit():
    main_window.destroy()


    
def main():
    Button(main_window, text="Quit", command=quit).grid(column=0, row=0)
    
    frame = tkinter.Frame(main_window)
    frame.grid(row=1, column=1)

    append_print_frame = tkinter.LabelFrame(frame, text="Append/Print Details")
    append_print_frame.grid(row=1, column=1)

    #Customer name input
    customer_name = tkinter.Label(append_print_frame, text="Customer Name")
    customer_name.grid(row=0, column=0)

    customer_name_entry = tkinter.Entry(append_print_frame)
    customer_name_entry.grid(row=0, column=1)

    #Item hired input
    item_hired = tkinter.Label(append_print_frame, text="Item Hired")
    item_hired.grid(row=1, column=0)

    item_hired_combobox = ttk.Combobox(append_print_frame, values=["Item 1","Item 2","Item 3"], state="readonly")
    item_hired_combobox.grid(row=1, column =1)

    #Item Quantity
    item_quantity = tkinter.Label(append_print_frame, text="Item Quantity")
    item_quantity.grid(row=2, column=0)

    item_quantity_spinbox = tkinter.Spinbox(append_print_frame, from_=1, to=500)
    item_quantity_spinbox.grid(row=2, column=1)



main()
