# Python program to create a
# GUI mark sheet using tkinter
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



def savejson():
    with open('users.json', 'r+') as f:        
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}
            data['students']=[]

    data['students'].append({
        'name':e1.get(),
        'matric':e2.get(),
        'score':int(e3.get())
    }) 

    with open("users.json", "w") as f:
        json.dump(data, f, indent=4)
     

def displayAvg():
    avg = 0
    with open('users.json', 'r+') as f:
        try:
            data = json.load(f)
            for i in data['students']:
                avg += i['score']
                    
        except json.JSONDecodeError:
            return tk.Label(master, text="no data").grid(row=20, column=5)
    
    
    
    tk.Label(master, text=str(avg/len(data['students']))).grid(row=20, column=5)

def displayMax():
    max = 0
    with open('users.json', 'r+') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return tk.Label(master, text="no data").grid(row=22, column=5)


    tk.Label(master, text=str(max)).grid(row=22, column=5)
 
    
# label to enter name
tk.Label(master, text="Name").grid(row=0, column=0)
 
# label for Matric number
tk.Label(master, text="Matric Number").grid(row=0, column=3)
 
# label for score
tk.Label(master, text="Score").grid(row=1, column=0)
 

# taking entries of name, reg, roll number respectively
e1=tk.Entry(master)
e2=tk.Entry(master)
e3=tk.Entry(master)
  
# organizing them in the grid
e1.grid(row=0, column=1)
e2.grid(row=0, column=4)
e3.grid(row=1, column=1)
  
# button to display all the calculated credit scores and sgpa
button1=tk.Button(master, text="submit", bg="green", command=savejson)
button1.grid(row=8, column=1)
  
# button to display all the calculated credit scores and sgpa
button2=tk.Button(master, text="average", bg="green", command=displayAvg)
button2.grid(row=20, column=4)

# button to display all the calculated credit scores and sgpa
button3=tk.Button(master, text="max score", bg="green", command=displayMax)
button3.grid(row=22, column=4)
  
     
master.mainloop()
  
  
