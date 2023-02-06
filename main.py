import sys
import logging
import tkinter as tk
from time import sleep
import keyboard
import webbrowser
import os

mouse_protection = False

def main():

    global mouse_protection

    root = tk.Tk()

    root.geometry("+0+400")
    root.lift()
    root.overrideredirect(True)
    root.wm_attributes("-topmost", True)
    root.configure(bg='')

    Title = tk.Label(root, text='Geneva', font=('Consolas', 10), fg='green3', bg='black')
    Title.grid(row=0, column=0, padx=5)
    Title.bind("<Button-1>", lambda x: webbrowser.open_new_tab('https://github.com/HotAndLonely/HotLoverlay'))

    Label1 = tk.Label(root, text='0', font=('Geneva', 30), fg='green3', bg='black')
    Label1.grid(row=1, column=0, padx=0, pady=18)

    Label2 = tk.Label(root, text='0', font=('Geneva', 30), fg='green3', bg='black')
    Label2.grid(row=2, column=0, padx=0, pady=18)

    Label3 = tk.Label(root, text='0', font=('Geneva', 30), fg='green3', bg='black')
    Label3.grid(row=3, column=0, padx=0, pady=18)

    Label4 = tk.Label(root, text='0', font=('Geneva', 30), fg='green3', bg='black')
    Label4.grid(row=4, column=0, padx=0, pady=18)

    Protection = tk.Label(root, text='Enable(8)', font=('Geneva', 15), fg='green3', bg='black')
    Protection.grid(row=5, column=0, padx=5, pady=0)

    Close = tk.Label(root, text='Exit(9)', font=('Geneva', 15), fg='green3', bg='black')
    Close.grid(row=6, column=0, pady=0)

    def update(key):
        global mouse_protection

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

        elif key.name == '8':
            mouse_protection = not mouse_protection
        elif key.name == '9':
            root.destroy()

    def onHoverHide(e):
        if mouse_protection == False:
            root.withdraw()
            sleep(0.5)
            root.deiconify()

    keyboard.on_press(update)
    root.bind('<Motion>', onHoverHide)

    root.mainloop()

if __name__ == '__main__':
    main()
