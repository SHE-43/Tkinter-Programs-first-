import tkinter as tk

def toggle_on_off():
    toggle.set(not toggle.get()) #
    
    if toggle.get():
        watch()

def watch():
    count_seconds.set(count_seconds.get() + 1)
    if toggle.get():
        _callback_id.set(root.after(1000, watch))
    else:
        root.after_cancel(_callback_id.get())
        
root = tk.Tk()
root.configure(background='black')
root.geometry('650x620+250+50')

count_seconds = tk.IntVar(root)
count_seconds.set(0)
toggle = tk.BooleanVar(root)
toggle.set(False)

tk.Button(root,text="Start",command=toggle_on_off, height = 1, width = 10, bg = "black", fg = "dark red", font = ('bold', 40)).pack(padx = 10, pady = 10)
tk.Button(root,text="Exit",command=root.destroy, height = 1, width = 10, bg = "black", fg = "dark red" ,font = ('bold', 40)).pack(padx = 15, pady = 15)
tk.Button(root,text="Travel Ahead in Time",command=root.destroy, height = 1, width = 20, bg = "black", fg = "dark red" ,font = ('bold', 40)).pack(padx = 15, pady = 15)
tk.Button(root,text="Travel Back in Time",command=root.destroy, height = 1, width = 20, bg = "black", fg = "dark red" ,font = ('bold', 40)).pack(padx = 15, pady = 15)
label = tk.Label(root, font = ('bold', 43), bg = "black", fg = "orange", textvariable=count_seconds).pack(padx = 1, pady = 1)

_callback_id = tk.StringVar(root)
_callback_id.set(None)

root.mainloop()






