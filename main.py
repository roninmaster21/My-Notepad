import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
import time
import threading
import pyperclip

programName = "My Notepad"

path = None

def error(errormsg):
    messagebox.showerror(title="Error",message=errormsg)

def new_command():
    global path
    path = None
    textArea.delete(1.0, tk.END)

def open_command():
    global path
    try:
        path = fd.askopenfilename(defaultextension=".txt",
                                  filetypes=[("Text file", ".txt"),
                                             ("All file types", ".*")])
        readText = ""
        with open(path, "r") as cfile:
            readText = cfile.read()
            textArea.delete(1.0, tk.END)
            textArea.insert(tk.END, readText)
            print("Opened file")
    except Exception as e:
        error("An error occurred in opening the file :(")
        print("Error: "+str(e))

def save_command():
    if path:
        try:
            with open(path, "w") as cfile:
                cfile.write(textArea.get(1.0, tk.END))
                print("Saved file")
        except Exception as e:
            error("An error occurred in saving the file :(")
            print("Error: "+str(e))
    else:
        error("You do not currently have a file open!")

def saveas_command():
    try:
        global path
        path = fd.asksaveasfilename(defaultextension=".txt",
                              filetypes=[("Text file", ".txt"),
                                         ("All file types", ".*")],confirmoverwrite=False)
        with open(path, "w") as cfile:
            cfile.write(textArea.get(1.0, tk.END))
            print("Saved as new file")
    except Exception as e:
        error("An error occurred in saving the file :(")
        print("Error: "+str(e))

def copy_command():
    try:
        pyperclip.copy(textArea.get(1.0, tk.END))
        print("Copied text")
    except Exception as e:
        error("An error occurred in copying the file :(")
        print("Error: "+str(e))

window = tk.Tk()
window.title(programName)
window.resizable(width=False, height=False)

menubar = tk.Menu(window)
window.config(menu=menubar)

menubar.add_command(label="New",command=new_command)
menubar.add_command(label="Open",command=open_command)
menubar.add_command(label="Save",command=save_command)
menubar.add_command(label="Save As",command=saveas_command)
menubar.add_command(label="Copy Text",command=copy_command)

textArea = tk.Text(font=("Courier", 12))
textArea.pack()

window.mainloop()
