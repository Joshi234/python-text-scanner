import tkinter as tk
setting=0
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.create_widgets()
        self.master.title("Text Analyzer                                                                    made by Joshi234                                                                                       Version:0.1.1")
    def create_widgets(self):
        global inputt
        inputt="Test"
        inputt=tk.StringVar()
        label=tk.Label(self.master,text="Gib einen Text ein um die wörter zu zählen")
        label.pack()
        self.settings= tk.Button(self.master,text="Print all words alone",width=100,command=lambda: settings())
        self.settings.pack()
        self.button= tk.Button(self.master,text="Analyze",width=100,command=lambda: actioon())
        
        self.quit = tk.Entry(self.master,width=200,textvariable=inputt)
   
        self.quit.pack(side="bottom")
        self.button.pack()
        label.focus_set()
    def say_hi(self):
        print("hi there, everyone!")
def settings():
    global setting
    if setting==0:
        setting=1
        print("Now printing all input alone")
    else:
        setting=0
        print("Nothing is printing now")
def actioon():
    global setting
    outputwort=""
    master=tk.Tk()
    master.title("Result")
    text=inputt.get()
    wort=""
    alreadywort=False
    woerter=1
    message="\nWörter gefunden"

    anzahl = len(text)
    if text=="":
        print("Please Enter a text")
        anzahl=-2
    while anzahl >= 0:

        anzahl=anzahl-1
        wort=text[anzahl]+wort
        if text[anzahl]== " ":

            woerter=woerter+ 1

            if setting==1:
                print(wort)
                outputwort=outputwort+"\n"+wort
                wort=""

        if text=="  ":
            woerter=0
        if text[anzahl]==" ":
            if text[anzahl-1]==" ":
                woerter=woerter-1
    if anzahl>-2:

        print(woerter)
    if text[0]==" ":
        woerter=woerter-1
    if text == "":
        woerter = 0
    if woerter==1:
        message=" \nWort gefunden"
    label=tk.Label(master,text=str(woerter)+message)
    output=tk.Label(master,text=outputwort)
    output.pack()
    label.pack()
root = tk.Tk()
app = Application(master=root)
app.mainloop()

