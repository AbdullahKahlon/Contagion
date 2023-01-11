# Import module 
from tkinter import *
from time import sleep
import threading

global infections
global multiplier
global infectivity
infections = 0
infectivity = 1
multiplier = 1


def add():
    global infections
    global multiplier
    print("a")
    infections += 1*multiplier
    infc.configure(text=("Infections: " + str(infections)))

def passive():
    global infections
    global infectivity
    print("p")
    infections += infectivity
    infc.configure(text=("Infections: " + str(infections)))
    sleep(1)
    t = threading.Timer(1.0, passive)
    t.start()


t = threading.Timer(1.0, passive)
t.start() 


# Create object 
window = Tk()
      
# Adjust details 
window.geometry("1024x576")
window.title('Contagion')
window.configure(bg='black')


#widgets
#global infc
infc=Label(window, text=("Infections: " + str(infections)), fg='white', bg='black', font=("Fixedsys Excelsior 3.01", 30))
infc.place(x=400, y=10)

btn=Button(window, text="Spread", height= 2, width=10, fg='black', bg='red', font=("Fixedsys Excelsior 3.01", 12), command=lambda : add())
btn.place(x=490, y=70)
  
# Execute tkinter
passive()
window.mainloop()

