import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
from mysql.connector import Error

#  1. KONFIGURASI DATABASE TETAP (Host, Port, Nama DB) 
# Hanya host, database, dan port yang tetap. User dan password akan dinamis dari input login.
DB_STATIC_CONFIG = {
    'host': 'localhost',
    'database': 'db_mahasiswa',
    'port': 3306
}

#  2. CLASS UTAMA APLIKASI TKINTER 

class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Informasi Mahasiswa")
        self.root.geometry("800x600")
        
        # Variabel untuk menampung koneksi database yang berhasil diautentikasi
        self.db_conn = None
        self.cursor = None
        
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

        self.root.title("Aplikasi CRUD Data Mahasiswa")
        
        #  Bagian Input Data 
        input_frame = ttk.LabelFrame(self.current_frame, text="Input Data Mahasiswa", padding=10)
        input_frame.pack(padx=20, pady=10, fill='x')

        labels = ["NPM:", "Nama:", "Alamat:"]
        self.entries = {}
        for i, label_text in enumerate(labels):
            tk.Label(input_frame, text=label_text).grid(row=i, column=0, padx=5, pady=5, sticky='w')
            entry = tk.Entry(input_frame, width=40)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky='ew')
            self.entries[label_text.replace(":", "")] = entry

        #  Bagian Tombol Operasi 
        button_frame = ttk.Frame(self.current_frame, padding=10)
        button_frame.pack(padx=20, pady=5, fill='x')

        ttk.Button(button_frame, text="Tambah Data", command=self.add_data).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Lihat Data", command=self.fetch_data).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Ubah Data", command=self.update_data).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Hapus Data", command=self.delete_data).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Logout", command=self.logout).pack(side=tk.RIGHT, padx=5)

        #  Bagian Tampilan Data (Treeview) 
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Arial', 10, 'bold'))
        
        columns = ("npm", "namaMahasiswa", "alamat")
        self.tree = ttk.Treeview(self.current_frame, columns=columns, show='headings')
        self.tree.pack(padx=20, pady=10, fill='both', expand=True)

        self.tree.heading("npm", text="NPM")
        self.tree.heading("namaMahasiswa", text="Nama Mahasiswa")
        self.tree.heading("alamat", text="Alamat")

        # Mengatur lebar kolom
        self.tree.column("npm", width=120, anchor='center')
        self.tree.column("namaMahasiswa", width=250, anchor='w')
        self.tree.column("alamat", width=300, anchor='w')
        
        # Bind event klik pada Treeview untuk mengisi form Update
        self.tree.bind('<<TreeviewSelect>>', self.load_selected_data)
        
        # Load data awal saat halaman CRUD dimuat
        self.fetch_data()
        
    def logout(self):
        """Menutup koneksi database dan kembali ke halaman login."""
        if self.db_conn and self.db_conn.is_connected():
            self.db_conn.close()
            self.db_conn = None
            self.cursor = None
            messagebox.showinfo("Logout", "Anda telah berhasil logout.")
        self.create_login_page()


    #  5. FUNGSI CRUD 

    def fetch_data(self):
        """Mengambil data dari database dan menampilkannya di Treeview."""
        if not self.db_conn or not self.db_conn.is_connected():
            messagebox.showerror("Error", "Koneksi database tidak aktif.")
            return

        try:
            self.cursor.execute("SELECT * FROM mahasiswa")
            records = self.cursor.fetchall()

            # Menghapus data lama di Treeview
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Memasukkan data baru
            for row in records:
                self.tree.insert('', tk.END, values=row)

        except Error as e:
            messagebox.showerror("Error Baca Data", f"Gagal mengambil data: {e}")

    def add_data(self):
        """Menambahkan data baru ke database."""
        if not self.db_conn or not self.db_conn.is_connected():
            messagebox.showerror("Error", "Koneksi database tidak aktif.")
            return

        try:
            npm = self.entries['NPM'].get().strip()
            nama = self.entries['Nama'].get().strip()
            alamat = self.entries['Alamat'].get().strip()

            if not npm or not nama or not alamat:
                messagebox.showwarning("Input Kurang", "Semua kolom harus diisi.")
                return
            
            try:
                npm_int = int(npm)
            except ValueError:
                messagebox.showwarning("Input Invalid", "NPM harus berupa angka.")
                return

            query = "INSERT INTO mahasiswa (npm, namaMahasiswa, alamat) VALUES (%s, %s, %s)"
            data = (npm_int, nama, alamat)
            
            self.cursor.execute(query, data)
            self.db_conn.commit()
            messagebox.showinfo("Sukses", "Data berhasil ditambahkan.")
            
            self.fetch_data()
            for entry in self.entries.values():
                entry.delete(0, tk.END)

        except Error as e:
            if e.errno == 1062:
                 messagebox.showerror("Gagal", f"NPM '{npm}' sudah terdaftar. Silakan gunakan NPM lain.")
            else:
                messagebox.showerror("Gagal", f"Gagal menambahkan data: {e}")

    def load_selected_data(self, event):
        """Memuat data dari baris Treeview yang dipilih ke kolom input."""
        selected_item = self.tree.focus()
        if not selected_item:
            return

        values = self.tree.item(selected_item, 'values')
        
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        
        self.entries['NPM'].insert(0, values[0])
        self.entries['Nama'].insert(0, values[1])
        self.entries['Alamat'].insert(0, values[2])
        
        self.old_npm = values[0] 

    def update_data(self):
        """Mengubah data mahasiswa yang ada di database."""
        if not self.db_conn or not self.db_conn.is_connected():
            messagebox.showerror("Error", "Koneksi database tidak aktif.")
            return

        try:
            if not hasattr(self, 'old_npm'):
                 messagebox.showwarning("Peringatan", "Pilih data di tabel yang ingin diubah terlebih dahulu.")
                 return

            npm_baru = self.entries['NPM'].get().strip()
            nama = self.entries['Nama'].get().strip()
            alamat = self.entries['Alamat'].get().strip()

            if not npm_baru or not nama or not alamat:
                messagebox.showwarning("Input Kurang", "Semua kolom harus diisi.")
                return

            try:
                npm_baru_int = int(npm_baru)
                old_npm_int = int(self.old_npm)
            except ValueError:
                messagebox.showwarning("Input Invalid", "NPM harus berupa angka.")
                return
            
            query = "UPDATE mahasiswa SET npm=%s, namaMahasiswa=%s, alamat=%s WHERE npm=%s"
            data = (npm_baru_int, nama, alamat, old_npm_int)
            
            self.cursor.execute(query, data)
            self.db_conn.commit()
            
            if self.cursor.rowcount > 0:
                messagebox.showinfo("Sukses", f"Data NPM '{self.old_npm}' berhasil diupdate.")
            else:
                messagebox.showwarning("Gagal", "Tidak ada data yang diubah atau NPM tidak ditemukan.")

            self.fetch_data()
            delattr(self, 'old_npm') 
            for entry in self.entries.values():
                entry.delete(0, tk.END)

        except Error as e:
            messagebox.showerror("Gagal", f"Gagal mengupdate data: {e}")

    def delete_data(self):
        """Menghapus data mahasiswa dari database."""
        if not self.db_conn or not self.db_conn.is_connected():
            messagebox.showerror("Error", "Koneksi database tidak aktif.")
            return
            
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih data di tabel yang ingin dihapus.")
            return
            
        values = self.tree.item(selected_item, 'values')
        npm_to_delete = values[0]
        
        if messagebox.askyesno("Konfirmasi Hapus", f"Anda yakin ingin menghapus data NPM {npm_to_delete}?"):
            try:
                npm_int = int(npm_to_delete)
                query = "DELETE FROM mahasiswa WHERE npm=%s"
                data = (npm_int,)
                
                self.cursor.execute(query, data)
                self.db_conn.commit()
                
                messagebox.showinfo("Sukses", f"Data NPM {npm_to_delete} berhasil dihapus.")
                self.fetch_data()
                
                for entry in self.entries.values():
                    entry.delete(0, tk.END)

            except Error as e:
                messagebox.showerror("Gagal", f"Gagal menghapus data: {e}")
            except ValueError:
                messagebox.showerror("Error", "NPM tidak valid.")


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