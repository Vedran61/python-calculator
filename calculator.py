
#           _____   _____       _____ _____         _______ _____                        _____ _______ _____  _____ _ 
#     /\   |  __ \ / ____|     / ____|  __ \     /\|__   __|_   _|   /\            /\   |  __ \__   __|_   _|/ ____| |
#    /  \  | |__) | (___      | |  __| |__) |   /  \  | |    | |    /  \          /  \  | |__) | | |    | | | (___ | |
#   / /\ \ |  _  / \___ \     | | |_ |  _  /   / /\ \ | |    | |   / /\ \        / /\ \ |  _  /  | |    | |  \___ \| |
#  / ____ \| | \ \ ____) |    | |__| | | \ \  / ____ \| |   _| |_ / ____ \      / ____ \| | \ \  | |   _| |_ ____) |_|
# /_/    \_\_|  \_\_____/      \_____|_|  \_\/_/    \_\_|  |_____/_/    \_\    /_/    \_\_|  \_\ |_|  |_____|_____/(_)
 
import tkinter as tk
import math

win = tk.Tk()
win.geometry("400x580")
win.title("Calculator - Vedran61")
win.configure(borderwidth=0, highlightthickness=0, bg="#1C1C1C")
win.resizable(False, False)

result_var = tk.StringVar()
result_entry = tk.Entry(win, 
                        textvariable=result_var, 
                        width=9, borderwidth=0, highlightthickness=0, 
                        font=("Arial", 56), bg="#2E2E2E", fg="white", justify="right")
result_entry.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

operation = ""

def on_button_click(btn):
    global operation
    if btn in ["+","-","x","/","%","√",".","="] and operation == "": #if there is no any number but user try using operations...
        return #return nothing...
    else:
        if btn == "=":
            if True:
                operation = operation.replace("x", "*")
                result = eval(operation)
                if result.is_integer():  #if result an integer...
                    result_var.set(str(int(result)))
                else:
                    result_var.set(str(result))
                operation = str(result)
        elif btn == "C":
            operation = ""
            result_var.set("")
        elif btn == "√":
            if True:
                result = math.sqrt(float(operation))
                if result.is_integer():  # If result is an integer...
                    result_var.set(str(int(result)))
                else:
                    result_var.set(str(result))
                operation = str(result)
        elif btn == "%":
            if operation:
                if "%" in operation:
                    base, percent = operation.split("%")
                    result = float(base)*(float(percent)/100)
                else:
                    result = float(operation)*0.01
                result_var.set(str(result))
                operation = str(result)
            else:
                result_var.set("Error")
                operation = ""
        else:
            operation += btn
            result_var.set(operation) 

buttons = [
    ("C", 1, 0), ("%", 1, 1), ("√", 1, 2), ("+", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("x", 3, 3),
    ("7", 4, 0), ("8", 4, 1), ("9", 4, 2), ("/", 4, 3),
    (".", 5, 0), ("0", 5, 1), ("00", 5, 2), ("=", 5, 3)
] # text, row, column

for (text, row, col) in buttons:
    if text == "=":
        color = "#93C572"
    elif text == "C":
        color = "#E63946"
    else:
        color = "#1C1C1C"
    fg_color = "white"
    button = tk.Button(win, 
                       text=text, 
                       height=3, width=6, 
                       bg=color, fg=fg_color, 
                       borderwidth=0, highlightthickness=0, 
                       font=("Arial", 18),
                       command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=col, padx=0, pady=0, sticky="nsew")

win.mainloop()