import tkinter as tk

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

label = tk.Label(root, text = "NONE")
label.pack()

def get_entry_text():
    x1 = entry.get()
    if x1 == "" or x1 == " ":
        x1 = "NONE STILL"
    #print(entry.get())
    label.config(text = entry.get())

button = tk.Button(root, text = "CLICK ME",
                  command = lambda: get_entry_text())

button.pack()

def click_here():
    a = entry.getvar()
    print(a)
