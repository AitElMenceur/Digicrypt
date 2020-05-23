import tkinter
import tkinter.ttk
import time
import os
import shutil
from tkinter import filedialog
import ntpath
from tkinter import messagebox
    
    

# create the root GUI window
root_window = tkinter.Tk()

# define window size
window_width = 2000       #A MODIFIER                
window_height = 1000          #A MODIFIER 

# background i
path = os.getcwd()
filename = tkinter.PhotoImage(file = path+"\\code\\GUI\\background.png") #A MODIFIER 
backgroundLabel = tkinter.Label(root_window, image=filename)
backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)

# create frames 

fileFrame=tkinter.ttk.Frame(root_window, width=window_width, height=window_height)
fileFrame['borderwidth'] = 2
fileFrame['relief'] = 'sunken'
fileFrame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

imagePath = tkinter.PhotoImage(file = path+"\\code\\GUI\\random.png")   #A MODIFIER
imageLabel = tkinter.Label(fileFrame, image=imagePath)
imageLabel.grid(column=1, row= 1, pady=10, padx=10, sticky=(tkinter.N))

# Start tkinter event - loop
root_window.mainloop()
