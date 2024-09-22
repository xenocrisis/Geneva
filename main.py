import tkinter as tk
from tkinter import ttk, colorchooser, messagebox
import json
import os
import keyboard
import webbrowser
from time import sleep

# Cargar las preferencias desde un archivo JSON o usar valores por defecto
def load_preferences():
    default_preferences = {
        "mouseMissClickProtection": {"value": False},
        "textFont": {"value": "Geneva"},
        "textColor": {"value": "#0fff15"},
        "textBgColor": {"value": "#aea4bf"},
        "xPosition": {"value": 0},
        "yPosition": {"value": 400}
    }
    
    if os.path.exists("preferences.json"):
        with open("preferences.json", "r") as file:
            preferences = json.load(file)
            # Actualizar las preferencias con valores por defecto si alguna clave no está presente
            for key in default_preferences:
                if key not in preferences:
                    preferences[key] = default_preferences[key]
            return preferences
    else:
        return default_preferences

# Guardar las preferencias en un archivo JSON
def save_preferences(preferences):
    with open("preferences.json", "w") as file:
        json.dump(preferences, file, indent=4)

# Actualizar la vista previa de la fuente en la ventana de opciones
def update_font_preview():
    font_preview_label.config(font=(text_font_var.get(), 12))

# Seleccionar color usando el selector de color
def choose_color(var):
    color = colorchooser.askcolor()[1]  # Devuelve un tuple, el segundo elemento es el código del color
    if color:
        var.set(color)

# Aplicar preferencias a la interfaz
def apply_preferences():
    # Actualizar las propiedades de los labels
    for label in [Label1, Label2, Label3, Label4, Dev, Options, Protection, Close]:
        label.config(font=(preferences['textFont']['value'], 30 if label in [Label1, Label2, Label3, Label4] else 15),
                     fg=preferences['textColor']['value'],
                     bg=preferences['textBgColor']['value'])
    root.geometry(f"+{preferences['xPosition']['value']}+{preferences['yPosition']['value']}")

# Ventana para cambiar las preferencias
def open_preferences_window():
    preferences_window = tk.Toplevel(root)
    preferences_window.title("Preferences")
    
    def update_preferences():
        preferences['mouseMissClickProtection']['value'] = mouse_protection_var.get()
        preferences['textFont']['value'] = text_font_var.get()
        preferences['textColor']['value'] = text_color_var.get()
        preferences['textBgColor']['value'] = text_bg_color_var.get()
        preferences['xPosition']['value'] = x_position_var.get()
        preferences['yPosition']['value'] = y_position_var.get()
        
        save_preferences(preferences)
        apply_preferences()  # Aplicar los cambios inmediatamente
        messagebox.showinfo("Preferences", "Preferences saved and applied successfully!")
        preferences_window.destroy()

    mouse_protection_var = tk.BooleanVar(value=preferences['mouseMissClickProtection']['value'])
    text_font_var = tk.StringVar(value=preferences['textFont']['value'])
    text_color_var = tk.StringVar(value=preferences['textColor']['value'])
    text_bg_color_var = tk.StringVar(value=preferences['textBgColor']['value'])
    x_position_var = tk.IntVar(value=preferences['xPosition']['value'])
    y_position_var = tk.IntVar(value=preferences['yPosition']['value'])

    tk.Label(preferences_window, text="Text Font:").grid(row=1, column=0, sticky="w")
    fonts = ["Geneva", "Arial", "Courier", "Helvetica", "Times", "Verdana"]
    font_combobox = ttk.Combobox(preferences_window, textvariable=text_font_var, values=fonts)
    font_combobox.grid(row=1, column=1)
    font_combobox.bind("<<ComboboxSelected>>", lambda event: update_font_preview())

    tk.Label(preferences_window, text="Text Color:").grid(row=2, column=0, sticky="w")
    text_color_button = tk.Button(preferences_window, text="Choose Color", command=lambda: choose_color(text_color_var))
    text_color_button.grid(row=2, column=1)

    tk.Label(preferences_window, text="Text Background Color:").grid(row=3, column=0, sticky="w")
    text_bg_color_button = tk.Button(preferences_window, text="Choose Color", command=lambda: choose_color(text_bg_color_var))
    text_bg_color_button.grid(row=3, column=1)

    tk.Label(preferences_window, text="X Position:").grid(row=4, column=0, sticky="w")
    tk.Entry(preferences_window, textvariable=x_position_var).grid(row=4, column=1)

    tk.Label(preferences_window, text="Y Position:").grid(row=5, column=0, sticky="w")
    tk.Entry(preferences_window, textvariable=y_position_var).grid(row=5, column=1)

    tk.Button(preferences_window, text="Save", command=update_preferences).grid(row=7, columnspan=2)

