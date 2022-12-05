# Python program to create a
# GUI mark sheet using tkinter
from tkinter import *
import tkinter as tk
import json
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
 
# creating a new tkinter window
master = customtkinter.CTk()
 
# assigning a title
master.title("MARKSHEET")
 
# specifying geometry for window size
master.geometry("700x800")
master.resizable(False,False)



#function to append or write user details to json file
#if json file is empty it creates an empty dictionary

label0 = customtkinter.CTkLabel(master, text="")#label to display error or successful messages to user
label0.grid(row=5, column=0)
def savejson():
    
    with open('users.json', 'r+') as f:        
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}
            data['students']=[]
    
    #error handling
    if not e1.get().isalpha():
        return label0.configure(text="invalid name input(alphabet required)")
    if not e2.get().isalpha():
        return label0.configure(text="invalid surname input(alphabet required)")
    if not e3.get().isdigit():
        return label0.configure(text="invalid user score")
    if int(e3.get()) < 0 or int(e3.get()) > 100:
        return label0.configure(text="invalid user score(must be within 0 to 100")
    if not e4.get().isdigit():
        return label0.configure(text="invalid matric(digits required)")
    if len(e4.get()) != 9:
        return label0.configure(text="invalid matric(9 digits required)")
    

    for i in data['students']:
        if int(e4.get()) == i['matric']:
            return label0.configure(text="user with matric already in database")

    try:
        data['students'].append({
            'name':e1.get(),
            'surname':e2.get(),
            'score':int(e3.get()),
            'matric':int(e4.get())  
        })
    except ValueError:
        return label0.configure(text="invalid input")
    
    #write user into file
    with open("users.json", "w") as f:
        json.dump(data, f, indent=4)
    
    return label0.configure(text="user saved successfully")

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
        return label0.configure(text="invalid matric input")

    if len(data)==0:
        return label0.configure(text="user with matric not found")
    i=0
    for dict in data['students']:
        if matric == dict['matric']:
            del data['students'][i]
            #rewrite the new data into json file
            with open("users.json", "w") as f:
                json.dump(data, f, indent=4)
            return label0.configure(text="User deleted successfully")
        i+=1
    
    return label0.configure(text="no user found")

#function to display average of the entire scores
label1 = customtkinter.CTkLabel(master, text="")
label1.grid(row=8, column=0, padx=55, sticky=tk.W)
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
    return label1.configure(text=str(round(avg/len(data['students']),2))+"%")

#function to display maximum scoring students 
label2 = customtkinter.CTkLabel(master, text="")
label2.grid(row=8, column=1, padx=85, sticky=tk.W)
def displayMax():
    allvalues = []
    max_students=[]
    with open('users.json', 'r+') as f:
        try:
            data = json.load(f)
            if len(data['students']) == 0:
                return label2.configure(text="no data")
            for i in data['students']:
                allvalues += [i['score']]
            #for i in data['students']:
                #if i['score'] == max(allvalues):
                    #max_students+=list(i.values())        
        except json.JSONDecodeError:
            return label2.configure(text="no data")

    return label2.configure(text=str(max(allvalues))+"%")

#function to display the minimum scoring students
label3 = customtkinter.CTkLabel(master, text="")
label3.grid(row=8, column=2, padx=60, sticky=tk.W)
def displayMin():
    allvalues = []
    min_students=[]
    with open('users.json', 'r+') as f:
        try:
            data = json.load(f)
            if len(data['students']) == 0:
                return label3.configure(text="no data")
            for i in data['students']:
                allvalues += [i['score']]
            #for i in data['students']:
                #if i['score'] == min(allvalues):
                    #min_students+=list(i.values())
        except json.JSONDecodeError:
            return label3.configure(text="no data")

    return label3.configure(text=str(min(allvalues))+"%")

#Best scoring students function
labelx = customtkinter.CTkLabel(master, text="")
labelx.grid(row=10, column=0, padx=10, sticky=tk.N+tk.W)
def displayMaxS():
    allvalues = []
    max_students=[]
    with open('users.json', 'r+') as f:
        try:
            data = json.load(f)
            if len(data['students']) == 0:
                return labelx.configure(text="no data")
            for i in data['students']:
                allvalues += [i['score']]
            for i in data['students']:
                if i['score'] == max(allvalues):
                    max_students+=list(i.values())
                    max_students.append(",")        
        except json.JSONDecodeError:
            return labelx.configure(text="no data")

    return labelx.configure(text=max_students, wraplength=190)
                
