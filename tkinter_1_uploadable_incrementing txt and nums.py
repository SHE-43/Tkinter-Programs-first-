import tkinter as tk
import itertools

# Works fine however we need to find a way to cancel the other function once 2 are
#       are running at the same time.


root = tk.Tk();
root.geometry('500x450+420+200');
root.title("FRAME!");

frame_1 = tk.Frame(root, bg='light grey', height = '300', width = '500')
frame_1.pack()

label_1 = tk.Label(frame_1, text = "Press Below", fg = 'blue', bg = 'grey', width = '43')
label_1.pack(padx = 5, pady = 5)

list_1 = [chr(x) for x in range(ord('A'), ord('z')+1)]
list_1_cycle = itertools.cycle(list_1)

list_2 = [x.__str__() for x in range(1,101)]
list_2_cycle = itertools.cycle(list_2)



def changer():
    def con(L):
        L.config(text = list_1_cycle.__next__(), width = '43')
    return con(label_1)

def changer_2():
    def con_1(L):
        L.config(text = list_2_cycle.__next__(), width = '43')
    return con_1(label_1)

counter = 0

def changer_3():
    counter = 0
    def con_2():
        global counter;
        counter += 1;
        label_1.config(text = str(counter), width = '43')        
        label_1.after(500, con_2)
    return con_2()

list_4 = [chr(x) for x in range(ord('A'), ord('A') + 26)]
cycle_4 = itertools.cycle(list_4)

def changer_4():
    def con_3():
        
        label_1.config(text = str(cycle_4.__next__()), width = '43')
        label_1.after(500, con_3)
    return con_3()




button_1 = tk.Button(frame_1, text = "Incrementing Alphabets", bg= 'black', fg = 'white', command = changer, width = '43')
button_1.pack(padx = 5, pady = 5)

button_2 = tk.Button(frame_1, text = "Counting Incrementing Numbers", bg= 'black', fg = 'white', command = changer_2, width = '43')
button_2.pack(padx = 5, pady = 5)

button_3 = tk.Button(frame_1, text = "Counter / Numbers", bg= 'black', fg = 'white',  width = '43' , command = changer_3)
button_3.pack(padx = 5, pady = 5)

button_4 = tk.Button(frame_1, text = "Counter / Letters", bg= 'black', fg = 'white',  width = '43' , command = changer_4)
button_4.pack()

button_5 = tk.Button(frame_1, text = "Exit", bg= 'black', fg = 'white',  width = '43' , command = root.destroy)
button_5.pack(padx = 5, pady = 5)

root.mainloop();










