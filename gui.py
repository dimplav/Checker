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
disconnect_button = Button(root, width=10, text="Stop", command=nit1)
#exit_button = Button(root, width=10, text="Exit", command=sys.exit)
inputs = Entry(root, width=80)
inputs.pack()
check_button.pack()
#exit_button.pack(side=RIGHT)
disconnect_button.pack(side=LEFT)

def ispisi():
    check_button['state'] = 'disabled'
    if inputs.get() == '' or inputs.get() == "Please insert URL":
        inputs.delete(0, END)
        inputs.insert(0, "Please insert URL")
        check_button['state'] = 'normal'
    else:
        connection.web_mta = inputs.get()
        nit()
        print(connection.web_mta)

root.mainloop()
