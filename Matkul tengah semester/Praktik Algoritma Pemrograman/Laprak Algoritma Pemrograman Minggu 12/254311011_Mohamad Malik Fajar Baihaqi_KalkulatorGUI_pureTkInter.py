import tkinter as tk
from tkinter import messagebox

# Fungsi-fungsi Kalkulator 

def tambah_angka(angka):
    """Menambahkan angka/operator ke tampilan."""
    current = input_text.get()
    
    # Reset tampilan jika ada Error atau angka awal adalah 0
    if current in ("Error", "0") and str(angka).isdigit() or current == "0" and str(angka) == '.':
        input_text.set(str(angka))
    elif current == "0" and not str(angka).isdigit() and str(angka) != '.':
        # Izinkan operator aritmatika dimasukkan setelah '0'
        input_text.set(current + str(angka))
    else:
        input_text.set(current + str(angka))

def operasikan_clear():
    """Mengosongkan tampilan, kembali ke '0'."""
    input_text.set("0")

def operasikan_hitung():
    """Menghitung ekspresi yang ada di tampilan."""
    try:
        ekspresi = input_text.get()
        # Mengganti simbol 'x' menjadi '*' dan '÷' menjadi '/' untuk perhitungan Python
        ekspresi = ekspresi.replace('x', '*').replace('÷', '/')
        
        # Evaluasi ekspresi aritmatika
        hasil = str(eval(ekspresi))
        input_text.set(hasil)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Pembagian dengan nol!")
        input_text.set("Error")
    except Exception:
        messagebox.showerror("Error", "Ekspresi tidak valid!")
        input_text.set("Error")

# Pengaturan Utama Tkinter

root = tk.Tk()
root.title("Kalkulator")
root.geometry("300x420")
root.resizable(False, False) 

# Skema Warna
BODY_COLOR = "#3C3C3C" # Abu-abu gelap (body kalkulator)
BUTTON_COLOR = "#505050" # Abu-abu untuk tombol angka
OPERATOR_COLOR = "#666666" # Abu-abu lebih terang untuk operator
EQUAL_COLOR = "#FF9500" # Oranye untuk tombol '='
TEXT_COLOR = "white"

root.configure(bg=BODY_COLOR) 

# Variabel untuk menampung teks yang ditampilkan
input_text = tk.StringVar()
input_text.set("0") 

#Font Consolas
DISPLAY_FONT = ('Consolas', 32, 'bold') 
BUTTON_FONT = ('Arial', 18)

#Tampilan/Display Kalkulator
display_frame = tk.Frame(root, bg=BODY_COLOR)
display_frame.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="nsew")

display = tk.Entry(
    display_frame, # Ditempatkan dalam frame
    textvariable=input_text, 
    font=DISPLAY_FONT, 
    bd=10, 
    width=13, 
    justify='right', 
    bg="#C8C8C8", # Latar belakang display abu-abu muda
    fg="#333333", # Warna teks
    relief=tk.GROOVE, # Relief Groove tombol timbul
    highlightthickness=0, 
    insertwidth=0, 
)
display.pack(expand=True, fill='both')


#List Layout Tombol

tombol_layout = [
    # Baris 1: 7, 8, 9, ÷
    {'label': '7', 'row': 1, 'col': 0, 'command': lambda: tambah_angka(7), 'style': BUTTON_COLOR},
    {'label': '8', 'row': 1, 'col': 1, 'command': lambda: tambah_angka(8), 'style': BUTTON_COLOR},
    {'label': '9', 'row': 1, 'col': 2, 'command': lambda: tambah_angka(9), 'style': BUTTON_COLOR},
    {'label': '÷', 'row': 1, 'col': 3, 'command': lambda: tambah_angka('÷'), 'style': OPERATOR_COLOR},

    # Baris 2: 4, 5, 6, x
    {'label': '4', 'row': 2, 'col': 0, 'command': lambda: tambah_angka(4), 'style': BUTTON_COLOR},
    {'label': '5', 'row': 2, 'col': 1, 'command': lambda: tambah_angka(5), 'style': BUTTON_COLOR},
    {'label': '6', 'row': 2, 'col': 2, 'command': lambda: tambah_angka(6), 'style': BUTTON_COLOR},
    {'label': 'x', 'row': 2, 'col': 3, 'command': lambda: tambah_angka('x'), 'style': OPERATOR_COLOR},

    # Baris 3: 1, 2, 3, -
    {'label': '1', 'row': 3, 'col': 0, 'command': lambda: tambah_angka(1), 'style': BUTTON_COLOR},
    {'label': '2', 'row': 3, 'col': 1, 'command': lambda: tambah_angka(2), 'style': BUTTON_COLOR},
    {'label': '3', 'row': 3, 'col': 2, 'command': lambda: tambah_angka(3), 'style': BUTTON_COLOR},
    {'label': '-', 'row': 3, 'col': 3, 'command': lambda: tambah_angka('-'), 'style': OPERATOR_COLOR},

    # Baris 4: 0, ., +, = (di gambar '0' hanya 1 kolom)
    # Saya menambahkan tombol Clear 'C' di baris 4 kolom 0 untuk fungsionalitas, dan 0 di bawahnya.
    {'label': 'C', 'row': 4, 'col': 0, 'command': operasikan_clear, 'style': OPERATOR_COLOR},
    {'label': '0', 'row': 4, 'col': 1, 'command': lambda: tambah_angka(0), 'style': BUTTON_COLOR},
    {'label': '.', 'row': 4, 'col': 2, 'command': lambda: tambah_angka('.'), 'style': BUTTON_COLOR},
    {'label': '+', 'row': 4, 'col': 3, 'command': lambda: tambah_angka('+'), 'style': OPERATOR_COLOR},
    
    # Baris 5: Tombol '=' besar
    {'label': '=', 'row': 5, 'col': 0, 'command': operasikan_hitung, 'style': EQUAL_COLOR, 'colspan': 4},
]

#  Membuat Tombol-tombol 

for btn in tombol_layout:
    r = btn['row']
    c = btn['col']
    colspan = btn.get('colspan', 1)
    
    # Membuat object Button
    button = tk.Button(
        root, 
        text=btn['label'], 
        command=btn['command'],
        bg=btn['style'], 
        fg=TEXT_COLOR, 
        font=BUTTON_FONT, 
        bd=5, # Border lebih tebal untuk efek 3D
        relief=tk.RAISED, # Efek 3D timbul
        activebackground=btn['style'],
        highlightthickness=0 
    )
    
    # Menempatkan tombol
    button.grid(row=r, column=c, columnspan=colspan, sticky="nsew", padx=4, pady=4)

#  Konfigurasi Grid Weight 

# tombol-tombol menyesuaikan ukuran baris dan kolom
for i in range(1, 6): # Baris tombol 1 sampai 5
    root.grid_rowconfigure(i, weight=1)

for i in range(4): # Kolom 0 sampai 3
    root.grid_columnconfigure(i, weight=1)
    
# Baris Display (Row 0)
root.grid_rowconfigure(0, weight=0) 

# Memulai main loop
root.mainloop()