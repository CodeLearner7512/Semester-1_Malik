from tkinter import *
import tkinter.messagebox as mb
import hashlib
import mysql.connector

class UpdateDelete:

    @staticmethod
    def koneksi():
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_simpeg',
            port=3306
        )

    def __init__(self):
        self.root = Tk()
        self.root.title("Update Delete Data Barang")
        self.root.resizable(False, False)
        self.root.eval('tk::PlaceWindow . center')

        frameUtama = Frame(self.root, bd=10)
        frameUtama.pack(fill=BOTH, expand=YES)

        frData = Frame(frameUtama, bd=5)
        frData.pack(fill=BOTH, expand=YES)

        Label(frData, text='Nama User').grid(row=0, column=0, sticky=W)
        self.entUser = Entry(frData)
        self.entUser.grid(row=0, column=1)

        Label(frData, text='Password').grid(row=1, column=0, sticky=W)
        self.entPass = Entry(frData, show='*')
        self.entPass.grid(row=1, column=1)

        frTombol = Frame(frameUtama, bd=5)
        frTombol.pack(fill=BOTH, expand=YES)

        Button(frTombol, text='Batal', command=self.root.destroy).pack(side=LEFT, fill=BOTH, expand=YES)
        Button(frTombol, text='Login', command=self.ProsesLogin).pack(side=LEFT, fill=BOTH, expand=YES)

        self.root.mainloop()

    def ProsesLogin(self):
        namaUser = self.entUser.get().strip()
        password = self.entPass.get()

        if not namaUser:
            mb.showerror('Login Gagal', 'Username tidak boleh kosong', parent=self.root)
            return

        if not password:
            mb.showerror('Login Gagal', 'Password tidak boleh kosong', parent=self.root)
            return

        password = hashlib.md5(password.encode()).hexdigest()

        conn = self.koneksi()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ms_user WHERE namaUser=%s AND password=%s", (namaUser, password))
        hasil = cursor.fetchall()
        cursor.close()
        conn.close()

        if not hasil:
            mb.showerror('Login Gagal', 'Nama user atau password salah.', parent=self.root)
            return

        for row in hasil:
            if row[3] == "Aktif":
                mb.showinfo("Login Berhasil", "Selamat, login berhasil.")
                self.root.withdraw()
                self.Aplikasi()
                return

        mb.showerror("Login Gagal", "User tidak aktif.", parent=self.root)

    def Aplikasi(self):
        app = Toplevel(self.root)
        app.title('Aplikasi')
        app.geometry('300x400')
        app.resizable(False, False)
        app.configure(background='Blue')

        Label(app, text='testqwq', font=('times new roman', 12), bg='Blue', fg='white').pack(pady=20)
        Button(app, text='Update Data', command=self.updatedata).pack(pady=10)
        Button(app, text='Delete Data', command=self.deletedata).pack(pady=10)
        Button(app, text='Logout', command=lambda: self.Logout(app)).pack(pady=10)
    
    def Logout(self, appwindow):
        appwindow.destroy()
        self.root.deiconify()

    def updatedata(self):
        conn = self.koneksi()
        cursor = conn.cursor()

        key = input("ID Barang: ")
        nama = input("Nama Barang: ")
        harga = input("Harga Barang: ")
        stok = input("Stok Barang: ")
        gambar = input("Gambar Barang: ")

        query = "UPDATE barang SET nama=%s, harga=%s, stok=%s, gambar=%s WHERE id=%s"

        cursor.execute(query, (nama, harga, stok, gambar, key))
        conn.commit()
        conn.close()
        print("Data berhasil diupdate")

    def deletedata(self):
        conn = self.koneksi()
        cursor = conn.cursor()

        key = input("ID Barang yang akan dihapus: ")

        query = "DELETE FROM barang WHERE id=%s"
        cursor.execute(query, (key,))
        conn.commit()
        conn.close()
        print("Data berhasil dihapus")

UpdateDelete()
