import sys
import logging
import tkinter as tk
from time import sleep
import keyboard
import webbrowser

root = tk.Tk()

root.geometry("+0+400")
root.lift()
root.overrideredirect(True)
root.wm_attributes("-topmost", True)
root.configure(bg='')

Title = tk.Label(root, text='HotL Overlay', font=('Consolas', 10), fg='green3', bg='gray4')
Title.grid(row=0, column=0, padx=5)
Title.bind("<Button-1>", lambda x: webbrowser.open_new_tab('https://github.com/HotAndLonely/HotLoverlay'))

Label1 = tk.Label(root, text='0', font=('Consolas', 30), fg='green3', bg='gray4')
Label1.grid(row=1, column=0, padx=0, pady=18)

Label2 = tk.Label(root, text='0', font=('Consolas', 30), fg='green3', bg='gray4')
Label2.grid(row=2, column=0, padx=0, pady=18)

Label3 = tk.Label(root, text='0', font=('Consolas', 30), fg='green3', bg='gray4')
Label3.grid(row=3, column=0, padx=0, pady=18)

Label4 = tk.Label(root, text='0', font=('Consolas', 30), fg='green3', bg='gray4')
Label4.grid(row=4, column=0, padx=0, pady=18)

def update(key):
    if key.name == '1':
        current = int(Label1.cget("text"))
        if current == 3:
            Label1.config(text="0")
        else:
            Label1.config(text=str(int(Label1.cget("text")) + 1 ))

    elif key.name == '2':
        current = int(Label2.cget("text"))
        if current == 3:
            Label2.config(text="0")
        else:
            Label2.config(text=str(int(Label2.cget("text")) + 1 ))

    elif key.name == '3':
        current = int(Label3.cget("text"))
        if current == 3:
            Label3.config(text="0")
        else:
            Label3.config(text=str(int(Label3.cget("text")) + 1 ))

    elif key.name == '4':
        current = int(Label4.cget("text"))
        if current == 3:
            Label4.config(text="0")
        else:
            Label4.config(text=str(int(Label4.cget("text")) + 1 ))

    elif key.name == '0':
        Label1.config(text='0')
        Label2.config(text='0')
        Label3.config(text='0')
        Label4.config(text='0')

keyboard.on_press(update)

root.mainloop()