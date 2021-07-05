# Import Module
from tkinter import *
 
# create root window
root = Tk()
 
# root window title and dimension
root.title("My first Python GUI")
# Set geometry (widthxheight)
root.geometry('800x600')
 
# Adding  labels and entries to the root window
lbl0 = Label(root, text = "Please enter your IP: ")
lbl0.grid(column = 0, row = 1)

ip1 = Entry(root, width = 3)
ip1.grid(column = 1, row = 1)

lbl1 = Label(root, text = ".")
lbl1.grid(column = 2, row = 1)

ip2 = Entry(root, width = 3)
ip2.grid(column = 3, row = 1)

lbl2 = Label(root, text = ".")
lbl2.grid(column = 4, row = 1)

ip3 = Entry(root, width = 3)
ip3.grid(column = 5, row = 1)

lbl3 = Label(root, text = ".")
lbl3.grid(column = 6, row = 1)

ip4 = Entry(root, width = 3)
ip4.grid(column = 7, row = 1)

lbl4 = Label(root, text = "  ")
lbl4.grid(column = 8, row = 1)

fullip = Label(root)
fullip.grid(column = 0, row = 2)


# function to display entries in red text when button is clicked
# Also added a check to display 'Invalid IP' if any of the numbers are bigger than 255  
def clicked():
    if int(ip1.get()) > 255:
        fullip.configure(text = "Invalid IP" , fg = "red")
        fullip.grid(column = 0, row = 2, columnspan= 7)
    elif int(ip2.get()) > 255:
        fullip.configure(text = "Invalid IP" , fg = "red")
        fullip.grid(column = 0, row = 2, columnspan= 7)
    elif int(ip3.get()) > 255:
        fullip.configure(text = "Invalid IP" , fg = "red")
        fullip.grid(column = 0, row = 2, columnspan= 7)
    elif int(ip4.get()) > 255:
        fullip.configure(text = "Invalid IP" , fg = "red")
        fullip.grid(column = 0, row = 2, columnspan= 7)
    else:
        fullip.configure(text = "Your IP is: "+ip1.get()+"."+ip2.get()+"."+ip3.get()+"."+ip4.get() , fg = "black")
        fullip.grid(column = 0, row = 2, columnspan= 7)

# Adding a button with blue text inside
btn = Button(root, text = "Show IP" , fg = "blue", command = clicked)

# Set button grid
btn.grid(column = 9, row = 1)

# Execute Tkinter
root.mainloop()