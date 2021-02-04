from tkinter import*
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import*
import fileinput
from tkinter.messagebox import*
root=Tk()
root.geometry("1000x600")
root.title("Cars and characteristics")

def funktion(a):
    tabs.select(a)



def papich_image(name):
    global img
    tabs.select(0)
    img=PhotoImage(file=name).subsample(4)
    can.create_image(10,10,image=img,anchor=NW)

def char_image(name):
    global img
    tabs.select(3)
    img=PhotoImage(file=name).subsample(4)
    can.create_image(10,10,image=img,anchor=NW)



tabs=ttk.Notebook(root)
texts=["Esimene","Teine","Kolmas","Neljas","Viies","Kuues","Seitsmes","Kaheksas"]
#or i in range(8):
  # tab=Frame(tabs)
   #tabs.add(tab,text=texts[i])

tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)
tab4=Frame(tabs)

tabs.add(tab2,text="Cars")


M=Menu(root)
root.config(menu=M)
m1=Menu(M,tearoff=1)
M.add_cascade(label="Tabs",menu=m1)
m1.add_command(label="Tab1",accelerator="Command+V",command=lambda:funktion(0))
m1.add_command(label="Tab2",command=lambda:funktion(1))

m2=Menu(M,tearoff=0)
M.add_cascade(label="Cars",menu=m2)
m2.add_command(label="Audi rs6",command=lambda:papich_image("Audi RS6.png"))
m2.add_command(label="Mercedes e63",command=lambda:papich_image("MB e63.png"))
m2.add_command(label="Mercedes s63",command=lambda:papich_image("MB s63.png"))
m2.add_command(label="Jaguar F-type",command=lambda:papich_image("Jaguar ftype.png"))
m2.add_command(label="BMW X5M",command=lambda:papich_image("BMW x5.png"))
m2.add_command(label="Toyota land cruiser",command=lambda:papich_image("13+Land+Cruiser.png"))
m2.add_command(label="Nissan skyline",command=lambda:papich_image("Sky.png"))
m2.add_command(label="Ford mustang",command=lambda:papich_image("Mustang.png"))
m2.add_command(label="Mercedes c63",command=lambda:papich_image("c63 Karolina.png"))


m3=Menu(M,tearoff=0)
M.add_cascade(label="Cars characteristics",menu=m3)
m3.add_command(label="Audi rs6 characteristics ",command=lambda:papich_image("RS6 character.PNG"))
m3.add_command(label="Mercedes e63 characteristics",command=lambda:papich_image("e63 char.PNG"))
m3.add_command(label="Mercedes s63 characteristics",command=lambda:papich_image("s63 char.PNG"))
m3.add_command(label="Jaguar F-type characteristics",command=lambda:papich_image("F-type char.PNG"))
m3.add_command(label="BMW X5M characteristics",command=lambda:papich_image("BMW x5 char.PNG"))
m3.add_command(label="Toyota Land Cruiser characteristics",command=lambda:papich_image("Toyota LC char.PNG"))
m3.add_command(label="Nissan skyline characteristics",command=lambda:papich_image("Sky  char.PNG"))
m3.add_command(label="Ford mustang characteristics",command=lambda:papich_image("Mustang char.PNG"))
m3.add_command(label="Mercedes c63 characteristics",command=lambda:papich_image("c63 char.PNG"))



can=Canvas(tab2,width=600,height=800)
img=PhotoImage(file="Audi RS6.png").subsample(4)
can.create_image(15,15,image=img,anchor=NW)
can.pack()
tabs.pack(fill="both")
root.mainloop()

can=Canvas(tab4,width=600,height=800)
img=PhotoImage(file="Audi RS6.png").subsample(4)
can.create_image(15,15,image=img,anchor=NW)
can.pack()
tabs.pack(fill="both")
root.mainloop()
