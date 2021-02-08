from tkinter import*
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import*
import fileinput
from tkinter.messagebox import*
root=Tk()
root.geometry("1000x600")
root.title("Cars and characteristics")


root.iconbitmap(default="car_icon4979.ico")

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


m2=Menu(M,tearoff=0)
M.add_cascade(label="Mercedes",menu=m2)

m2.add_command(label="Mercedes E63",command=lambda:papich_image("MB e63.png"))
m2.add_command(label="Mercedes S63",command=lambda:papich_image("MB s63.png"))
m2.add_command(label="Mercedes C63",command=lambda:papich_image("c63 Karolina.png"))
m2.add_command(label="Mercedes E500",command=lambda:papich_image("MB w124.png"))
m2.add_command(label="Mercedes S600",command=lambda:papich_image("W140 MB.png"))



m3=Menu(M,tearoff=0)
M.add_cascade(label="BMW",menu=m3)

m3.add_command(label="BMW X5M",command=lambda:papich_image("BMW x5.png"))
m3.add_command(label="BMW M4",command=lambda:papich_image("Bmw m4.png"))
m3.add_command(label="BMW M2",command=lambda:papich_image("bmw m2.png"))
m3.add_command(label="BMW M3 e36",command=lambda:papich_image("m3 e366.png"))
m3.add_command(label="BMW M3 e46",command=lambda:papich_image("m3 e46.png"))

m4=Menu(M,tearoff=0)
M.add_cascade(label="Audi",menu=m4)

m4.add_command(label="Audi RS6",command=lambda:papich_image("Audi RS6.png"))
m4.add_command(label="Audi RS7",command=lambda:papich_image("Audi RS7.png"))
m4.add_command(label="Audi R8",command=lambda:papich_image("Audi R88.png"))
m4.add_command(label="Audi TTS",command=lambda:papich_image("Audi TTRS.png"))
m4.add_command(label="Audi S5 ",command=lambda:papich_image("Audi RS 5.png"))

m5=Menu(M,tearoff=0)
M.add_cascade(label="Hypercars",menu=m5)

m5.add_command(label="Buggati Veyron",command=lambda:papich_image("buggati veyron.png"))
m5.add_command(label="Lamborghini Aventador SVJ",command=lambda:papich_image("aventador SVJ.png"))
m5.add_command(label="Lamborghini Gallardo",command=lambda:papich_image("Gallardo.png"))
m5.add_command(label="Porsche Carrera GT ",command=lambda:papich_image("Carrera GT.png"))
m5.add_command(label="Ferrari LaFerrari ",command=lambda:papich_image("Ferra.png"))






m6=Menu(M,tearoff=0)
M.add_cascade(label="Cars characteristics",menu=m6)
m6.add_command(label="Audi rs6 characteristics ",command=lambda:papich_image("RS6 character.PNG"))
m6.add_command(label="Mercedes e63 characteristics",command=lambda:papich_image("e63 char.PNG"))
m6.add_command(label="Mercedes s63 characteristics",command=lambda:papich_image("s63 char.PNG"))
m6.add_command(label="BMW X5M characteristics",command=lambda:papich_image("BMW x5 char.PNG"))
m6.add_command(label="Mercedes c63 characteristics",command=lambda:papich_image("c63 char.PNG"))
m6.add_command(label="BMW M4 characteristics ",command=lambda:papich_image("M4 char.PNG"))
m6.add_command(label="BMW M3 e36 characteristics ",command=lambda:papich_image("e36 char.PNG"))
m6.add_command(label="BMW M3 e46 characteristics ",command=lambda:papich_image("bmw e46 char.PNG"))
m6.add_command(label="Mercedes E500 characteristics ",command=lambda:papich_image("MB w124 char.PNG"))
m6.add_command(label="Mercedes S600 characteristics ",command=lambda:papich_image("MB w140 char.PNG"))
m6.add_command(label="Audi RS7 characteristics",command=lambda:papich_image("RS7 char.PNG"))
m6.add_command(label="Audi R8 characteristics",command=lambda:papich_image("Audi R8 char.PNG"))
m6.add_command(label="Audi TTS characteristics",command=lambda:papich_image("Audi TT RS.PNG"))
m6.add_command(label="Audi S5 characteristics",command=lambda:papich_image("Audi S5 char.PNG"))
m6.add_command(label="Buggati Veyron characteristics",command=lambda:papich_image("Buggati veyron char.PNG"))
m6.add_command(label="Lamborghini Aventador SVJ characteristics",command=lambda:papich_image("aventador SVJ char.PNG"))
m6.add_command(label="Lamborghini Gallardo characteristics",command=lambda:papich_image("Galardo char.PNG"))
m6.add_command(label="Porsche Carrera GT characteristics",command=lambda:papich_image("Carrera GT char.PNG"))
m6.add_command(label="Ferrari LaFerrari",command=lambda:papich_image("Ferra png.PNG"))


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