namestring = '''global infections
    global infectivity
    global points
    global infc_per_pnt
    global cure'''


names = namestring.split()

print("global ", end="")

for i in range(len(names)):
    if i%2!=0:
        print(names[i], end="")
        print(", ", end="")