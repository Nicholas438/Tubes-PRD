from cProfile import label
from tkinter import *
import pandas as pd
from tkinter import ttk
from tkinter import filedialog
import geopy 


# DEKLARASI FUNGSI
data = pd.read_csv("data.csv")
kegiatan = ""
budget = 0
def budget1():
    global budget
    budget=1
def budget2():
    global budget
    budget=2
def budget3():
    global budget
    budget=3
def a():
    global kegiatan
    kegiatan="Kegiatan Air"
def b():
    global kegiatan
    kegiatan="Wisata Alam"
def c():
    global kegiatan
    kegiatan="Museum"
def d():
    global kegiatan
    kegiatan="Spot Foto"
def e():
    global kegiatan
    kegiatan="Kuliner"
def f():
    global kegiatan
    kegiatan="Anak anak"
def g():
    global kegiatan
    kegiatan="Trekking"
def h():
    global kegiatan
    kegiatan="Panjat Tebing"
def i():
    global kegiatan
    kegiatan="Wisata budaya"

def generate():
    df=data.loc[((data['kategori 1']== kegiatan)|(data['kategori 2']== kegiatan)) & (data['Range Budget(1: 0-100.000 2: 100.000-250.000 3: >250.000) ']== budget)]
    print(df)
    my_tree["column"]=list(df.columns)
    my_tree["show"]="headings"

    for column in my_tree["column"]:
        my_tree.heading(column, text=column)
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("", "end", values=row)
    my_tree.pack()

def distance():
    koor1=e1.get()
    koor2=e2.get()
    hasil= str(geopy.distance.geodesic(koor1,koor2).km)
    myLabel = Label(root, text=hasil)
    myLabel.pack()

    
# Membuat ui utama
root=Tk()
root.title("Tour Guide STEI ITB")
root.geometry('1000x400')


# Membuat frame kontrol
myframe= Frame(root)
myframe.grid(row=0, column=0)

myframe2= LabelFrame(root,text="Pilih Budget",bg="Wheat1")
myframe2.grid(row=1, column=0)

myframe3= LabelFrame(root,text="Pilih Kategori",bg="Wheat1")
myframe3.grid(row=2, column=0)

myframe4= LabelFrame(root,text="Lihat Hasil",bg="Wheat1")
myframe4.grid(row=3, column=0)

myframe5= LabelFrame(root,text="Distance",bg="Wheat1")
myframe5.grid(row=4, column=0)

my_tree=ttk.Treeview(myframe)


# Membuat Button kontrol
e1=Entry(myframe5, width=50, borderwidth= 5)
e1.grid(row=5,column=0, padx=10)
e2=Entry(myframe5, width=50, borderwidth= 5)
e2.grid(row=6,column=0, padx=10)
sub = Button(myframe5, text="Submit", command = distance, borderwidth= 5)
sub.grid(row=7, column=0, padx=10)

budget1_ = Button(myframe2, text="Rp 0-Rp 100.000", command = budget1, borderwidth= 5)
budget1_.grid(row = 1, column=0, padx=10)
budget2 = Button(myframe2, text="Rp 100.000-Rp 250.000", command = budget2 , borderwidth = 5)
budget2.grid(row = 1, column=1, padx=10)
budget3 = Button(myframe2, text=">Rp 250.000", command = budget3, borderwidth = 5)
budget3.grid(row =1, column=2, padx=10)
a = Button(myframe3, text="Kegiatan Air", command = a, borderwidth= 5)
a.grid(row=2, column=0, padx=10)
b = Button(myframe3, text="Wisata alam", command = b, borderwidth= 5)
b.grid(row=2, column=1, padx=10)
c=Button(myframe3, text="Museum", command = c, borderwidth= 5)
c.grid(row=2,column=2, padx=10)
d=Button(myframe3, text="Spot foto", command = d, borderwidth= 10)
d.grid(row=2,column=3, padx=10)
e=Button(myframe3, text="Kuliner", command = e, borderwidth= 10)
e.grid(row=2,column=4, padx=10)
f=Button(myframe3, text="Anak anak", command = f, borderwidth= 10)
f.grid(row=2,column=5, padx=10)
g=Button(myframe3, text="Trekking", command = g, borderwidth= 10)
g.grid(row=2,column=6, padx=10)
h=Button(myframe3, text="Panjat Tebing", command = h, borderwidth= 10)
h.grid(row=2,column=7, padx=10)
i=Button(myframe3, text="Wisata budaya", command = i, borderwidth= 10)
i.grid(row=2,column=8, padx=10)
generate=Button(myframe4, text="Generate", command = generate, borderwidth= 10)
generate.grid(row=4,column=0, padx=10)


root.mainloop() # Agar Tkinter(ui) muncul terus menerus
