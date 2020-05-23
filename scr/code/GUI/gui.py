import tkinter
import tkinter.ttk
import time
import os
import shutil
from tkinter import filedialog
import ntpath
from tkinter import messagebox
from util import capteur as cpt
import time

#create global variable
user = ""
cypherChoice = "Vernam"
path = os.getcwd()
workingDirectoryPath = path+ "\\code\\GUI\\cipheredFiles"



def get_entry(event):
    global user
    user = userLoginWindowLabelUsername.get()

def get_choice(*args):
    global cypherChoice
    cypherChoice = variable.get()
    print(cypherChoice)

def createUserLoginWindow():
    # Create the label for the frame
    userLoginWindowLabelText = tkinter.ttk.Label(userFrame, text='User Identification')
    userLoginWindowLabelText.grid(column=1, row=0, padx=5, pady=5, sticky=(tkinter.N))
    userLoginWindowLabelUser = tkinter.ttk.Label(userFrame, text='Username: ')
    userLoginWindowLabelUser.grid(column=0, row=1, padx=5, pady=5, sticky=(tkinter.N))
    userLoginWindowLabelUsername.grid(column=1, row=1, padx=5, pady=5, sticky=(tkinter.N))
    userLoginWindowLabelDescription = tkinter.ttk.Label(userFrame, text='Fill in you username and scan your finger')
    userLoginWindowLabelDescription.grid(column=1, row=2, padx=5, pady=5, sticky=(tkinter.N))

    root_window.bind('<ButtonPress>', get_entry)

    # Create the button for the frame
    userLoginWindowLabelDoneButton = tkinter.Button(userFrame, text = "Done", command = callDigicryptWindow) #A MODIFIER: VERIFIER DANS LA DATABASE USERNAME + EMPREINTE
    userLoginWindowLabelDoneButton.grid(column=2, row=3, pady=10, padx=10, sticky=(tkinter.N))
    userLoginWindowLabelQuitButton = tkinter.Button(userFrame, text = "Quit", command = quitProgram)
    userLoginWindowLabelQuitButton.grid(column=0, row=3, pady=10, padx=10, sticky=(tkinter.N))


def createDigicryptWindow():
    # Create the label for the frame
    fileWindowLabel = tkinter.ttk.Label(fileFrame, text='Files')
    fileWindowLabel.grid(column=1, row=0, pady=10, padx=10, sticky=(tkinter.N))

    # Create the button for the frame
    fileWindowAddFileButton = tkinter.Button(fileFrame, text = "Add File", command = callCypherWindow)
    fileWindowAddFileButton.grid(column=2, row=3, pady=10, sticky=(tkinter.N))
    fileWindowAddQuitButton = tkinter.Button(fileFrame, text = "Quit", command = quitProgram)
    fileWindowAddQuitButton.grid(column=0, row=3, pady=10, sticky=(tkinter.N))
    fileWindowAddBackButton = tkinter.Button(fileFrame, text = "Back", command = callUserLoginWindow)
    fileWindowAddBackButton.grid(column=1, row=3, pady=10, sticky=(tkinter.N))

    # Load the files
    loadFiles()


def createCypherWindow():
    # Create the label for the frame
    cypherWindowLabel = tkinter.ttk.Label(cypherFrame, text='Choose a cypher for your file')
    cypherWindowLabel.grid(column=0, row=0, pady=10, padx=10, sticky=(tkinter.N))

    # Create the list for the frame
    cypherList.grid(column=0, row=1, pady=10, sticky=(tkinter.N))
    cypherWindowDoneButton = tkinter.Button(cypherFrame, text = "Done", command = getFile)
    cypherWindowDoneButton.grid(column=1, row=1, pady=10, sticky=(tkinter.N))

    variable.trace('w', get_choice)

def openfile():
    currentFile = workingDirectoryPath + "\\testFile.txt"
    print(currentFile)
    return filedialog.askopenfilename(initialdir = currentFile)

def on_click(event=None):
    openfile()

