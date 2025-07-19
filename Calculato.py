from tkinter import *
root = Tk()

#creating main window
root.geometry("260x400")
root.title("Calculator")
root.iconbitmap("icon.webp")

# logic for arithmetic opeations in caculator by event handing
def on_click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if(text == "="):
            if scvalue.get().isdigit():
                value = int(scvalue.get())
            else:
                try:
                    value = eval(screen.get())
                except Exception as e:
                   print("You click buttons in wrong format")
                   value = "Error"

            scvalue.set(value)
            screen.update()

    elif(text == "C"):
       scvalue.set("")
       screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

# Making a screen of the calculator
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font = "lucida 30 bold")
screen.pack(fill=X, ipadx=8, padx=10, pady=10)

# Creating Buttons
f1 =Frame(root)
b = Button(f1, text="9", padx=12, pady=12,font = "lucidia 18 bold", )
b.pack(side=LEFT, padx=5, pady=4)
b.bind("<Button-1>",on_click)
b = Button(f1, text="8", padx=12, pady=12,font = "lucidia 18 bold")
b.pack(side=LEFT, padx=5, pady=4)
b.bind("<Button-1>",on_click)
b = Button(f1, text="7", padx=12, pady=12,font = "lucidia 18 bold")
b.pack(side=LEFT, padx=5, pady=4)
b.bind("<Button-1>",on_click)
b = Button(f1, text="/", padx=12, pady=12,font = "lucidia 18 bold")
b.pack(side=LEFT, padx=5, pady=4)
b.bind("<Button-1>",on_click)

f1.pack()

f1 =Frame(root)
b = Button(f1, text="6", padx=12, pady=12,font = "lucidia 18 bold", )
b.pack(side=LEFT, padx=5, pady=4)
b.bind("<Button-1>",on_click)
b = Button(f1, text="5", padx=12, pady=12,font = "lucidia 18 bold")
b.pack(side=LEFT, padx=5, pady=4)
b.bind("<Button-1>",on_click)
b = Button(f1, text="4", padx=12, pady=12,font = "lucidia 18 bold")
b.pack(side=LEFT, padx=5, pady=4)
b.bind("<Button-1>",on_click)
b = Button(f1, text="*", padx=12, pady=12,font = "lucidia 18 bold")
b.pack(side=LEFT, padx=5, pady=4)
b.bind("<Button-1>",on_click)

f1.pack()

f1 =Frame(root)
b = Button(f1, text="3", padx=12, pady=12,font = "lucidia 18 bold", )
b.pack(side=LEFT, padx=5, pady=4)
b.bind("<Button-1>",on_click)
b = Button(f1, text="2", padx=12, pady=12,font = "lucidia 18 bold")
b.pack(side=LEFT, padx=5, pady=4)
b.bind("<Button-1>",on_click)
b = Button(f1, text="1", padx=12, pady=12,font = "lucidia 18 bold")
b.pack(side=LEFT, padx=5, pady=4)
b.bind("<Button-1>",on_click)
b = Button(f1, text="-", padx=12, pady=12,font = "lucidia 18 bold")
b.pack(side=LEFT, padx=5, pady=4)
b.bind("<Button-1>",on_click)

f1.pack()

f1 =Frame(root)
b = Button(f1, text="C", padx=12, pady=12,font = "lucidia 18 bold", )
b.pack(side=LEFT, padx=5, pady=4)
b.bind("<Button-1>",on_click)
b = Button(f1, text="0", padx=12, pady=12,font = "lucidia 18 bold")
b.pack(side=LEFT, padx=5, pady=4)
b.bind("<Button-1>",on_click)
b = Button(f1, text="=", padx=12, pady=12,font = "lucidia 18 bold")
b.pack(side=LEFT, padx=5, pady=4)
b.bind("<Button-1>",on_click)
b = Button(f1, text="+", padx=12, pady=12,font = "lucidia 18 bold")
b.pack(side=LEFT, padx=5, pady=4)
b.bind("<Button-1>",on_click)

f1.pack()

root.mainloop()