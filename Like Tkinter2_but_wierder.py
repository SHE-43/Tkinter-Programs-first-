import tkinter as tk


root = tk.Tk()

class Fibo:

    def __init__(self, root):
        self.x = "HAMZA"
        self.root = root
        self.root.title("OOP TKINTER")
        self.root.geometry("300x300+750+150")
        self.label = tk.Label(self.root, text = "Label 1")
        self.label.place(x = 120, y=60)
        self.label_2 = tk.Label(self.root, text = "Label 2")
        self.label_2.place(x = 120, y=60+25)

        self.entry_1 = tk.Entry(self.root,
                                bg = "orange",
                                fg = "yellow")
        
        self.entry_1.place(x=120,y=25)
                              
        button_1 = tk.Button(self.root, text = "Button 1",
                          bg = "RED",
                          fg = "YELLOW",
                          command = self.printer)
        button_1.place(x = 120, y=60+25+25)

        button_2 = tk.Button(self.root, text = "Button 2",
                          bg = "RED",
                          fg = "YELLOW",
                          command = self.printer2)
        button_2.place(x =120, y=60+25+25+25)

        # Exit button
        button_exit = tk.Button(self.root,
                             text = "Exit",
                             command = self.root.destroy)
        button_exit.place(x=120, y = 60+25+25+25+45);
        
        
        # We have finished it with the exit button.
        # This means that it is complete.
        
        #Extract entry box
        def entry_txt():
            x1 = self.entry_1.get()
            if x1 == "":
                x1 = "NONE ENTERED"
            self.label_2.config(text = x1)

        # Button for using entry box to say anything you want.
        button_4 = tk.Button(self.root,
                             text = "Extra",
                             command = entry_txt)
        button_4.place(x=120, y = 60+25+25+25+45+25)

    # Method for labelling Hello via Button 1
    def printer(self):
        a = "Hello"; self.label.config(text = a)

    # Method for labelling Bye via Button 2
    def printer2(self):
        a = "Bye"; self.label_2.config(text = a)
        
a = Fibo(root)
root.mainloop();









