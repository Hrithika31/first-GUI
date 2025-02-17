import tkinter as tk

root = tk.Tk()
root.title("My First GUI")
root.geometry("400x500")
root.configure(bg = "pink")

label = tk.Label(root, text="Hello, click the button!", font=("times new roman", 40), bg="pink")
label.pack(pady=10)

def on_button_click():
    label.config(text="Button Clicked!")

button = tk.Button(root, text="Click Me",font =("times new roman", 20), bg="pink",command=on_button_click)
button.pack(pady=10) 

root.mainloop()
