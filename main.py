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
master.geometry("1200x250")


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
    if not e1.get().isalpha():
        return tk.Label(master, text="  invalid name  ").grid(row=9, column=1)
    if not e2.get().isalpha():
        return tk.Label(master, text="  invalid surname  ").grid(row=9, column=1)
    if not e3.get().isdigit():
        return tk.Label(master, text="   invalid score    ").grid(row=9, column=1)
    if int(e3.get()) < 0 or int(e3.get()) > 100:
        return tk.Label(master, text="   invalid score    ").grid(row=9, column=1)
    if not e4.get().isdigit():
        return tk.Label(master, text="  invalid matric  ").grid(row=9, column=1)
    if len(e4.get()) != 9:
        return tk.Label(master, text="  invalid matric  ").grid(row=9, column=1)
    

    for i in data['students']:
        if int(e4.get()) == i['matric']:
            return tk.Label(master, text="    user exists    ").grid(row=9, column=1)

    try:
        data['students'].append({
            'name':e1.get(),
            'surname':e2.get(),
            'score':int(e3.get()),
            'matric':int(e4.get())  
        })
    except ValueError:
        return tk.Label(master, text="   invalid input    ").grid(row=9, column=1)
    
    #write user into file
    with open("users.json", "w") as f:
        json.dump(data, f, indent=4)
    
    tk.Label(master, text="  succesful input  ").grid(row=9, column=1)

#function to delete user using matric no
def deleteUser():
    with open('users.json', 'r+') as f:        
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}
            data['students']=[]
    try:
        matric = int(e4.get())  
    except ValueError:
        return tk.Label(master, text="   invalid input    ").grid(row=9, column=1)

    if len(data)==0:
        return tk.Label(master, text="   no user found    ").grid(row=9, column=1)
    i=0
    for dict in data['students']:
        if matric == dict['matric']:
            del data['students'][i]
            #rewrite the new data into json file
            with open("users.json", "w") as f:
                json.dump(data, f, indent=4)
            return tk.Label(master, text="  user deleted  ").grid(row=9, column=1)
        i+=1
    
    tk.Label(master, text="  no user found  ").grid(row=9, column=1)

#function to display average of the entire scores
label1 = tk.Label(master, text="")
label1.grid(row=20, column=5)
def displayAvg():
    avg = 0
    with open('users.json', 'r+') as f:
        try:
            data = json.load(f)
            if len(data['students']) == 0:
                return label1.configure(text="no data")
            for i in data['students']:
                avg += i['score']  
            
        except json.JSONDecodeError:
            return label1.configure(text="no data")
    
    #widget for average score
    return label1.config(text="Average: " + str(round(avg/len(data['students']),2)))

#function to display maximum scoring students 
label2 = tk.Label(master, text="")
label2.grid(row=22, column=5)
def displayMax():
    allvalues = []
    max_students=[]
    with open('users.json', 'r+') as f:
        try:
            data = json.load(f)
            if len(data['students']) == 0:
                return label2.config(text="no data")
            for i in data['students']:
                allvalues += [i['score']]
            for i in data['students']:
                if i['score'] == max(allvalues):
                    max_students+=list(i.values())        
        except json.JSONDecodeError:
            return label2.config(text="no data")

    return label2.config(text=max_students, wraplength=700)

#function to display the minimum scoring students
label3 = tk.Label(master, text="")
label3.grid(row=24, column=5)
def displayMin():
    allvalues = []
    min_students=[]
    with open('users.json', 'r+') as f:
        try:
            data = json.load(f)
            if len(data['students']) == 0:
                return label3.config(text="no data")
            for i in data['students']:
                allvalues += [i['score']]
            for i in data['students']:
                if i['score'] == min(allvalues):
                    min_students+=list(i.values())
        except json.JSONDecodeError:
            return label3.config(text="no data")

    return label3.config(text=min_students, wraplength=700)
                
#function to display students that scored below 40
label4 = tk.Label(master, text="")
label4.grid(row=26, column=5)
def displayFailed():
    allvalues = []
    with open('users.json', 'r+') as f:
        try:
            data = json.load(f)
            if len(data['students']) == 0:
                return label4.config(text="no data")
            for i in data['students']:
                if i['score'] < 40:
                    allvalues+=list(i.values())
            if len(allvalues)==0:
                return label4.config(text="no data")
        except json.JSONDecodeError:
            return label4.config(text="no data")

    return label4.config(text=allvalues, wraplength=700)

#function to display students who scored above 69
label5 = tk.Label(master, text="")
label5.grid(row=28, column=5)
def displayTop():
    allvalues = []
    with open('users.json', 'r+') as f:
        try:
            data = json.load(f)
            if len(data['students']) == 0:
                return label5.config(text="no data")
            for i in data['students']:
                if i['score'] > 69:
                    allvalues+=list(i.values())
            if len(allvalues) == 0:
                return label5.config(text="no data")
        except json.JSONDecodeError:
            return label5.config(text="no data")

    return label5.config(text=allvalues, wraplength=700)

    
# label to enter name
tk.Label(master, text="Name").grid(row=0, column=0)
 
# label to enter surname
tk.Label(master, text="Surname").grid(row=0, column=3)
 
# label for Matric number
tk.Label(master, text="Matric Number").grid(row=1, column=3)
 
# label for score
tk.Label(master, text="Score").grid(row=1, column=0)
 
# taking entries of name, matric number and score respectively
e1=tk.Entry(master)
e2=tk.Entry(master)
e3=tk.Entry(master)
e4=tk.Entry(master)
  
# organizing them in the grid
e1.grid(row=0, column=1)
e2.grid(row=0, column=4)
e3.grid(row=1, column=1)
e4.grid(row=1, column=4)
  
# button to save new students in json file
button1=tk.Button(master, bd=1, text="Save", bg="green", command=savejson)
button1.grid(row=8, column=1)

#button to delete user
button1=tk.Button(master, bd=1, text="Delete", bg="green", command=deleteUser)
button1.grid(row=8, column=3)
  
# button to display the average score
button2=tk.Button(master, bd=1, text="Mean Score", bg="green", command=displayAvg)
button2.grid(row=20, column=4)

# button to display best scoring students
button3=tk.Button(master, bd=1, text="Best Student(s)", bg="green", command=displayMax)
button3.grid(row=22, column=4)

# button to display least scoring students
button3=tk.Button(master, bd=1, text="Least Scoring Student(s)", bg="green", command=displayMin)
button3.grid(row=24, column=4)

# button to display failed students
button3=tk.Button(master, bd=1, text="Student(s) below 40", bg="green", command=displayFailed)
button3.grid(row=26, column=4)

# button to display students 70 and above
button3=tk.Button(master, bd=1, text="Student(s) above 69", bg="green", command=displayTop)
button3.grid(row=28, column=4)
  
if __name__ == "__main__":    
    master.mainloop()
  
  
