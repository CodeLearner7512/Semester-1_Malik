import customtkinter as ctk

# Mengatur tampilan default CustomTkinter
ctk.set_appearance_mode("Dark") 
ctk.set_default_color_theme("dark-blue") 

# Fungsi-fungsi Kalkulator

def tambah_angka(angka):
    """Menambahkan angka/operator ke tampilan."""
    current = app.input_text.get()
    
    # Menghapus '0' awal atau 'Error' saat memulai input
    if current in ("Error", "0") and str(angka).isdigit() or current == "0" and str(angka) == '.':
        app.input_text.set(str(angka))
    elif current == "0" and not str(angka).isdigit() and str(angka) != '.':
        # Izinkan operator aritmatika dimasukkan setelah '0'
        app.input_text.set(current + str(angka))
    elif current != "Error":
        app.input_text.set(current + str(angka))

def operasikan_clear():
    """Mengosongkan tampilan, kembali ke '0'."""
    app.input_text.set("0")

def operasikan_hitung():
    """Menghitung ekspresi yang ada di tampilan."""
    try:
        ekspresi = app.input_text.get()
        # Mengganti simbol 'x' menjadi '*' dan '÷' menjadi '/'
        ekspresi = ekspresi.replace('x', '*').replace('÷', '/')
        
        # Evaluasi ekspresi
        hasil = str(eval(ekspresi))
        app.input_text.set(hasil)
    except ZeroDivisionError:
        app.input_text.set("Error")
    except Exception:
        app.input_text.set("Error")

# class Aplikasi Utama 

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Kalkulator Digital")
        self.geometry("300x420")
        self.resizable(False, False) 
        
        # Variabel untuk menampung teks yang ditampilkan
        self.input_text = ctk.StringVar(value="0") 

        
        # Skema Warna
        BODY_COLOR = "#3C3C3C" 
        BUTTON_COLOR = "#505050" 
        OPERATOR_COLOR = "#666666" 
        EQUAL_COLOR = "#FF9500" 
        TEXT_COLOR = "white"
        
        # Mengatur warna latar belakang frame utama 
        self.configure(fg_color=BODY_COLOR) 
        
        # Font-Family
        DISPLAY_FONT = ('Consolas', 32, 'bold') 
        BUTTON_FONT = ('Arial', 18)
        
        #  Tampilan/Display Kalkulator 
        
        # CTkEntry sudah memiliki corner_radius secara default
        display = ctk.CTkEntry(
            self, 
            textvariable=self.input_text, 
            font=DISPLAY_FONT, 
            width=280, 
            height=60, 
            justify='right', 
            fg_color="#C8C8C8", # Background
            text_color="#333333", # Warna teks
            border_width=0,
            corner_radius=10 # Sudut melengkung 
        )
        display.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="nsew")

        #  Layout Tombol 
        tombol_layout = [
            # Baris 1: 7, 8, 9, ÷
            {'label': '7', 'row': 1, 'col': 0, 'command': lambda: tambah_angka(7), 'color': BUTTON_COLOR},
            {'label': '8', 'row': 1, 'col': 1, 'command': lambda: tambah_angka(8), 'color': BUTTON_COLOR},
            {'label': '9', 'row': 1, 'col': 2, 'command': lambda: tambah_angka(9), 'color': BUTTON_COLOR},
            {'label': '÷', 'row': 1, 'col': 3, 'command': lambda: tambah_angka('÷'), 'color': OPERATOR_COLOR},

            # Baris 2: 4, 5, 6, x
            {'label': '4', 'row': 2, 'col': 0, 'command': lambda: tambah_angka(4), 'color': BUTTON_COLOR},
            {'label': '5', 'row': 2, 'col': 1, 'command': lambda: tambah_angka(5), 'color': BUTTON_COLOR},
            {'label': '6', 'row': 2, 'col': 2, 'command': lambda: tambah_angka(6), 'color': BUTTON_COLOR},
            {'label': 'x', 'row': 2, 'col': 3, 'command': lambda: tambah_angka('x'), 'color': OPERATOR_COLOR},

            # Baris 3: 1, 2, 3, -
            {'label': '1', 'row': 3, 'col': 0, 'command': lambda: tambah_angka(1), 'color': BUTTON_COLOR},
            {'label': '2', 'row': 3, 'col': 1, 'command': lambda: tambah_angka(2), 'color': BUTTON_COLOR},
            {'label': '3', 'row': 3, 'col': 2, 'command': lambda: tambah_angka(3), 'color': BUTTON_COLOR},
            {'label': '-', 'row': 3, 'col': 3, 'command': lambda: tambah_angka('-'), 'color': OPERATOR_COLOR},

            # Baris 4: 0, ., +, C (Saya pindahkan C ke sini agar 0 bisa lebih besar, tapi saya ikuti gambar)
            # Saya tambahkan tombol Clear (C) untuk fungsionalitas
            {'label': 'C', 'row': 4, 'col': 0, 'command': operasikan_clear, 'color': OPERATOR_COLOR},
            {'label': '0', 'row': 4, 'col': 1, 'command': lambda: tambah_angka(0), 'color': BUTTON_COLOR},
            {'label': '.', 'row': 4, 'col': 2, 'command': lambda: tambah_angka('.'), 'color': BUTTON_COLOR},
            {'label': '+', 'row': 4, 'col': 3, 'command': lambda: tambah_angka('+'), 'color': OPERATOR_COLOR},
            
            # Baris 5: Tombol '=' besar
            {'label': '=', 'row': 5, 'col': 0, 'command': operasikan_hitung, 'color': EQUAL_COLOR, 'colspan': 4},
        ]
        
        #  Membuat Tombol-tombol 

        for btn in tombol_layout:
            r = btn['row']
            c = btn['col']
            colspan = btn.get('colspan', 1)
            
            # Membuat objek CTkButton
            button = ctk.CTkButton(
                self, 
                text=btn['label'], 
                command=btn['command'],
                fg_color=btn['color'], # Warna latar belakang
                text_color=TEXT_COLOR, # Warna teks
                font=BUTTON_FONT, 
                corner_radius=8, # Sudut melengkung untuk tombol
                height=50,
                hover_color=OPERATOR_COLOR if btn['label'] != '=' else EQUAL_COLOR
            )
            
            # Menempatkan tombol
            button.grid(row=r, column=c, columnspan=colspan, sticky="nsew", padx=4, pady=4)

        #  Konfigurasi Grid Weight 

        for i in range(1, 6): # Baris tombol 1 sampai 5
            self.grid_rowconfigure(i, weight=1)

        for i in range(4): # Kolom 0 sampai 3
            self.grid_columnconfigure(i, weight=1)
            
        # Baris Display (Row 0)
        self.grid_rowconfigure(0, weight=0) 

#  Menjalankan Aplikasi secara mainloop
if __name__ == "__main__":
    app = App()
    app.mainloop()