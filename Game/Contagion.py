# Import module 
from tkinter import *
  
# Create object 
window = Tk()
  
# Adjust details 
window.geometry("1024x576")
window.title('Contagion')

  
# change background
bg = PhotoImage(file = "background.png")
label1 = Label( window, image = bg)
label1.place(x = 0, y = 0)

  
# Execute tkinter
window.mainloop()
