import customtkinter as ctk
import math

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Calculator")
app.geometry("355x450")

# -------- Display --------
entry = ctk.CTkEntry(app, width=340, height=100, font=("Arial", 20))
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
        cur = cur.replace("√", "sqrt") 
        result = eval(cur,{"__builtins__":None},{
            "sin":math.sin,
            "cos":math.cos,
            "tan":math.tan,
            "sqrt":math.sqrt,
        })
        entry.delete(0, "end")
        entry.insert(0, str(result))
    except:
        entry.delete(0, "end")
        entry.insert(0, "Error")


# -------- Buttons --------
buttons = [
    ["sin(","cos(","tan(","√("],
    ["(" , ")" , "AC","C"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]
app.bind("<Return>", lambda e: calculate())
app.bind("<BackSpace>", lambda e: acclear())
frame = ctk.CTkFrame(app)
frame.pack()

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == "=":
            btn = ctk.CTkButton(frame, text=text, width=75,height=45, command=calculate,font=("Arial",15,"bold"),fg_color="#FD0288")
        elif text=="C":
            btn = ctk.CTkButton(frame, text=text,width=75,height=45, command=clear,font=("Arial",15,"bold"))
        elif text=="AC":
            btn = ctk.CTkButton(frame, text=text,width=75,height=45, command=acclear,font=("Arial",15,"bold"))
        else:
            btn = ctk.CTkButton(frame, text=text, width=75,height=45,
                                command=lambda t=text: click(t),font=("Arial",15,"bold"),fg_color="#5AA359")
        btn.grid(row=i, column=j, padx=2, pady=2)
app.mainloop()