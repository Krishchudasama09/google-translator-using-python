from tkinter import*
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="Hindi"):
    text1=text
    sec1=src
    dest1=dest

    trans=Translator()
    trans1=trans.Translate(text,src,dest=dest)
    return trans1.text

def data():
    s=combo_sor.get()
    d=combo_dest.get()
    masg =sor_text.get(1.0,END)
    textget =change(text=masg,src=s,dest=d)
    dest_text.delete(1.0,END)
    dest_text.insert(END,textget)

root=Tk()
root.title("Translator")
root.geometry("600x600")
root.config(bg="black")

lab_txt =Label(root,text="Translator",font="Sans-serif""bold",bg="white")
lab_txt.place(x=100,y=20,height=30,width=350)

frame=Frame(root).pack(side=BOTTOM) # root object nu frame bnave che ,and pack ea place kre

lab_txt =Label(root,text="Source Text",font="Sans-serif""bold",bg="white")
lab_txt.place(x=100,y=80,height=20,width=350)


sor_text=Text(frame,font=("Sans-serif""bold"),wrap=WORD)# frame nu text box bane
sor_text.place(x=10,y=120,height=200,width=530)

list_text=list(LANGUAGES.values())

combo_sor=ttk.Combobox(frame,value=list_text)
combo_sor.place(x=30,y=330,height=30,width=80)

combo_sor.set("ENGLISH") 

button_change=Button(frame,text="TRANSLATE",relief=RAISED,command=data) #relief and reaised ea 3d button provide kare
button_change.place(x=240,y=330,height=30,width=80)

combo_dest=ttk.Combobox(frame,value=list_text)
combo_dest.place(x=440,y=330,height=30,width=80)
combo_dest.set("ENGLISH")

lab_txt =Label(root,text="Destination Text",font="Sans-serif""bold",bg="white")
lab_txt.place(x=100,y=380,height=20,width=350)

dest_text=Text(frame,font=("Sans-serif""bold"),wrap=WORD)# frame nu text box bane
dest_text.place(x=10,y=420,height=220,width=530)

root.mainloop()
