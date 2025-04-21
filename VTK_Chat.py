import tkinter as tk
from tkinter import scrolledtext
from VTK_Code import *

    
def outputText(text,text_area):
    text_area.insert(tk.END, text + "\n")
    text_area.see(tk.END)  # Scroll to the bottom
    
def respond(inputText):
    return "You said:" + inputText

# Function to add entry text to text area
def getInputText(entry,text_area):
    inputText = entry.get()
    if inputText.strip():
        text_area.insert(tk.END, "< " + inputText + "\n","blue_text")
        text_area.see(tk.END)  # Scroll to the bottom
        response = respond(inputText)
        text_area.insert(tk.END, "> " + response + "\n")
        entry.delete(0, tk.END)

def quit(root):
    root.quit

def setupChatWindow():
    # Create the main window
    root = tk.Tk()
    root.title("VTK Chat")
    root.geometry("400x350")
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=12, font=("Arial", 12))

    # Create a ScrolledText widget
    text_area.pack(padx=10, pady=(10, 5), fill=tk.BOTH, expand=True)

    # Frame to hold the entry and button
    input_frame = tk.Frame(root)
    input_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

    # Entry widget for user input
    entry = tk.Entry(input_frame, font=("Arial", 12))
    entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

    text_area.tag_configure("red_text",foreground="red")
    text_area.tag_configure("blue_text",foreground="blue")
    # Button to trigger adding text
    add_button = tk.Button(input_frame, text="Quit", command=root.destroy)
    add_button.pack(side=tk.RIGHT)

    # Allow pressing Enter to add text too
    entry.bind("<Return>", lambda event: getInputText(entry,text_area))

    initialPrompt = "> Hello"
    outputText(initialPrompt,text_area)

    # Start the main event loop
    root.mainloop()


if __name__ == "__main__":
    #pass
    setupChatWindow()
    inputFileName = 'WAG.06.xml'
    startStateName = 'Start'
    nsm = NewStateMachine(inputFileName)
    nsm.stateMachine.run(startStateName)
    setupChatWindow()