def loadFiles():
    i = 0
    with open(path+'\\code\\GUI\\'+'files.txt', 'r') as f:
        for line in f:
            stringTitle = line.split( " ")
            titleString = stringTitle[0]
            imageLabel = tkinter.Label(fileFrame, image=imagePath)
            imageLabel.grid(column=i, row = 1, pady=10, padx=10, sticky=(tkinter.N))
            title = tkinter.ttk.Label(fileFrame, text=titleString)
            title.grid (column = i, row = 2, padx=10, pady=10, sticky=(tkinter.N))
            imageLabel.bind('<Button-1>', on_click)
            buttonImage = tkinter.Button(fileFrame, image=imagePath, command=on_click)
            buttonImage.grid(column=i, row = 1, pady=10, padx=10, sticky=(tkinter.N))

            i = i + 1
    

   


def callUserLoginWindow():
    fileFrame.grid_forget()
    cypherFrame.grid_forget()
    userFrame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

def callDigicryptWindow():
    Enregistrer()
    userFrame.grid_forget()
    cypherFrame.grid_forget()
    fileFrame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

def callCypherWindow():
    fileFrame.grid_forget()
    userFrame.grid_forget()
    cypherFrame.grid(column=1, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

def quitProgram():
    root_window.destroy()


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def registerFile(nameFile):
    with open('files.txt', 'a') as f:
        fileInfo = nameFile + ' ' + user + ' ' + cypherChoice + '\n'
        f.write(fileInfo)


def cypher(fiName):
    #TO DO
    #switch on cypherChoices and use cypher algorithms on file with name fiName
    fiNale = ""

def moveFile(fpath, fname):
    shutil.copy(fpath, workingDirectoryPath)
    registerFile(fname)
    cypher(fname)


def getFile():
    root_window.filepath = filedialog.askopenfilename(initialdir = "C:\\Users\\Karen_DELL_13\\Desktop",title = "Select file", filetypes = (("all files", "*.*"), ("text files", "*.txt"))) #A MODIFIER
    filename = path_leaf (root_window.filepath)
    moveFile(root_window.filepath, filename)
    loadFiles()
    callDigicryptWindow()

f=0
def Enregistrer():
    messagebox.showinfo("Title", "Appuyez sur OK et placez votre doigt sur le capteur")
    cpt.Enregistrer_ch1(f)
    messagebox.showinfo("Title", "Appuyez sur OK et retirez votre doigt")
    messagebox.showinfo("Title", "Appuyez sur OK et placez votre doigt sur le capteur")
    cpt.Enregistrer_ch2(f)
    messagebox.showinfo("Title", cpt.Enregistrer_empreinte(f))
    
    




################################
############# MAIN #############
################################
root_window = tkinter.Tk()

    # define window size
window_width = 1500          #A MODIFIER                
window_height = 900          #A MODIFIER 

# title and size
root_window.title("Digicrypt")
root_window.geometry("1200x600")     #A MODIFIER 

# background i
filename = tkinter.PhotoImage(file = path +"\\code\\GUI\\background.png") #A MODIFIER 
backgroundLabel = tkinter.Label(root_window, image=filename)
backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)

# create image for files
imagePath = tkinter.PhotoImage(file = path+"\\code\\GUI\\fileIcon.png")

# create frames 

userFrame=tkinter.ttk.Frame(root_window, width=window_width, height=window_height)
userFrame['borderwidth'] = 2
userFrame['relief'] = 'sunken'
userFrame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

fileFrame=tkinter.ttk.Frame(root_window, width=window_width, height=window_height)
fileFrame['borderwidth'] = 2
fileFrame['relief'] = 'sunken'
fileFrame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

cypherFrame=tkinter.ttk.Frame(root_window, width=window_width, height=window_height)
cypherFrame['borderwidth'] = 2
cypherFrame['relief'] = 'sunken'
cypherFrame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

# create User Entry in the second window
userLoginWindowLabelUsername = tkinter.ttk.Entry(userFrame)

# create cypher list in the third window
choices = ['Vernam', 'AES', 'RSA', '3DES']
variable = tkinter.StringVar(cypherFrame)
variable.set('Vernam')
cypherList = tkinter.OptionMenu(cypherFrame, variable, *choices)

# create widgets
createCypherWindow()
createDigicryptWindow()
createUserLoginWindow()

# hide frames
cypherFrame.grid_forget()
fileFrame.grid_forget()
userFrame.grid_forget()

#user window apears after 2 second
root_window.after(2000, callUserLoginWindow)

    
# create the root GUI window
def Build():
    f=cpt.Startup()
    # Start tkinter event - loop
    root_window.mainloop()
