# Import module 
from tkinter import *
from tkinter import ttk

global infections
infections = 1


def add():
    global infections
    print("a")
    infections += 1
    infc.configure(text=("Infections: " + str(infections)))


# Create object 
window = Tk()
      
# Adjust details 
window.geometry("1024x576")
window.title('Contagion')
window.configure(bg='black')


      
# change background
# bg = PhotoImage(file = "background.png")
# label1 = Label( window, image = bg)
# label1.place(x = 0, y = 0)


global infc
infc=Label(window, text=("Infections: " + str(infections)), fg='white', bg='black', font=("Fixedsys Excelsior 3.01", 30))
infc.place(x=10, y=10)

btn=Button(window, text="Spread", fg='black', bg='red', command=lambda : add())
btn.place(x=120, y=70)
  
# Execute tkinter
window.mainloop()

