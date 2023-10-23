from gtts import gTTS
import os
from tkinter import *

root = Tk()
canvas = Canvas(root, width=499, height=300)
canvas.pack()

# Create an Entry widget for user input
entry = Entry(root)
canvas.create_window(200, 180, window=entry)

def text_to_speech():
    # Get the text from the Entry widget
    text = entry.get()
    if text:
        # Create a gTTS object with the entered text
        output = gTTS(text=text, lang="en", slow=False)
        
        # Save the generated speech to an mp3 file
        output.save("output.mp3")
        
        # Play the generated speech
        os.system("start output.mp3")

# Create a button to trigger text-to-speech conversion
button = Button(root, text="Start", command=text_to_speech)
canvas.create_window(200, 230, window=button)

root.mainloop()
