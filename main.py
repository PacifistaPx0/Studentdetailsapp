# Python program to create a
# GUI mark sheet using tkinter
from tkinter import *
import tkinter as tk
import json

 
 
 
# creating a new tkinter window
master = tk.Tk()
 
# assigning a title
master.title("MARKSHEET")
 
# specifying geometry for window size
master.geometry("700x250")
 
 
# declaring objects for entering data
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)




#function to append or write user details to json file
#if json file is empty it creates an empty dictionary
def savejson():
    
    with open('users.json', 'r+') as f:        
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}
            data['students']=[]
    
    
    
    #error handling
    if len(e2.get()) != 9:
        return tk.Label(master, text="  invalid matric  ").grid(row=1, column=4)
    if int(e3.get()) < 0 or int(e3.get()) > 100:
        return tk.Label(master, text="   invalid score    ").grid(row=1, column=4)

    for i in data['students']:
        if int(e2.get()) == i['matric']:
            return tk.Label(master, text="   user exists   ").grid(row=1, column=4)

    try:
        data['students'].append({
            'name':e1.get(),
            'matric':int(e2.get()),
            'score':int(e3.get())
        })
    except ValueError:
        return tk.Label(master, text="   invalid input    ").grid(row=1, column=4)
    #write user into file
    
    with open("users.json", "w") as f:
        json.dump(data, f, indent=4)
    
    tk.Label(master, text="  succesful input  ").grid(row=1, column=4)
    
     
#function to display average of the entire score
def displayAvg():
    avg = 0
    with open('users.json', 'r+') as f:
        try:
            data = json.load(f)
            for i in data['students']:
                avg += i['score']
                    
        except json.JSONDecodeError:
            return tk.Label(master, text="no data").grid(row=20, column=5)
    
    #widget for average score
    tk.Label(master, text=str(avg/len(data['students']))).grid(row=20, column=5)

#function to display max score 
def displayMax():
    allvalues = []
    with open('users.json', 'r+') as f:
        try:
            data = json.load(f)
            for i in data['students']:
                allvalues += [i['score']]
        except json.JSONDecodeError:
            return tk.Label(master, text="no data").grid(row=22, column=5)


    tk.Label(master, text=str(max(allvalues))).grid(row=22, column=5)
 
    
# label to enter name
tk.Label(master, text="Name").grid(row=0, column=0)
 
# label for Matric number
tk.Label(master, text="Matric Number").grid(row=0, column=3)
 
# label for score
tk.Label(master, text="Score").grid(row=1, column=0)
 

# taking entries of name, matric number and score respectively
e1=tk.Entry(master)
e2=tk.Entry(master)
e3=tk.Entry(master)
  
# organizing them in the grid
e1.grid(row=0, column=1)
e2.grid(row=0, column=4)
e3.grid(row=1, column=1)
  
# button to save new students in json file
button1=tk.Button(master, text="submit", bg="green", command=savejson)
button1.grid(row=8, column=1)
  
# button to display the average score
button2=tk.Button(master, text="average", bg="green", command=displayAvg)
button2.grid(row=20, column=4)

# button to display the max score
button3=tk.Button(master, text="max score", bg="green", command=displayMax)
button3.grid(row=22, column=4)
  
     
master.mainloop()
  
  
