import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="This is a label with a transparent background", bg="systemTransparent")
label.pack()

root.mainloop()
