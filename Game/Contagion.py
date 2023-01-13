# Import module 
from tkinter import *
from time import sleep
import threading
import datetime

global infections
global multiplier
global infectivity
global count
global currentdate
infections = -1
infectivity = 1
multiplier = 1
count = 0
currentdate = ''


def add():
    global infections
    global multiplier
    print("a")
    infections += 1*multiplier
    infc.configure(text=("Infections: " + str(infections)))

def tick():
    global count
    global infections
    global infectivity
    global currentdate
    global infc

    print("t")
    
    infections += infectivity
    infc.configure(text=("Infections: " + str(infections)))
    unfecpop.configure(text=("Population Uninfected: " + str(8010529930 - infections )))
    
    count+=1
    currentdate = datetime.date.today() + datetime.timedelta(days=count)
    datelbl.configure(text=("Date: " + str(currentdate)))

    sleep(1)
    t = threading.Timer(1.0, tick)
    t.start()


t = threading.Timer(1.0, tick)
t.start() 


# Create object 
window = Tk()

      
# Adjust details 
window.geometry("1024x576")
window.configure(bg='black')
window.title('Contagion')
window.iconbitmap("contagionicon.ico")
window.resizable(width=False, height=False)


#widgets
global infc
infc=Label(window, text=("Infections: " + str(infections)), fg='white', bg='black', font=("Fixedsys Excelsior 3.01", 30))
infc.place(x=10, y=10)

cornerlogo = PhotoImage(file='cornerlogo.png')
logo = Label(window, image = cornerlogo, highlightthickness = 0, bd = 0)
logo.place(x=670, y=0)

bottomline = PhotoImage(file='bottomline.png')
bline = Label(window, image = bottomline, highlightthickness = 0, bd = 0)
bline.place(x=0, y=135)

tline = Label(window, image = bottomline, highlightthickness = 0, bd = 0)
tline.place(x=0, y=495)

alivepop=Label(window, text=("Population Alive: 8010529930"), fg='green', bg='black', font=("Fixedsys Excelsior 3.01", 12))
alivepop.place(x=750, y=55)

unfecpop=Label(window, text=("Population Uninfected: " + str(8010529930 - infections )), fg='green', bg='black', font=("Fixedsys Excelsior 3.01", 12))
unfecpop.place(x=750, y=80)

datelbl=Label(window, text=("Date: " + str(currentdate)), fg='green', bg='black', font=("Fixedsys Excelsior 3.01", 12))
datelbl.place(x=750, y=105)

irate=Label(window, text=("Infections per day: " + str(infectivity)), fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12))
irate.place(x=12, y=55)

drate=Label(window, text=("Deaths per day: 0"), fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12))
drate.place(x=13, y=80)

cure_prog = Label(window, text =("Cure Progress: 0%"), fg="blue", bg = 'black', font=("Fixedsys Excelsior 3.01", 20))
cure_prog.place(x=475, y=518)

lethality_label = Label(window, text =("Lethality: 0%"), fg="red", bg = 'black', font=("Fixedsys Excelsior 3.01", 20))
lethality_label.place(x=250, y=518)

infectivity_label = Label(window, text =("Infectivity: 0%"), fg="green", bg = 'black', font=("Fixedsys Excelsior 3.01", 20))
infectivity_label.place(x=25, y=518)

points_label = Label(window, text =("Points: 0%"), fg="green", bg = 'black', font=("Fixedsys Excelsior 3.01", 20))
points_label.place(x=25, y=518)


#buttons
infectbtn= PhotoImage(file='infect.png')
btn= Button(window, highlightthickness = 0, bd = 0, width=64, height=62, image=infectbtn, command= add)
btn.place(x=955, y=510)

infec1= Button(window, text="Air Transmission 1", height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12))
infec2= Button(window, text="Land Transmission 1", height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12))
infec3= Button(window, text="Water Transmission 1", height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12))

infec1.place(x=25, y=185)
infec2.place(x=25, y=290)
infec3.place(x=25, y=395)

lethal1= Button(window, text="Symptom: Headache", height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12))
lethal2= Button(window, text="Symptom: Cough", height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12))
lethal3= Button(window, text="Symptom: Nausea", height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12))

lethal1.place(x=250, y=185)
lethal2.place(x=250, y=290)
lethal3.place(x=250, y=395)

misc1= Button(window, text="Misc 1", height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12))
misc2= Button(window, text="Misc 2", height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12))
misc3= Button(window, text="Misc 3", height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12))

misc1.place(x=475, y=185)
misc2.place(x=475, y=290)
misc3.place(x=475, y=395)


# Execute tkinter
tick()
window.mainloop()

