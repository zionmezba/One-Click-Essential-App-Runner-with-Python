import tkinter as tk
from tkinter import filedialog,Text
import os

root = tk.Tk(screenName="App runner",baseName="App Runner")
root.title("App Runner")
apps = []
lbls = []

def appName(fname):
    fname = fname.split('/')
    x = len(fname)
    fname = fname[x-1].split('.')
    return fname[0].upper()

def addApps():
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\User\\Desktop", title="Select File",
    filetypes=(("Executables","*.exe"),("all files","*.*")))
    if filename:
        for widget in frame.winfo_children():
            widget.destroy()
        apps.append(filename)
        x = appName(filename)
        lbls.append(x.strip())

        for app in lbls:
            label = tk.Label(frame,text = app, bg="blue",font = ("Arial", 20))
            label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

def delApps():
    for widget in frame.winfo_children():
        widget.destroy()
    apps.clear()
    open('save.sv','w').close()

canvas = tk.Canvas(root, height=300, width=400, bg ="#020202")
canvas.place(relheight=1,relwidth=1,relx=0.01,rely=0.01)
canvas.pack()

frame = tk.Frame(root, bg = "#020202")
frame.place(relheight=.88,relwidth=1,relx=0.01,rely=0.01)

if os.path.isfile('save.sv'):
    with open('save.sv','r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
        for app in apps:
            label = tk.Label(frame,text = app, bg="blue",font = ("Arial", 20))
            label.pack()

openfile = tk.Button(root,text="Open File", padx=200,pady=5,fg="white",bg="#00008b", command=addApps)
openfile.pack()

runApp = tk.Button(root, command = runApps, text="Run Apps", padx=200,pady=5,fg="white",bg="green")
runApp.pack()

delAp = tk.Button(root,text="Delete Files",padx=200,pady=5,command=delApps,fg="white",bg="red")
delAp.pack()

for app in lbls:
    label = tk.Label(frame,text = app)
    label.pack

root.mainloop()
with open('save.sv','w') as f:
    for app in lbls:
        f.write(app+',')