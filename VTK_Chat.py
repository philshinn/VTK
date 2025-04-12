from tkinter import *

window = Tk()

messages = Text(window)
messages.pack()

input_user = StringVar()
input_field = Entry(window, text=input_user)
input_field.pack(side=BOTTOM, fill=X)

def EnterPressed(event):
    inputText = input_field.get()
    print(inputText)
    messages.insert(INSERT, '<%s\n' % inputText)
    # label = Label(window, text=input_get)
    input_user.set('')
    # label.pack()
    response = GetResponse(inputText)
    messages.insert(INSERT, '>%s\n' % response)
    return "break"

def GetResponse(inputText):
    return 'hello'


frame = Frame(window)  # , width=300, height=300)
input_field.bind("<Return>", EnterPressed)
frame.pack()

window.mainloop()