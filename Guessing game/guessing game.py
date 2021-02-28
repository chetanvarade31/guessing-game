from tkinter import *
import random

from  PIL import ImageTk, Image



global attempt
attempt = 0

win = Tk()
win.geometry("600x600")
win.maxsize(600,600)
win.title("GUESS NUMBER !!")

# set wining number from random 
winning = random.randint(1,100)
# set background image 
img = Image.open("background.png")
img1 = ImageTk.PhotoImage(img)

first = IntVar()
seconf = StringVar()
third = IntVar()

# create canva :
canava = Canvas(win,width= 600,height= 600)
canava.create_image(0,0,image =img1 )# set image on background using canva 
def restart():

    global winning
    global attempt
    attempt = 0
    

    winning = random.randint(1,100)  

    third.set("")
    seconf.set("")
    first.set("")
    

    
def submit():

    global attempt
    attempt = attempt + 1
    
    e1  = str(entry_1.get())
    str(entry_2.get())

    e1  = int(e1)
    
    if e1 == winning:

        string= f"YOU GUESS IN {attempt} ATTEMPT !!"

        seconf.set("!!! YOU ARE WIN !!! ")
        third.set(string)
        
    else:
        if e1 > winning:

            seconf.set("YOU GUESS TOO HIGH !!")

        else:

            seconf.set("YOU GUESS TOO LOW !!")
        

    
lable = Label(win, text="GUESS THE NUMBER BETWEEN 1 TO 100 ",bg= "black",fg= "yellow",font= ("Courier",18,"bold"),justify= CENTER)
lable.place(x = 50, y = 50)

entry_1 = Entry(win,textvariable= first,fg  = "red",bg= "black",font= ("Arial",20,"bold"))
entry_1.place(x = 150, y = 125)

entry_2 = Entry(win,textvariable=seconf,bg= "black",fg= "yellow",font= ("Courier",18,"bold"),width= 35,justify= CENTER)
entry_2.place(x = 65,y=300 )

button = Button(win, text= "SUBMIT",fg= "red",bd= "8" ,bg= "black",font= ("Courier",20,"bold"),command= submit)
button.place(x= 240, y = 200)

button1 = Button(win, text= "RESTART",fg = "red",bg = "black",bd= "8",font= ("Courier",20,"bold"),command= restart)
button1.place(x = 150, y= 475)

button3 = Button(win, text= "EXIT",fg="red",bg= "black",bd = "8",font= ("Courier",20,"bold"),command= win.destroy)
button3.place(x = 375,y = 475)

lable1 = Label(win,fg= "yellow",bg= "black",textvariable= third,font= ("Courier",18,"bold"))
lable1.place(x= 150, y= 400)

canava.pack()


win.mainloop()