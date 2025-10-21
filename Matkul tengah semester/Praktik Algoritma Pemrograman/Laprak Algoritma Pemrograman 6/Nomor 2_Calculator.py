import tkinter as gui



#fungsi untuk kalskulasi aritmatika
def calculate():
    print('calculate debug',hasil.get())
    try :
        expression = Entry.get()
        value=eval(expression)
        hasil.set(str(value))
        if isinstance(value, float) and value.is_integer():
           value = int(value)
        hasil.set(str(value))
    except ZeroDivisionError:
        hasil.set('0')
    except Exception :
        hasil.set("Input tidak valid")

def tombolClear():
    Entry.delete(0,gui.END)
    hasil.set("hasil")

def tombolBackspace():
    current = Entry.get()
    if current :
        Entry.delete(len(current)-1,gui.END)


#deklaras root 
root = gui.Tk()
root.title("Kalkulator aritmatika basic")
root.configure(background='#292b2c')

#kolom input
Entry = gui.Entry(root,width=20,font=("Arial",20),justify='right',relief='ridge',background='white')
Entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

#kolom hasil
hasil = gui.StringVar(value='hasil')
label_hasil = gui.Label(root, textvariable=hasil,font=('Arial',18),anchor='e',background='white',
                        relief='sunken',width=20)
label_hasil.grid(row=1,column=0,columnspan=4,padx=10,pady=10)


#list/array Button dalam bentuk matrix
Button = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]


#loop untuk generate tombol
row,col = 2,0
for i in Button:
    if i == '=':
        cmd = calculate  #pass fungsi calculate ke tombol '='
    else :
        cmd = lambda x=i: Entry.insert(gui.END, x)
    gui.Button(root,text=i,width=5,height=2,font=('Arial',14),pady=5,command=cmd).grid(row=row,column=col)
    
    col += 1
    if col>3:
        col = 0
        row += 1

#tombol clear
gui.Button(root,text='Clear',width=5,height=2,font=('Arial',14),background='#BB86FC',
           command=tombolClear).grid(row=row,column=0)

#tombol backspace
gui.Button(root,text='⌫',width=5,height=2,font=('Arial',14),background='#BB86FC',
           command=tombolBackspace).grid(row=row,column=1)


root.mainloop()