#function to display students that scored below 40
label4 = customtkinter.CTkLabel(master, text="")
label4.grid(row=10, column=1, padx=30, pady=5, sticky=tk.N+tk.W)
def displayFailed():
    allvalues = []
    with open('users.json', 'r+') as f:
        try:
            data = json.load(f)
            if len(data['students']) == 0:
                return label4.configure(text="no data")
            for i in data['students']:
                if i['score'] < 40:
                    allvalues+=list(i.values())
                    allvalues.append(",")
            if len(allvalues)==0:
                return label4.configure(text="no data")
        except json.JSONDecodeError:
            return label4.configure(text="no data")

    return label4.configure(text=allvalues, wraplength=190)

#function to display students who scored above 69
label5 = customtkinter.CTkLabel(master, text="")
label5.grid(row=10, column=2, pady=5, sticky=tk.W)
def displayTop():
    allvalues = []
    with open('users.json', 'r+') as f:
        try:
            data = json.load(f)
            if len(data['students']) == 0:
                return label5.configure(text="no data")
            for i in data['students']:
                if i['score'] > 69:
                    allvalues+=list(i.values())
                    allvalues.append(",")
            if len(allvalues) == 0:
                return label5.configure(text="no data")
        except json.JSONDecodeError:
            return label5.configure(text="no data")

    return label5.configure(text=allvalues, wraplength=190, anchor="w")

    
# label to enter name
customtkinter.CTkLabel(master, text="First Name:").grid(row=0, column=0)
 
# label to enter surname
customtkinter.CTkLabel(master, text="Surname:").grid(row=0, column=1)
 
# label for Matric number
customtkinter.CTkLabel(master, text="Matric Number:").grid(row=2, column=1)
 
# label for score
customtkinter.CTkLabel(master, text="Score:").grid(row=2, column=0)
 
# taking entries of name, matric number and score respectively
e1=customtkinter.CTkEntry(master, width=180)
e2=customtkinter.CTkEntry(master, width=180)
e3=customtkinter.CTkEntry(master, width=180)
e4=customtkinter.CTkEntry(master, width=180)
  
# organizing them in the grid
e1.grid(row=1, column=0)
e2.grid(row=1, column=1, padx=50, sticky=tk.W)
e3.grid(row=3, column=0)
e4.grid(row=3, column=1, padx=50, sticky=tk.W)
  
# button to save new students in json file
button1=customtkinter.CTkButton(master, text="Save", command=savejson)
button1.grid(row=4, column=0)

#button to delete user
button1=customtkinter.CTkButton(master, text="Delete", command=deleteUser)
button1.grid(row=4, column=1, padx=70, sticky=tk.W)

customtkinter.CTkLabel(master, text="Generate the following in one click.").grid(row=6, column=0, padx=10, pady=25)
  
# button to display the average score
button2=customtkinter.CTkButton(master, text="Mean Score", command=displayAvg)
button2.grid(row=7, column=0, padx=10, pady=5, sticky=tk.N+tk.W)

# button to display max score
button3=customtkinter.CTkButton(master, text="Max score", command=displayMax)
button3.grid(row=7, column=1, padx=30, pady=5, sticky=tk.N+tk.W)

# button to display minimum score
button3=customtkinter.CTkButton(master, text="Minimum score", command=displayMin)
button3.grid(row=7, column=2, pady=5, sticky=tk.W)

# button to display best scoring students
button3=customtkinter.CTkButton(master, text="Best Student(s)", command=displayMaxS)
button3.grid(row=9, column=0, padx=10, pady=5, sticky=tk.N+tk.W)

# button to display failed students
button3=customtkinter.CTkButton(master, text="Student(s) below 40", command=displayFailed)
button3.grid(row=9, column=1, padx=30, pady=5, sticky=tk.N+tk.W)

# button to display students 70 and above
button3=customtkinter.CTkButton(master, text="Student(s) above 69", command=displayTop)
button3.grid(row=9, column=2, pady=5, sticky=tk.W)
  
if __name__ == "__main__":    
    master.mainloop()
  
  