# Cargar las preferencias al iniciar
preferences = load_preferences()

# Configurar ventana principal
root = tk.Tk()
root.geometry(f"+{preferences['xPosition']['value']}+{preferences['yPosition']['value']}")
root.lift()
root.overrideredirect(True)
root.wm_attributes("-topmost", True)
root.configure(bg='')

Label1 = tk.Label(root, text='0', font=(preferences['textFont']['value'], 30), fg=preferences['textColor']['value'], bg=preferences['textBgColor']['value'])
Label1.grid(row=1, column=0, padx=0, pady=18)

Label2 = tk.Label(root, text='0', font=(preferences['textFont']['value'], 30), fg=preferences['textColor']['value'], bg=preferences['textBgColor']['value'])
Label2.grid(row=2, column=0, padx=0, pady=18)

Label3 = tk.Label(root, text='0', font=(preferences['textFont']['value'], 30), fg=preferences['textColor']['value'], bg=preferences['textBgColor']['value'])
Label3.grid(row=3, column=0, padx=0, pady=18)

Label4 = tk.Label(root, text='0', font=(preferences['textFont']['value'], 30), fg=preferences['textColor']['value'], bg=preferences['textBgColor']['value'])
Label4.grid(row=4, column=0, padx=0, pady=18)

Dev = tk.Label(root, text='xenocrisis', font=(preferences['textFont']['value'], 10), fg=preferences['textColor']['value'], bg=preferences['textBgColor']['value'])
Dev.grid(row=5, column=0, padx=5)
Dev.bind("<Button-1>", lambda x: webbrowser.open_new_tab('https://github.com/HotAndLonely/HotLoverlay'))

# Instrucción para acceder a opciones con la tecla 7
Options = tk.Label(root, text='Options (7)', font=(preferences['textFont']['value'], 15), fg=preferences['textColor']['value'], bg=preferences['textBgColor']['value'])
Options.grid(row=6, column=0, pady=0)

Protection = tk.Label(root, text='Hover (8)', font=(preferences['textFont']['value'], 15), fg=preferences['textColor']['value'], bg=preferences['textBgColor']['value'])
Protection.grid(row=7, column=0, padx=5, pady=0)

Close = tk.Label(root, text='Exit (9)', font=(preferences['textFont']['value'], 15), fg=preferences['textColor']['value'], bg=preferences['textBgColor']['value'])
Close.grid(row=8, column=0, pady=0)

mouse_protection = preferences['mouseMissClickProtection']['value']

def update(key):
    global mouse_protection

    if key.name == '1':
        current = int(Label1.cget("text"))
        if current == 3:
            Label1.config(text="0")
        else:
            Label1.config(text=str(int(Label1.cget("text")) + 1))

    elif key.name == '2':
        current = int(Label2.cget("text"))
        if current == 3:
            Label2.config(text="0")
        else:
            Label2.config(text=str(int(Label2.cget("text")) + 1))

    elif key.name == '3':
        current = int(Label3.cget("text"))
        if current == 3:
            Label3.config(text="0")
        else:
            Label3.config(text=str(int(Label3.cget("text")) + 1))

    elif key.name == '4':
        current = int(Label4.cget("text"))
        if current == 3:
            Label4.config(text="0")
        else:
            Label4.config(text=str(int(Label4.cget("text")) + 1))

    elif key.name == '0':
        Label1.config(text='0')
        Label2.config(text='0')
        Label3.config(text='0')
        Label4.config(text='0')

    elif key.name == '7':  # Abrir ventana de opciones al presionar 7
        open_preferences_window()
    elif key.name == '8':
        mouse_protection = not mouse_protection
    elif key.name == '9':
        root.destroy()

def onHoverHide(e):
    if not mouse_protection:
        root.withdraw()
        sleep(0.5)
        root.deiconify()

keyboard.on_press(update)
root.bind('<Motion>', onHoverHide)

root.mainloop()
