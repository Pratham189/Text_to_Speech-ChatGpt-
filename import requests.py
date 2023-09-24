import pyttsx3
import openai
import tkinter as tk
from tkinter import scrolledtext


# Set up your OpenAI API key
openai.api_key = "Enter Your API_KEY"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def send_gui():
    user_input = user_input_entry.get()
    user_input_entry.delete(0,tk.END) 

    if user_input.lower() == "Exit":
        root.destroy()
    
    else:
        response = generate_response(user_input)
        conversation_text.insert(tk.END,"Enter Your Query:"+user_input+"\n")
        conversation_text.insert(tk.END,"ChatGpt Baba:"+response+"\n")
        text_to_speech(response)

#Create a tkinter window
root = tk.Tk()
root.title("ChatGPT Baba Ka GUI")

#Create a text box 'basically' to display response text from Baba
conversation_text = scrolledtext.ScrolledText(root,wrap=tk.WORD,width=40,height=15)
conversation_text.pack()

#User to type message in input field
user_input_entry = tk.Entry(root,width=40)
user_input_entry.pack()

#Send button
send_button = tk.Button(root,text="Send",command=send_gui)
send_button.pack()

#Start Tkinter GUI
root.mainloop()




