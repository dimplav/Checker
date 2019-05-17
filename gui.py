from tkinter import *
from functions import*

root = Tk()
root.title("--Checker--")
root.geometry("500x150")
root.resizable(0, 0)

theMainLabel = Label(root, text="Insert web page that you want to be checked")
theMainLabel.pack()

check_button = Button(root, text="Check for changes...", command=lambda: [ispisi()])
label = Label(root, text="Web page has some changes")
label1 = Label(root, text="Web page has no changes")
disconnect_button = Button(root, width=10, text="Stop", command=lambda:[nit1(), enable_button()])
#exit_button = Button(root, width=10, text="Exit", command=sys.exit)
inputs = Entry(root, width=80)
inputs.pack()
check_button.pack()
#exit_button.pack(side=RIGHT)
disconnect_button.pack(side=LEFT)

def enable_button():
    check_button['state'] = 'normal'

def disable_button():
    check_button['state'] = 'disabled'

def ispisi():
    disable_button()
    if inputs.get() == '' or inputs.get() == "Please insert URL":
        inputs.delete(0, END)
        inputs.insert(0, "Please insert URL")
        enable_button()
    else:
        connection.web_mta = inputs.get()
        nit()
        print(connection.web_mta)

var = IntVar()
linkCheck = Radiobutton(root, text="Link",variable=var, value=1, command=links)
linkCheck.pack(anchor=W)
imageCheck = Radiobutton(root, text="Image",variable=var, value=2, command=images)
imageCheck.pack(anchor=W)


root.mainloop()
