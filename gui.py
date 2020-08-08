import CP
import tkinter as tk
from tkinter import ttk
import pandas as pd

def result_set(*args):
    if poke_name.get() != "":
        res.set(CP.pokemon(poke_name.get(),Aiv.get(),Div.get(),Hiv.get(),pl.get()).CP())
    else:pass


df = pd.read_pickle(r"C:\Users\ktmks\programming\GUI_app\Data\race_values.pkl")
poke_names = df.index.values.tolist()
poke_names.sort()

root = tk.Tk()
root.title("CP計算ツール")
root.geometry("400x300")
mainframe = ttk.Frame(root,padding="20",relief="solid")
mainframe.grid(column=0,row=0,sticky=("N","W","E","S"))
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

poke_name = tk.StringVar(value="カイリュー")
Aiv = tk.IntVar(value=15)
Div = tk.IntVar(value=15)
Hiv = tk.IntVar(value=15)
res = tk.IntVar()
pl = tk.DoubleVar(value=40)
ivs = [i for i in range(15,-1,-1)]


Pokename_entry = ttk.Combobox(mainframe,
                              textvariable = poke_name,
                              values       = poke_names,
                              width        = 15,
                              )
Pokename_entry.grid(column=3,row=0)
Pokename_entry.bind("<<ComboboxSelected>>",result_set)

Aiv_entry = ttk.Combobox(mainframe,
                         width        = 4,
                         values       = ivs,
                         textvariable = Aiv)
Aiv_entry.grid(column=2,row=2)
Aiv_entry.bind("<<ComboboxSelected>>",result_set)

Div_entry = ttk.Combobox(mainframe,
                         width        = 4,
                         values       = ivs,
                         textvariable = Div)
Div_entry.grid(column=3,row=2)
Div_entry.bind("<<ComboboxSelected>>",result_set)

Hiv_entry = ttk.Combobox(mainframe,
                         width        = 4,
                         values       = ivs,
                         textvariable = Hiv)
Hiv_entry.grid(column=4,row=2)
Hiv_entry.bind("<<ComboboxSelected>>",result_set)



ttk.Label(mainframe,text="ポケモン名").grid(column=1,row=0)

ttk.Label(mainframe, text="個体値").grid(column=1,row=2)
ttk.Label(mainframe, text="攻撃").grid(column=2, row=1)
ttk.Label(mainframe, text="防御").grid(column=3, row=1)
ttk.Label(mainframe, text="HP").grid(column=4, row=1)

ttk.Label(mainframe,text="PL").grid(column=1,row=3)
tk.Scale(mainframe,
         orient="horizontal",
         variable=pl,
         from_=1,to=40,
         resolution=0.5,
         length=250,
         command=result_set,
         ).grid(column=2,columnspan=3,row=3)

ttk.Label(mainframe,text="CPは").grid(column=1,row=5)
ttk.Label(mainframe,textvariable=res).grid(column=2,row=5)
ttk.Label(mainframe,text="です").grid(column=3,row=5)

for child in mainframe.winfo_children():
    child.grid_configure(padx=10,pady=10)

Pokename_entry.focus()
root.bind("<Return>",result_set)


root.mainloop()





