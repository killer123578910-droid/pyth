import customtkinter as ctk
import math

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Calculator")
app.geometry("1024x768")

# -------- Display --------
entry = ctk.CTkEntry(app, width=580, height=200, font=("Arial", 20))
entry.pack(pady=10)

# -------- Functions --------
def click(value):
    if entry.get()=="Error":
        entry.delete(0,"end")
    entry.insert("end", value)

def clear():
    entry.delete(0, "end")
def acclear():
    cur=entry.get()
    entry.delete(0,"end")
    entry.insert(0,cur[:-1])

def calculate():
    try:
        cur=entry.get()
        result = eval(cur,{"__builtins__":None},{
            "sin":math.sin,
            "cos":math.cos,
            "tan":math.tan,
            "pi":math.pi,
        })
        entry.delete(0, "end")
        entry.insert(0, str(result))
    except:
        entry.delete(0, "end")
        entry.insert(0, "Error")


# -------- Buttons --------
buttons = [
    ["sin(","cos(","tan(","pi"],
    ["(" , ")" , "AC","C"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

frame = ctk.CTkFrame(app)
frame.pack()

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == "=":
            btn = ctk.CTkButton(frame, text=text, width=70,height=70, command=calculate)
        elif text=="C":
            btn = ctk.CTkButton(frame, text=text,width=70,height=70, command=clear)
        elif text=="AC":
            btn = ctk.CTkButton(frame, text=text,width=70,height=70, command=acclear)
        else:
            btn = ctk.CTkButton(frame, text=text, width=70,height=70,
                                command=lambda t=text: click(t))
        btn.grid(row=i, column=j, padx=2, pady=2)
app.mainloop()