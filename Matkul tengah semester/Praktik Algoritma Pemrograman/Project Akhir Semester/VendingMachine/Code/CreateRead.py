import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk 
import io
import sys
from tkinter import filedialog



#  1. KONFIGURASI DATABASE TETAP (Host, Port, Nama DB) 
# Hanya host, database, dan port yang tetap. User dan password akan dinamis dari input login.
DB_STATIC_CONFIG = {
    'host': 'localhost',
    'database': 'db_vm',
    'port': 3306
}





class CreateRead:

    """Class yang menangani semua interaksi dengan database (CRUD)."""
    
    def __init__(self, app_instance):
        # Menyimpan referensi ke instance CRUDApp untuk mengakses koneksi dan widget GUI.
        self.app = app_instance

    def fetch_data(self):
        """Mengambil data dari database dan menampilkannya di Treeview."""
        if not self.app.db_conn or not self.app.db_conn.is_connected():
            messagebox.showerror("Error", "Koneksi database tidak aktif.")
            return

        try:
            self.app.cursor.execute("SELECT * FROM produk")
            records = self.app.cursor.fetchall()

            # Menghapus data lama di Treeview
            for item in self.app.tree.get_children():
                self.app.tree.delete(item)

            # Memasukkan data baru
            for row in records:
                # Mengganti data biner gambar (mediumblob) dengan string placeholder 
                # karena Treeview tidak bisa menampilkan gambar
                row_list = list(row)
                row_list[4] = "[BLOB Data]" if row_list[4] else "[No Image]"
                self.app.tree.insert('', tk.END, values=row)

        except Error as e:
            messagebox.showerror("Error Baca Data", f"Gagal mengambil data: {e}")

    def Create(self):
        """Menambahkan data baru ke database."""
        if not self.app.db_conn or not self.app.db_conn.is_connected():
            messagebox.showerror("Error", "Koneksi database tidak aktif.")
            return

        try:
            id_produk = self.app.entries['ID'].get().strip()
            nama_produk = self.app.entries['Nama Produk'].get().strip()
            harga = self.app.entries['Harga'].get().strip()
            stok_produk = self.app.entries['Stok'].get().strip()

            if not id_produk or not nama_produk or not harga or not stok_produk:
                messagebox.showwarning("Input Kurang", "Semua kolom harus diisi.")
                return
            
            try:
                id_produk_int = int(id_produk)
                harga_num = float(harga)
                stok_produk_num = int(stok_produk)
            except ValueError:
                messagebox.showwarning("Input Invalid", "ID harus berupa angka.")
                return
            

            # Dapatkan data gambar biner yang sudah disimpan setelah browse
            gambar_produk_bin = self.app.selected_image_data

            query = "INSERT INTO produk (id_produk, nama_produk, harga, stok_produk, gambar_produk) VALUES (%s, %s, %s, %s, %s)"
            data = (id_produk_int, nama_produk, harga_num, stok_produk_num, gambar_produk_bin)
            
            self.app.cursor.execute(query, data)
            self.app.db_conn.commit()
            messagebox.showinfo("Sukses", "Data berhasil ditambahkan.")
            
            self.fetch_data()
            for entry in self.app.entries.values():
                entry.delete(0, tk.END)
            # Panggil function untuk reset preview gambar
            self.app.reset_image_preview()

        except Error as e:
            if e.errno == 1062:
                 messagebox.showerror("Gagal", f"ID '{id_produk}' sudah terdaftar. Silakan gunakan ID lain.")
            else:
                messagebox.showerror("Gagal", f"Gagal menambahkan data: {e}")

    def Read(self, event):
        """Memuat data dari baris Treeview yang dipilih ke kolom input."""
        selected_item = self.app.tree.focus()
        if not selected_item:
            return

        # Ambil ID produk dari kolom pertama Treeview (0)
        id_produk = self.app.tree.item(selected_item, 'values')[0]

        # Reset preview gambar dan data gambar yang ada
        self.app.reset_image_preview()

        values = self.app.tree.item(selected_item, 'values')
        
        for entry in self.app.entries.values():
            entry.delete(0, tk.END)


        try:
            self.app.entries['ID'].insert(0, values[0])
            self.app.entries['Nama Produk'].insert(0, values[1])
            self.app.entries['Harga'].insert(0, values[2])
            self.app.entries['Stok'].insert(0, values[3])

            # Tampilkan gambar jika ada
            image_blob = values[4]
            if image_blob:
                self.app.display_image_blob(image_blob)
            
            self.app.old_id_produk = values[0]  #############
        except IndexError:
            messagebox.showwarning("Data Error", "Data dari baris yang dipilih tidak lengkap.")
        except Error as e:
            messagebox.showerror("Database Error", f"Gagal mengambil detail produk: {e}")




###################################################################


