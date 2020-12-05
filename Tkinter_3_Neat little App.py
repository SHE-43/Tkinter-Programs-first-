# Instead of overusing that method, use a class please.
# That'll give you more grip on OOP.
# This should be next on list for Tkinter and OOP.

import tkinter as tk

master = tk.Tk()
master.geometry("300x300+400+150")
master.configure(background = "dark blue")
master.title("Various Math Sequences")

counter = 0
def open_new_window_1():
    def fibo(x):
        cache = {0:0, 1:0, 2:1,3:1}
        def fibo1(x):
            if x in cache:
                return cache[x]
            else:
                value = fibo1(x-1)+ fibo1(x-2)
                cache[x] = value
            return cache[x]
        return fibo1(x)
        
    newWindow = tk.Tk()
    newWindow.title("New Window")
    newWindow.geometry("400x400+350+200")
    newWindow.configure(background = "dark blue")
    tk.Label(newWindow,
             text = "This is a new window",
             fg = "yellow",
             bg = "blue",
             font = ("bold", 14)).pack()
    entry = tk.Entry(newWindow, fg = "yellow", highlightcolor = "red", # highlightthickness
                   bg = "blue")
    entry.tk_bisque()
    entry.pack()
    label_answer = tk.Label(newWindow,
                            fg = "Yellow",
                            bg = "blue",
                            text = "#",
                            font = ("bold", 14))
    label_answer.pack()

    def record_method(L = 0):
        x11 = entry.get()
        if x11 == "":
            x11 = 0
        else:
            x11 = eval(x11)
            x11 = int(x11)
        x12 = fibo(x11)
        L.config(text = x12)
        
    counter = 0
    
    def timer_style():
        def method():
            global counter
            counter += 1
            x43 = fibo(counter)
            label_answer.config(text = str(x43))
            label_answer.after(1000, method)
        return method()        
    
    btn_2 = tk.Button(newWindow,
                      text = "Record",
                      fg = "yellow",
                      bg = "blue",
                      height = 2,
                      width = 10,
                      command =
                      lambda:record_method(label_answer)).pack()

    btn_3 = tk.Button(newWindow,
                      text = "Timer Style",
                      fg = "yellow",
                      bg = "blue",
                      height = 2,
                      width = 10,
                      command = timer_style).pack()

    btn_4 = tk.Button(newWindow,
                      text = "Exit Window",
                      fg = "yellow",
                      bg = "blue",
                      height = 2,
                      width = 10,
                      command = newWindow.destroy).pack()

    def exit_all():
        minor = lambda: newWindow.destroy()
        major = lambda: master.destroy()
        return (minor(), major())

    btn_5 = tk.Button(newWindow,
                      text = "Exit All",
                      fg = "yellow",
                      bg = "blue",
                      height = 2,
                      width = 10,
                      command = exit_all).pack()

"""XXX-XXX-XXX-XXX-XXX-XXX-XXX-XXX-XXX-XXX-XXX-XXX-XXX-XXX-XXX-XXX-XXX-XXX"""
    
label = tk.Label(master,
                 text = "A neat little app",
                 fg = "yellow",
                 bg = "blue")
label.grid(row = 9, column = 2)

button = tk.Button(master,
                   text = "Fibonacci Window",
                   fg = "yellow",
                   bg = "blue",
                   command = open_new_window_1)
button.grid(row = 7, column = 2)        


