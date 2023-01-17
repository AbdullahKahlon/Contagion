#Import Modules
from tkinter import *
from time import sleep
import threading
import datetime
import math

global infections
global multiplier
global infectivity
global count
global currentdate
global points
global upgrade_cost_a
global upgrade_cost_b
global upgrade_cost_c
global infectivity_upgrades
global symptom_upgrades
global misc_upgrades
global death
global mutation
mutation = 0.01
death = 0.001
misc_upgrades = {"cure": 0, "mutation": 0, "misc": 0}
symptom_upgrades = {"nausea": 0, "cough": 0, "fever": 0}
infectivity_upgrades = {"air": 0, "land": 0, "water": 0}
upgrade_cost_a = 4
upgrade_cost_b = 16
upgrade_cost_c = 64
infections = -1
infectivity = 1
multiplier = 1
points = 4
infc_per_pnt = 25
count = 0
currentdate = ''


def add():
    global infections
    global infectivity
    global points
    global infc_per_pnt
    print("a")
    infections += 1*infectivity
    points += (1/infc_per_pnt)*infectivity 
    pnts.configure(text=("Points: " + str(math.floor(points))))
    infc.configure(text=("Infections: " + str(infections)))
    
def air_upgrade():
    global points
    global infectivity
    global death
    global infectivity_upgrades
    global upgrade_cost_a
    global infc_per_pnt
    if points >= upgrade_cost_a:
        infectivity_upgrades["air"] += 1
        points -= upgrade_cost_a
        infectivity *= 4.5
        upgrade_cost_a *=256
        infc_per_pnt += 25
    pnts.configure(text=("Points: " + str(math.floor(points))))

def land_upgrade():
    global points
    global infectivity
    global death
    global infectivity_upgrades
    global upgrade_cost_b
    global infc_per_pnt
    if points >= upgrade_cost_b:
        infectivity_upgrades["land"] += 1
        points -= upgrade_cost_b
        infectivity *= 4.5
        upgrade_cost_b *=256
        infc_per_pnt += 25
    pnts.configure(text=("Points: " + str(math.floor(points))))
 
def tick():
    global count
    global infections
    global infectivity
    global currentdate
    global infc
    global points
    global infc_per_pnt

    print("t")
    
    infections += infectivity
    infc.configure(text=("Infections: " + str(infections)))
    points += (1/infc_per_pnt)*infectivity  
    pnts.configure(text=("Points: " + str(math.floor(points))))
    unfecpop.configure(text=("Population Uninfected: " + str(8010529930 - infections )))
    
    count+=1
    currentdate = datetime.date.today() + datetime.timedelta(days=count)
    datelbl.configure(text=("Date: " + str(currentdate)))
    
    irate.configure(text=("Infections per day: " + str(infectivity)))

    infec1.configure(text="Air Transmission " + str(infectivity_upgrades["air"]+1) + "\nCost: " + str(upgrade_cost_a))

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
global pnts
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

pnts = Label(window, text =("Points: " + str(points)), fg="green", bg = 'black', font=("Fixedsys Excelsior 3.01", 20))
pnts.place(x=750, y=518)

clicker_label = Label(window, text =("Infect"), fg="red", bg = 'black', font=("Fixedsys Excelsior 3.01", 14))
clicker_label.place(x=956, y=468)

#buttons
infectbtn= PhotoImage(file='infect.png')
btn= Button(window, highlightthickness = 0, bd = 0, width=64, height=62, image=infectbtn, command= add)
btn.place(x=955, y=510)

infec1= Button(window, text="Air Transmission " + str(infectivity_upgrades["air"]+1) + "\nCost: " + str(upgrade_cost_a), height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12), command=air_upgrade)
infec2= Button(window, text="Land Transmission " + str(infectivity_upgrades["land"]+1) + "\nCost: " + str(upgrade_cost_b), height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12), command=land_upgrade)
infec3= Button(window, text="Water Transmission " + str(infectivity_upgrades["water"]+1), height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12))

infec1.place(x=25, y=185)
infec2.place(x=25, y=290)
infec3.place(x=25, y=395)

lethal1= Button(window, text="Symptom: Fever", height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12))
lethal2= Button(window, text="Symptom: Cough", height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12))
lethal3= Button(window, text="Symptom: Nausea", height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12))

lethal1.place(x=250, y=185)
lethal2.place(x=250, y=290)
lethal3.place(x=250, y=395)

misc1= Button(window, text="Cure Resistance", height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12))
misc2= Button(window, text="Mutation Chance", height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12))
misc3= Button(window, text="Misc 3", height=3, width=22, fg='gray', bg='black', font=("Fixedsys Excelsior 3.01", 12))

misc1.place(x=475, y=185)
misc2.place(x=475, y=290)
misc3.place(x=475, y=395)


# Execute tkinter
tick()
window.mainloop()

