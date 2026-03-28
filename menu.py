import tkinter as tk
from tkinter import messagebox, filedialog

r = tk.Tk()
r.geometry("300x250")

lb = tk.Listbox(r)
sb = tk.Scrollbar(r)

lb.pack(side="left", fill="both", expand=True)
sb.pack(side="right", fill="y")

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

for i in range(20):
    lb.insert("end", "Item " + str(i))

def msg():
    messagebox.showinfo("Info", "Hello")

def openf():
    filedialog.askopenfilename()

m = tk.Menu(r)
r.config(menu=m)

fm = tk.Menu(m, tearoff=0)
m.add_cascade(label="File", menu=fm)
fm.add_command(label="Open", command=openf)
fm.add_command(label="Exit", command=r.quit)

mb = tk.Menubutton(r, text="Options", relief="raised")
mb.menu = tk.Menu(mb, tearoff=0)
mb["menu"] = mb.menu
mb.menu.add_command(label="Show Msg", command=msg)
mb.pack()

r.mainloop()