# Ukuran preview gambar
IMAGE_PREVIEW_SIZE = (100, 100)

class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Informasi Mahasiswa")
        self.root.geometry("800x650")
        
        # Variabel untuk menampung koneksi database yang berhasil diautentikasi
        self.db_conn = None
        self.cursor = None

        # Variabel GUI
        self.entries = {}
        self.tree = None
        self.old_id_produk = None 
        
        # Variabel Gambar
        self.selected_image_data = None  # Menyimpan data biner gambar yang akan disimpan
        self.image_display_ref = None    # Referensi ke objek gambar Tkinter (PENTING untuk mencegah garbage collection)
        self.image_preview_label = None  # Label tempat gambar ditampilkan

        # Variabel untuk Instantiate CreateRead Class
        self.CreateandRead = CreateRead(self)
        
        # Membuat frame yang akan menampung semua konten (Login atau CRUD)
        self.current_frame = tk.Frame(root)
        self.current_frame.pack(fill='both', expand=True)
        
        self.create_login_page()

    #  3. HALAMAN LOGIN 
    
    def create_login_page(self):
        """Membangun antarmuka halaman Login."""
        
        # Membersihkan/refreah frame yang ada
        for widget in self.current_frame.winfo_children():
            widget.destroy()

        login_frame = ttk.Frame(self.current_frame, padding="50 50 50 50")
        login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Label dan Entry Box
        username_label = tk.Label(login_frame, text='Username:', font=('Arial', 12))
        password_label = tk.Label(login_frame, text='Password :', font=('Arial', 12))

        self.user_box = tk.Entry(login_frame, font=('Arial', 12))
        self.pass_box = tk.Entry(login_frame, show='*', font=('Arial', 12))
        
        # Tombol Login
        login_button = tk.Button(login_frame, text='Login', command=self.login_attempt, font=('Arial', 12, 'bold'), bg='lightblue')

        # Penempatan menggunakan grid
        username_label.grid(row=0, column=0, pady=10, padx=10, sticky='w')
        password_label.grid(row=1, column=0, pady=10, padx=10, sticky='w')
        self.user_box.grid(row=0, column=1, pady=10, padx=10)
        self.pass_box.grid(row=1, column=1, pady=10, padx=10)
        login_button.grid(row=2, column=1, pady=20, sticky='e')

    def login_attempt(self):
        """Mencoba koneksi ke MySQL menggunakan kredensial yang dimasukkan pengguna (Otentikasi Database)."""
        username = self.user_box.get()
        password = self.pass_box.get()
        
        try:
            # Mencoba membuat koneksi menggunakan kredensial pengguna
            self.db_conn = mysql.connector.connect(
                host=DB_STATIC_CONFIG['host'],
                database=DB_STATIC_CONFIG['database'],
                user=username,  # Kredensial dinamis
                password=password, # Kredensial dinamis
                port=DB_STATIC_CONFIG['port']
            )
            
            # Jika koneksi berhasil, otentikasi sukses
            if self.db_conn.is_connected():
                self.cursor = self.db_conn.cursor()
                messagebox.showinfo("Login Sukses", f"Berhasil login sebagai user '{username}'.")
                self.create_main_crud_page()
            else:
                messagebox.showerror("Login Gagal", "Gagal terhubung ke database.")

        except Error as e:
            # Jika ada error koneksi (misalnya Error 1045 Access denied), login dianggap gagal
            if e.errno == 1045:
                messagebox.showerror("Login Gagal", "Username atau Password database salah!")
            else:
                messagebox.showerror("Login Gagal", f"Gagal terhubung ke database. Pastikan Laragon/XAMPP berjalan. Error: {e}")

    #  4. HALAMAN UTAMA CRUD 

    def create_main_crud_page(self):
        """Membangun antarmuka CRUD utama."""
        for widget in self.current_frame.winfo_children():
            widget.destroy()

        self.root.title("Tampilan CRUD Vending Machine")
        
        #  Bagian Input Data 
        input_frame = ttk.LabelFrame(self.current_frame, text="Input Data Produk", padding=10)
        input_frame.pack(padx=20, pady=10, fill='x')

        labels = ["ID:", "Nama Produk:", "Harga:", "Stok"]
        self.entries = {}
        for i, label_text in enumerate(labels):
            tk.Label(input_frame, text=label_text).grid(row=i, column=0, padx=5, pady=5, sticky='w')
            entry = tk.Entry(input_frame, width=40)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky='ew')
            self.entries[label_text.replace(":", "")] = entry

        # Input Gambar
        image_label = tk.Label(input_frame, text="Gambar Produk:")
        image_label.grid(row=len(labels), column=0, padx=5, pady=5, sticky='w')

        # Tombol Pilih Gambar
        image_button = ttk.Button(input_frame, text="Pilih Gambar (.jpg/.png)", command=self.browse_image)
        image_button.grid(row=len(labels), column=1, padx=5, pady=5, sticky='w')
        
        # Label Pratinjau Gambar
        self.image_preview_label = tk.Label(
            input_frame, 
            text='[No Image Selected]',
            width=IMAGE_PREVIEW_SIZE[0] // 8, # menjadikan IMAGE_PREVIEW_SIZE[0] sebagai width 
            height=IMAGE_PREVIEW_SIZE[1] // 16, # menjadikan IMAGE_PREVIEW_SIZE[0] sebagai height
            relief=tk.SUNKEN
        )
        self.image_preview_label.grid(row=len(labels), column=2, rowspan=2, padx=10, pady=5)
        self.reset_image_preview()

        #  Bagian Tombol Operasi 
        button_frame = ttk.Frame(self.current_frame, padding=10)
        button_frame.pack(padx=20, pady=5, fill='x')

        ttk.Button(button_frame, text="Tambah Data", command=self.CreateandRead.Create).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Lihat Data", command=self.CreateandRead.fetch_data).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Logout", command=self.logout).pack(side=tk.RIGHT, padx=5)

        #  Bagian Tampilan Data (Treeview) 
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial', 10, 'bold'))
        
        columns = ("id_produk", "nama_produk", "harga","stok_produk", "gambar_produk")
        self.tree = ttk.Treeview(self.current_frame, columns=columns, show='headings')
        self.tree.pack(padx=20, pady=10, fill='both', expand=True)

        self.tree.heading("id_produk", text="ID")
        self.tree.heading("nama_produk", text="Nama Produk")
        self.tree.heading("harga", text="Harga")
        self.tree.heading("stok_produk", text="Stok")
        self.tree.heading("gambar_produk", text="Gambar (BLOB)")

        # Mengatur lebar kolom
        self.tree.column("id_produk", width=120, anchor='center')
        self.tree.column("nama_produk", width=250, anchor='w')
        self.tree.column("harga", width=300, anchor='w')
        self.tree.column("stok_produk", width=250, anchor='w')
        self.tree.column("gambar_produk", width=150, anchor='center')

        # Bind event klik pada Treeview untuk mengisi form Update
        self.tree.bind('<<TreeviewSelect>>', self.CreateandRead.Read)
        
        # Load data awal saat halaman CRUD dimuat
        self.CreateandRead.fetch_data()
        
    def logout(self):
        """Menutup koneksi database dan kembali ke halaman login."""
        if self.db_conn and self.db_conn.is_connected():
            self.db_conn.close()
            self.db_conn = None
            self.cursor = None
            messagebox.showinfo("Logout", "Anda telah berhasil logout.")
        self.create_login_page()



    #----------------Function/Method untuk gambr--------------------#
    
    def reset_image_preview(self):
        """Mereset data biner yang dipilih dan label pratinjau."""
        self.selected_image_data = None
        if self.image_preview_label:
            self.image_preview_label.config(image='', text='[No Image Selected]')
            self.image_display_ref = None

    def display_image_blob(self, image_blob):
        """Menampilkan data blob gambar di label pratinjau."""
        try:
            image = Image.open(io.BytesIO(image_blob))
            image.thumbnail(IMAGE_PREVIEW_SIZE)
            tk_image = ImageTk.PhotoImage(image)
            
            self.image_preview_label.config(image=tk_image, text='')
            self.image_display_ref = tk_image # Simpan referensi
        except Exception as e:
            self.image_preview_label.config(image='', text=f"[Display Error: {e}]")
            self.image_display_ref = None

    def browse_image(self):
        """Membuka dialog file, membaca gambar, dan menampilkan pratinjau."""
        filetypes = [
            ("Image files", "*.jpg *.jpeg *.png"),
            ("All files", "*.*")
        ]
        filepath = filedialog.askopenfilename(
            title="Pilih Gambar Produk",
            filetypes=filetypes
        )
        
        if filepath:
            try:
                # Baca file dalam mode biner
                with open(filepath, 'rb') as f:
                    image_data = f.read()
                
                # Simpan data biner untuk operasi Create
                self.selected_image_data = image_data
                
                # Tampilkan pratinjau
                self.display_image_blob(image_data)
                
            except Exception as e:
                messagebox.showerror("Error File", f"Gagal membaca file gambar: {e}")
                self.reset_image_preview()




#####################################################################

if __name__ == "__main__":
    # Inisialisasi Root Window
    root = tk.Tk()
    
    # Membuat instance aplikasi
    app = CRUDApp(root)
    
    # Jalankan loop utama Tkinter
    root.mainloop()

    # Pastikan koneksi ditutup saat aplikasi keluar
    if app.db_conn and app.db_conn.is_connected():
        app.db_conn.close()