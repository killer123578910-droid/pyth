import sqlite3
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
#quickinit
def multiinit(vst):
        conn=sqlite3.connect("D:\\realshit\\proj\\gui\\university.db")
        cur=conn.cursor()
        for k in vst:
            cur.execute("""
            INSERT INTO uni(name,major,gpa) VALUES(?,?,?)""",(k)
            )
        conn.commit()
        conn.close()

#function  
def taobang():
    conn=sqlite3.connect("D:\\realshit\\proj\\gui\\university.db")
    cur=conn.cursor()
    cur.execute("DROP TABLE IF EXISTS uni")
    cur.execute("""
                CREATE TABLE IF NOT EXISTS uni(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                major TEXT,
                gpa FLOAT
                )
                
    """)
    show()
    conn.commit()
    conn.close()


def combine(a,b,c):
    kq=a+","+b+","+c
    return kq

def insert(vst):
    conn=sqlite3.connect("D:\\realshit\\proj\\gui\\university.db")
    cur=conn.cursor()
    temp=vst.split(",")
    cur.execute("""
        INSERT INTO uni(name,major,gpa) VALUES(?,?,?)""",(
            temp[0],temp[1],temp[2]
        ))
    conn.commit()
    conn.close()
    show()




def truyvan(inp):
    conn=sqlite3.connect("D:\\realshit\\proj\\gui\\university.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM uni")
    liste=cur.fetchall()
    cur.close()
    if inp=="0":
        return liste
    else:
        temp=[]
        for k in liste:
            if float(k[3])>3.0:
                temp.append(k)
        return temp
    

def update(namee,gpaa,idd):
    conn=sqlite3.connect("D:\\realshit\\proj\\gui\\university.db")
    cur=conn.cursor()
    cur.execute("""
                UPDATE uni
                SET gpa=? 
                WHERE name=? and id=?""",(gpaa,namee,idd))
    conn.commit()
    conn.close()
    show()



def show(key="0"):
    for item in tree.get_children():
        tree.delete(item)
    data=truyvan(key)
    for row in data:
        tree.insert("", tk.END, values=row)


def delete():
    conn=sqlite3.connect("D:\\realshit\\proj\\gui\\university.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM uni WHERE gpa < 2.0")
    conn.commit()
    conn.close()
    show()
    


#khung tkinkter
goc=ctk.CTk()
goc.title("Uniserver")
goc.geometry("1080x720")
columns=("id","name","major","gpa")

# data = [
#     ("Nguyễn Văn An", "Công nghệ thông tin", 3.2),
#     ("Trần Thị Bình", "Khoa học dữ liệu", 3.8),
#     ("Lê Minh Cường", "Kỹ thuật phần mềm", 2.9),
#     ("Phạm Thị Dung", "Hệ thống thông tin", 3.5),
#     ("Hoàng Văn Em", "An toàn thông tin", 3.0),
#     ("Đỗ Thị Phương", "Trí tuệ nhân tạo", 3.7),
#     ("Vũ Quang Huy", "Mạng máy tính", 2.8),
#     ("Bùi Thị Lan", "Kỹ thuật máy tính", 3.4),
#     ("Ngô Đức Long", "Khoa học máy tính", 3.6),
#     ("Đặng Thị Mai", "Phân tích dữ liệu", 3.1)
# ]
# multiinit(data)

#bang sql
tree=ttk.Treeview(goc,column=columns,show="headings")
for col in columns:
    tree.heading(col,text=col)
    tree.column(col,width=100)
tree.pack(expand=True, fill='both')




#cac nut
frame = ctk.CTkFrame(goc)
frame.pack(pady=10)

entry0 = ctk.CTkEntry(frame,placeholder_text="id" ,width=100)
entry0.grid(row=0, column=0, padx=2)

entry1 = ctk.CTkEntry(frame,placeholder_text="nhập tên" ,width=100)
entry1.grid(row=0, column=1, padx=2)

entry2 = ctk.CTkEntry(frame,placeholder_text="major" ,width=100)
entry2.grid(row=0, column=2, padx=2)

entry3 = ctk.CTkEntry(frame,placeholder_text="gpa" ,width=100)
entry3.grid(row=0, column=3, padx=2)

entry4 = ctk.CTkEntry(frame,placeholder_text="0:cả bảng,1:gpa>3.0" ,width=100)
entry4.grid(row=0, column=4, padx=2)



btn1 = ctk.CTkButton(frame, text="Insert",width=100,
                    command=lambda: insert(combine(entry1.get(),entry2.get(),entry3.get()),entry4.get()))
btn1.grid(row=1, column=3, padx=2)


btn2 = ctk.CTkButton(frame, text="Reset hệ thống",width=100,
                    command=lambda:taobang())
btn2.grid(row=1, column=0, padx=2)


btn3 = ctk.CTkButton(frame, text="Update",width=100,
                    command=lambda:update(entry1.get(),entry3.get(),entry0.get()))
btn3.grid(row=1, column=1, padx=2)


btn4 = ctk.CTkButton(frame, text="Truy vấn",width=100,
                    command=lambda:show(entry4.get()))
btn4.grid(row=1, column=2, padx=2)


btn5 = ctk.CTkButton(frame, text="Xóa",width=100,command=delete)
btn5.grid(row=1, column=4, padx=2)




goc.mainloop()
