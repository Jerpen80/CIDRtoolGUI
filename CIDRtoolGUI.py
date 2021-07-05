# Import Module
from tkinter import *
 
# create root window
root = Tk()
 
# root window title and dimension
root.title("Jeroen's CIDR tool 1.1")
# Set geometry (widthxheight)
root.geometry('800x600')
 
# Adding  labels and entries to the root window
intro = Label(root, text = "Welcome to CIDR subnetting tool!")
intro.grid(row = 0, columnspan = 15)

lbl0 = Label(root, text = "Please enter your IP and mask bits: ")
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

lbl4 = Label(root, text = "/")
lbl4.grid(column = 8, row = 1)

smask = Entry(root, width = 2)
smask.grid(column = 9, row = 1)

lbl4 = Label(root, text = "  ")
lbl4.grid(column = 10, row = 1)

fullip = Label(root)
subnetmask = Label(root)
networkadress = Label(root)
broadcastadress = Label(root)
hostnumber = Label(root)

# CIDR functions:

# Converting mask bits into subnet mask
def submask(mask):
    range1 = [25,26,27,28,29,30,31]
    range2 = [17,18,19,20,21,22,23,24]
    range3 = [9,10,11,12,13,14,15,16]
    range4 = [1,2,3,4,5,6,7,8]
    if mask in range1: 
        snm1 = 255
        snm2 = 255
        snm3 = 255
        if mask == 25:
            snm4 = 128
        elif mask == 26:
            snm4 = 192
        elif mask == 27:
            snm4 = 224
        elif mask == 28:
            snm4 = 240
        elif mask == 29:
            snm4 = 248
        elif mask == 30:
            snm4 = 252
        elif mask == 31:
            snm4 = 254
    elif mask in range2:
        snm1 = 255
        snm2 = 255
        snm4 = 0
        if mask == 17:
            snm3 = 128
        elif mask == 18:
            snm3 = 192
        elif mask == 19:
            snm3 = 224
        elif mask == 20:
            snm3 = 240
        elif mask == 21:
            snm3 = 248
        elif mask == 22:
            snm3 = 252
        elif mask == 23:
            snm3 = 254
        elif mask == 24:
            snm3 = 255
    elif mask in range3:
        snm1 = 255
        snm3 = 0
        snm4 = 0
        if mask == 9:
            snm2 = 128
        elif mask == 10:
            snm2 = 192
        elif mask == 11:
            snm2 = 224
        elif mask == 12:
            snm2 = 240
        elif mask == 13:
            snm2 = 248
        elif mask == 14:
            snm2 = 252
        elif mask == 15:
            snm2 = 254
        elif mask == 16:
            snm2 = 255
    elif mask in range4:
        snm2 = 0
        snm3 = 0
        snm4 = 0
        if mask == 1:
            snm1 = 128
        elif mask == 2:
            snm1 = 192
        elif mask == 3:
            snm1 = 224
        elif mask == 4:
            snm1 = 240
        elif mask == 5:
            snm1 = 248
        elif mask == 6:
            snm1 = 252
        elif mask == 7:
            snm1 = 254
        elif mask == 8:
            snm1 = 255
    return snm1,snm2,snm3,snm4

# Calculating Network adress from ip adress and subnetmask with an AND operator
def netwadr(mask,snm1,snm2,snm3,snm4):
    if mask <= 8:
        nwa2 = 0
        nwa3 = 0
        nwa4 = 0
        nwa1 = int(ip1.get()) & snm1
    elif mask <= 16:
        nwa1 = int(ip1.get())
        nwa3 = 0
        nwa4 = 0
        nwa2 = int(ip2.get()) & snm2
    elif mask <= 24:
        nwa1 = int(ip1.get())
        nwa2 = int(ip2.get())
        nwa4 = 0
        nwa3 = int(ip3.get()) & snm3
    else:
        nwa1 = int(ip1.get())
        nwa2 = int(ip2.get())
        nwa3 = int(ip3.get())
        nwa4 = int(ip4.get()) & snm4
    return nwa1, nwa2, nwa3, nwa4

# Calculating Broadcast adress from subnet mask and ip adress with an OR operator
def bcadr(mask,snm1,snm2,snm3,snm4):
    if mask <= 8:
        bca2 = 255
        bca3 = 255
        bca4 = 255
        bca1 = int(ip1.get()) | (255 - snm1)
    elif mask <= 16:
        bca1 = int(ip1.get())
        bca3 = 255
        bca4 = 255
        bca2 = int(ip2.get()) | (255 - snm2)
    elif mask <= 24:
        bca1 = int(ip1.get())
        bca2 = int(ip2.get())
        bca4 = 255
        bca3 = int(ip3.get()) | (255 - snm3)
    else:
        bca1 = int(ip1.get())
        bca2 = int(ip2.get())
        bca3 = int(ip3.get())
        bca4 = int(ip4.get()) | (255 - snm4)
    return bca1, bca2, bca3, bca4

# Calculating hosts with a formula
def hosts(mask):
    host = 2 ** (32 - mask) - 2
    return host

# function to display entries in text when button is clicked
# Also added a check to display 'Invalid IP' in red text if any of the numbers are bigger than 255 
# or no number at all
# Also calls all CIDR functions to display outcome after button is clicked
def clicked():
    try:
        if int(ip1.get()) > 255 or int(ip2.get()) > 255 or int(ip3.get()) > 255 or int(ip4.get()) > 255:
            fullip.configure(text = "Invalid IP or bit mask number" , fg = "red")
            fullip.grid(column = 0, row = 2, columnspan= 7)
        elif int(smask.get()) < 0 or int(smask.get()) > 31:
            fullip.configure(text = "Invalid IP or bit mask number" , fg = "red")
            fullip.grid(column = 0, row = 2, columnspan= 7)
        else:
            fullip.configure(text = "Your IP is: "+ip1.get()+"."+ip2.get()+"."+ip3.get()+"."+ip4.get(), fg = "black")
            fullip.grid(column = 0, row = 2, columnspan= 7)
            mask = int(smask.get())
            snm1,snm2,snm3,snm4 = submask(mask)
            subnetmask.configure(text = "Subnet mask is: "+str(snm1)+"."+str(snm2)+"."+str(snm3)+"."+str(snm4), fg = "black")
            subnetmask.grid(column = 0, row = 3, columnspan = 7)
            nwa1,nwa2,nwa3,nwa4 = netwadr(mask,snm1,snm2,snm3,snm4)
            networkadress.configure(text = "Network adress is: "+str(nwa1)+"."+str(nwa2)+"."+str(nwa3)+"."+str(nwa4), fg = "black")
            networkadress.grid(column = 0, row = 4, columnspan = 7)
            bca1,bca2,bca3,bca4 = bcadr(mask,snm1,snm2,snm3,snm4)
            broadcastadress.configure(text = "Broadcast adress is: "+str(bca1)+"."+str(bca2)+"."+str(bca3)+"."+str(bca4), fg = "black")
            broadcastadress.grid(column = 0, row = 5, columnspan = 7)
            host = hosts(mask)
            hostnumber.configure(text = "Maximum number of hosts in a subnet: "+str(host) , fg = "black")
            hostnumber.grid(column = 0, row = 6, columnspan= 7)

    except ValueError:
        fullip.configure(text = "Invalid IP or bit mask number" , fg = "red")
        fullip.grid(column = 0, row = 2, columnspan= 7)
        
# Adding a button with blue text inside
btn = Button(root, text = "Go!!!" , fg = "blue", command = clicked)

# Set button grid
btn.grid(column = 11, row = 1)

# Execute Tkinter
root.mainloop()