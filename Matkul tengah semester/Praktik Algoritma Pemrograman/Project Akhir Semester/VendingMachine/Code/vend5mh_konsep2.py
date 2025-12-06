#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import io
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import mysql.connector
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets", "images")
os.makedirs(ASSETS_DIR, exist_ok=True)

# ---------- DB connection (MySQL primary, SQLite fallback) ----------
DB_TYPE = None
mysql_conn = None
mysql_cursor = None
sqlite_conn = None
sqlite_cursor = None
SQLITE_FILE = os.path.join(BASE_DIR, "vm_fallback.db")

def try_connect_mysql():
    global mysql_conn, mysql_cursor, DB_TYPE
    try:
        mysql_conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",     # sesuaikan bila ada password
            database="db_vm"
        )
        mysql_cursor = mysql_conn.cursor(dictionary=True)
        DB_TYPE = "mysql"
        return True
    except Exception:
        mysql_conn = None
        mysql_cursor = None
        DB_TYPE = None
        return False

def init_sqlite():
    global sqlite_conn, sqlite_cursor, DB_TYPE
    sqlite_conn = sqlite3.connect(SQLITE_FILE)
    sqlite_conn.row_factory = sqlite3.Row
    sqlite_cursor = sqlite_conn.cursor()
    DB_TYPE = "sqlite"
    sqlite_cursor.execute("""
        CREATE TABLE IF NOT EXISTS produk (
            id_produk INTEGER PRIMARY KEY,
            nama_produk TEXT,
            stok_produk INTEGER,
            harga NUMERIC,
            gambar_produk BLOB
        )
    """)
    sqlite_conn.commit()

def ensure_mysql_table():
    # create table with correct column names
    mysql_cursor.execute("""
        CREATE TABLE IF NOT EXISTS produk (
            nama_produk VARCHAR(255),
            id_produk INT PRIMARY KEY,
            stok_produk INT,
            harga DECIMAL(10,0),
            gambar_produk MEDIUMBLOB
        )
    """)
    mysql_conn.commit()

def ensure_db():
    ok = try_connect_mysql()
    if ok:
        ensure_mysql_table()
    else:
        init_sqlite()

def db_fetchall(query, params=()):
    if DB_TYPE == "mysql":
        mysql_cursor.execute(query, params)
        return mysql_cursor.fetchall()
    else:
        sqlite_cursor.execute(query, params)
        rows = sqlite_cursor.fetchall()
        return [dict(r) for r in rows]

def db_fetchone(query, params=()):
    if DB_TYPE == "mysql":
        mysql_cursor.execute(query, params)
        return mysql_cursor.fetchone()
    else:
        sqlite_cursor.execute(query, params)
        r = sqlite_cursor.fetchone()
        return dict(r) if r else None

def db_execute(query, params=()):
    if DB_TYPE == "mysql":
        mysql_cursor.execute(query, params)
        mysql_conn.commit()
    else:
        sqlite_cursor.execute(query, params)
        sqlite_conn.commit()

# ---------- DB helpers that follow your schema ----------
def get_all_produk():
    q = "SELECT id_produk, nama_produk, harga, stok_produk FROM produk ORDER BY id_produk"
    return db_fetchall(q)

def get_produk_by_id(id_produk):
    if DB_TYPE == "mysql":
        q = "SELECT id_produk, nama_produk, harga, stok_produk, gambar_produk FROM produk WHERE id_produk = %s"
        return db_fetchone(q, (id_produk,))
    else:
        q = "SELECT id_produk, nama_produk, harga, stok_produk, gambar_produk FROM produk WHERE id_produk = ?"
        return db_fetchone(q, (id_produk,))

def add_produk_db(id_produk, nama, stok, harga, gambar_blob):
    if DB_TYPE == "mysql":
        q = "INSERT INTO produk (nama_produk, id_produk, stok_produk, harga, gambar_produk) VALUES (%s, %s, %s, %s, %s)"
        db_execute(q, (nama, id_produk, stok, harga, gambar_blob))
    else:
        q = "INSERT INTO produk (nama_produk, id_produk, stok_produk, harga, gambar_produk) VALUES (?,?,?,?,?)"
        db_execute(q, (nama, id_produk, stok, harga, gambar_blob))

def update_produk_db(id_produk, nama, stok, harga, gambar_blob):
    if gambar_blob is None:
        if DB_TYPE == "mysql":
            q = "UPDATE produk SET nama_produk=%s, stok_produk=%s, harga=%s WHERE id_produk=%s"
            db_execute(q, (nama, stok, harga, id_produk))
        else:
            q = "UPDATE produk SET nama_produk=?, stok_produk=?, harga=? WHERE id_produk=?"
            db_execute(q, (nama, stok, harga, id_produk))
    else:
        if DB_TYPE == "mysql":
            q = "UPDATE produk SET nama_produk=%s, stok_produk=%s, harga=%s, gambar_produk=%s WHERE id_produk=%s"
            db_execute(q, (nama, stok, harga, gambar_blob, id_produk))
        else:
            q = "UPDATE produk SET nama_produk=?, stok_produk=?, harga=?, gambar_produk=? WHERE id_produk=?"
            db_execute(q, (nama, stok, harga, gambar_blob, id_produk))

def delete_produk_db(id_produk):
    if DB_TYPE == "mysql":
        q = "DELETE FROM produk WHERE id_produk = %s"
        db_execute(q, (id_produk,))
    else:
        q = "DELETE FROM produk WHERE id_produk = ?"
        db_execute(q, (id_produk,))

def decrement_stok(id_produk):
    if DB_TYPE == "mysql":
        q = "UPDATE produk SET stok_produk = stok_produk - 1 WHERE id_produk = %s"
        db_execute(q, (id_produk,))
    else:
        q = "UPDATE produk SET stok_produk = stok_produk - 1 WHERE id_produk = ?"
        db_execute(q, (id_produk,))

# ---------- blob helpers ----------
def file_to_blob(path):
    with open(path, "rb") as f:
        return f.read()

def blob_to_photoimage(blob, size=None):
    if not blob:
        return None
    try:
        img = Image.open(io.BytesIO(blob))
        if size:
            img = img.resize(size)
        return ImageTk.PhotoImage(img)
    except Exception:
        return None

# ---------- GUI ----------
# card sizes for grid
CARD_WIDTH = 150
CARD_HEIGHT = 200
IMAGE_SIZE = (150, 120)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Vending Machine")
        self.root.geometry("1024x680")
        self.frames = {}
        for F in (MenuFrame, ShopFrame, LoginAdminFrame, AdminPanelFrame):
            frame = F(self.root, self)
            self.frames[F.__name__] = frame
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.show_frame("MenuFrame")

    def show_frame(self, name):
        for f in self.frames.values():
            f.lower()
        self.frames[name].lift()
        frame = self.frames[name]
        if hasattr(frame, "on_show"):
            frame.on_show()

class MenuFrame(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        tk.Label(self, text="Selamat Datang di Vending Machine", font=("Arial", 20)).pack(pady=40)
        tk.Button(self, text="Belanja", width=20, height=2, command=lambda: app.show_frame("ShopFrame")).pack(pady=10)
        tk.Button(self, text="Admin", width=20, height=2, command=lambda: app.show_frame("LoginAdminFrame")).pack(pady=10)

class ShopFrame(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app

        # Left: product grid area (scrollable canvas)
        left_frame = tk.Frame(self, bg="#f6f6f6")
        left_frame.place(relx=0.02, rely=0.02, relwidth=0.64, relheight=0.96)

        title = tk.Label(left_frame, text="Produk", font=("Arial", 14), bg="#f6f6f6")
        title.pack(anchor="w", padx=10, pady=6)

        # Canvas with scrollbar for grid
        self.canvas_frame = tk.Frame(left_frame)
        self.canvas_frame.pack(fill="both", expand=True, padx=10, pady=6)
        self.canvas = tk.Canvas(self.canvas_frame, bg="#f6f6f6")
        self.vscroll = tk.Scrollbar(self.canvas_frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vscroll.set)
        self.vscroll.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.grid_frame = tk.Frame(self.canvas, bg="#f6f6f6")
        self.canvas.create_window((0,0), window=self.grid_frame, anchor="nw")
        self.grid_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Right: panel (uang, keypad, input code, beli)
        right = tk.Frame(self, bg="#ffffff")
        right.place(relx=0.68, rely=0.02, relwidth=0.3, relheight=0.96)

        tk.Label(right, text="Masukkan Uang", font=("Arial", 12), bg="#ffffff").pack(anchor="w", padx=10, pady=(12,0))
        self.entry_money = tk.Entry(right, font=("Arial", 20), justify="right")
        self.entry_money.pack(padx=10, pady=6, fill="x")

        # keypad layout (1 2 3 / 4 5 6 / 7 8 9 / < 0 C)
        keypad = tk.Frame(right, bg="#ffffff")
        keypad.pack(padx=10, pady=6)
        keys = [
            ("1",0,0),("2",0,1),("3",0,2),
            ("4",1,0),("5",1,1),("6",1,2),
            ("7",2,0),("8",2,1),("9",2,2),
            ("<",3,0),("0",3,1),("C",3,2)
        ]
        for (txt,r,c) in keys:
            btn = tk.Button(keypad, text=txt, width=6, height=2, command=(lambda t=txt: self.keypress(t)))
            btn.grid(row=r, column=c, padx=4, pady=4)

        tk.Label(right, text="Masukkan Kode Produk", font=("Arial", 12), bg="#ffffff").pack(anchor="w", padx=10, pady=(8,0))
        self.entry_code = tk.Entry(right, font=("Arial", 14))
        self.entry_code.pack(padx=10, pady=6, fill="x")

        self.btn_buy = tk.Button(right, text="Beli", bg="#4caf50", fg="white", command=self.do_buy)
        self.btn_buy.pack(padx=10, pady=8, fill="x")

        # result area
        self.result_label = tk.Label(right, text="", justify="left", anchor="w", bg="#ffffff")
        self.result_label.pack(padx=10, pady=6, fill="x")

        tk.Button(right, text="Kembali", command=lambda: app.show_frame("MenuFrame")).pack(side="bottom", pady=10)

        self.photo_cache = []
        self.on_show()

    def on_show(self):
        self.load_products()
        self.entry_money.delete(0, "end")
        self.entry_code.delete(0, "end")
        self.result_label.config(text="")

    def load_products(self):
        # clear grid_frame
        for w in self.grid_frame.winfo_children():
            w.destroy()
        self.photo_cache.clear()

        produk = get_all_produk()
        if not produk:
            tk.Label(self.grid_frame, text="Tidak ada produk", font=("Arial", 14), bg="#f6f6f6").pack(pady=10)
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
            return

        kolom = 3
        padx = 10
        pady = 10

        for i, p in enumerate(produk):
            idp = p['id_produk']
            nama = p['nama_produk']
            harga = p['harga']
            stok = p['stok_produk']
            full = get_produk_by_id(idp)
            blob = full.get("gambar_produk") if full else None

            card = tk.Frame(self.grid_frame, width=CARD_WIDTH, height=CARD_HEIGHT, bd=1, relief="solid", bg="white")
            card.grid(row=i//kolom, column=i%kolom, padx=padx, pady=pady)
            card.grid_propagate(False)

            # image
            if blob:
                try:
                    img = Image.open(io.BytesIO(blob))
                    img = img.resize(IMAGE_SIZE)
                    photo = ImageTk.PhotoImage(img)
                except Exception:
                    photo = None
            else:
                photo = None

            if photo:
                lbl_img = tk.Label(card, image=photo, bg="white")
                lbl_img.image = photo
                self.photo_cache.append(photo)
            else:
                placeholder = Image.new("RGB", IMAGE_SIZE, (220,220,220))
                photo_pl = ImageTk.PhotoImage(placeholder)
                lbl_img = tk.Label(card, image=photo_pl, bg="white")
                lbl_img.image = photo_pl
                self.photo_cache.append(photo_pl)

            lbl_img.pack(pady=(6,4))

            lbl_name = tk.Label(card, text=str(nama), bg="white", font=("Arial", 10, "bold"), wraplength=CARD_WIDTH-10, justify="center")
            lbl_name.pack()

            lbl_price = tk.Label(card, text=f"Rp {int(float(harga))}", bg="white", font=("Arial", 9))
            lbl_price.pack()

            lbl_stock = tk.Label(card, text=f"Stok: {stok}", bg="white", font=("Arial", 9))
            lbl_stock.pack()

            lbl_id = tk.Label(card, text=f"ID: {idp}", bg="white", font=("Arial", 9))
            lbl_id.pack(pady=(4,6))

        # update scrollregion
        self.grid_frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def keypress(self, key):
        if key == "C":
            self.entry_money.delete(0, "end")
        elif key == "<":
            s = self.entry_money.get()
            self.entry_money.delete(0, "end")
            self.entry_money.insert(0, s[:-1])
        else:
            # digit
            self.entry_money.insert("end", key)

    def do_buy(self):
        try:
            uang = int(self.entry_money.get())
        except:
            messagebox.showerror("Error", "Masukkan jumlah uang yang valid")
            return
        kode = self.entry_code.get().strip()
        if not kode.isdigit():
            messagebox.showerror("Error", "Masukkan kode produk (angka)")
            return
        idp = int(kode)
        prod = get_produk_by_id(idp)
        if not prod:
            messagebox.showerror("Error", "Produk tidak ditemukan")
            return
        harga = float(prod["harga"])
        stok = int(prod["stok_produk"])
        if stok <= 0:
            messagebox.showinfo("Stok Kosong", "Stok produk kosong")
            return
        if uang < harga:
            messagebox.showinfo("Saldo Kurang", f"Harga Rp {int(harga)}. Koin anda Rp {uang}")
            return
        kembalian = int(uang - harga)
        decrement_stok(idp)
        self.load_products()
        nota = f"Pembelian berhasil!\nProduk: {prod['nama_produk']}\nHarga: Rp {int(harga)}\nUang: Rp {uang}\nKembalian: Rp {kembalian}"
        self.result_label.config(text=nota)
        # clear inputs
        self.entry_money.delete(0, "end")
        self.entry_code.delete(0, "end")

class LoginAdminFrame(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        tk.Label(self, text="Login Admin", font=("Arial", 16)).pack(pady=20)
        frm = tk.Frame(self)
        frm.pack(pady=6)
        tk.Label(frm, text="Username:").grid(row=0, column=0, sticky="e")
        tk.Label(frm, text="Password:").grid(row=1, column=0, sticky="e")
        self.ent_user = tk.Entry(frm)
        self.ent_pass = tk.Entry(frm, show="*")
        self.ent_user.grid(row=0, column=1, padx=6, pady=6)
        self.ent_pass.grid(row=1, column=1, padx=6, pady=6)
        tk.Button(self, text="Login", width=12, command=self.do_login).pack(pady=10)
        tk.Button(self, text="Kembali", width=12, command=lambda: app.show_frame("MenuFrame")).pack()
        self.info = tk.Label(self, text="", fg="red")
        self.info.pack()

    def do_login(self):
        user = self.ent_user.get().strip()
        pw = self.ent_pass.get().strip()
        if user == "admin" and pw == "admin":
            self.app.show_frame("AdminPanelFrame")
        else:
            self.info.config(text="Username atau password salah")

class AdminPanelFrame(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        left = tk.Frame(self)
        right = tk.Frame(self)
        left.place(relx=0.02, rely=0.02, relwidth=0.48, relheight=0.96)
        right.place(relx=0.52, rely=0.02, relwidth=0.46, relheight=0.96)

        tk.Label(left, text="Manajemen Produk", font=("Arial", 14)).pack(anchor="w", padx=8, pady=6)
        self.listbox = tk.Listbox(left, height=18)
        self.listbox.pack(fill="both", padx=8)
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        btn_frame = tk.Frame(left)
        btn_frame.pack(pady=6)
        tk.Button(btn_frame, text="Tambah Baru", command=self.prepare_add).pack(side="left", padx=6)
        tk.Button(btn_frame, text="Hapus", command=self.do_delete).pack(side="left", padx=6)
        tk.Button(btn_frame, text="Refresh", command=self.load_list).pack(side="left", padx=6)

        tk.Label(right, text="Form Produk", font=("Arial", 12)).pack(anchor="w", padx=8, pady=6)
        frm = tk.Frame(right)
        frm.pack(padx=8, pady=6, fill="x")
        tk.Label(frm, text="ID:").grid(row=0, column=0, sticky="e")
        tk.Label(frm, text="Nama:").grid(row=1, column=0, sticky="e")
        tk.Label(frm, text="Harga:").grid(row=2, column=0, sticky="e")
        tk.Label(frm, text="Stok:").grid(row=3, column=0, sticky="e")
        tk.Label(frm, text="Gambar:").grid(row=4, column=0, sticky="e")

        self.ent_id = tk.Entry(frm)
        self.ent_nama = tk.Entry(frm)
        self.ent_harga = tk.Entry(frm)
        self.ent_stok = tk.Entry(frm)
        self.ent_gambar = tk.Entry(frm)

        self.ent_id.grid(row=0, column=1, padx=6, pady=4, sticky="we")
        self.ent_nama.grid(row=1, column=1, padx=6, pady=4, sticky="we")
        self.ent_harga.grid(row=2, column=1, padx=6, pady=4, sticky="we")
        self.ent_stok.grid(row=3, column=1, padx=6, pady=4, sticky="we")
        self.ent_gambar.grid(row=4, column=1, padx=6, pady=4, sticky="we")

        tk.Button(frm, text="Pilih Gambar", command=self.browse_image).grid(row=4, column=2, padx=4)

        tk.Button(right, text="Simpan / Update", bg="#2196f3", fg="white", command=self.save_or_update).pack(padx=8, pady=8, fill="x")
        tk.Button(right, text="Kembali", command=lambda: app.show_frame("MenuFrame")).pack(side="bottom", pady=12)

        # preview
        self.preview_label = tk.Label(right, bg="#eee", width=32, height=10)
        self.preview_label.pack(padx=8, pady=6)

        self.image_blob = None
        self.load_list()

    def load_list(self):
        self.listbox.delete(0, "end")
        for p in get_all_produk():
            self.listbox.insert("end", f"{p['id_produk']} - {p['nama_produk']} | Rp{p['harga']} | Stok:{p['stok_produk']}")

    def on_select(self, event):
        sel = self.listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        text = self.listbox.get(idx)
        idp = int(text.split(" - ")[0])
        prod = get_produk_by_id(idp)
        if not prod:
            return
        self.ent_id.delete(0, "end"); self.ent_id.insert(0, str(prod["id_produk"]))
        self.ent_nama.delete(0, "end"); self.ent_nama.insert(0, prod["nama_produk"])
        self.ent_harga.delete(0, "end"); self.ent_harga.insert(0, str(prod["harga"]))
        self.ent_stok.delete(0, "end"); self.ent_stok.insert(0, str(prod["stok_produk"]))
        self.ent_gambar.delete(0, "end")
        self.image_blob = prod.get("gambar_produk")
        if self.image_blob:
            photo = blob_to_photoimage(self.image_blob, size=(240,160))
            if photo:
                self.preview_label.config(image=photo, text="")
                self.preview_label.image = photo
                return
        self.preview_label.config(image="", text="No image")

    def prepare_add(self):
        self.ent_id.delete(0, "end")
        self.ent_nama.delete(0, "end")
        self.ent_harga.delete(0, "end")
        self.ent_stok.delete(0, "end")
        self.ent_gambar.delete(0, "end")
        self.image_blob = None
        self.preview_label.config(image="", text="")

    def browse_image(self):
        filepath = filedialog.askopenfilename(title="Pilih gambar", filetypes=[("Image files","*.png;*.jpg;*.jpeg;*.gif")])
        if not filepath:
            return
        try:
            with open(filepath, "rb") as f:
                self.image_blob = f.read()
            self.ent_gambar.delete(0, "end")
            self.ent_gambar.insert(0, os.path.basename(filepath))
            photo = blob_to_photoimage(self.image_blob, size=(240,160))
            if photo:
                self.preview_label.config(image=photo, text="")
                self.preview_label.image = photo
        except Exception as e:
            messagebox.showerror("Error", f"Gagal membaca gambar: {e}")

    def save_or_update(self):
        idv = self.ent_id.get().strip()
        nama = self.ent_nama.get().strip()
        try:
            harga = float(self.ent_harga.get().strip())
        except:
            messagebox.showerror("Error", "Harga harus angka")
            return
        try:
            stok = int(self.ent_stok.get().strip())
        except:
            messagebox.showerror("Error", "Stok harus angka")
            return
        if not idv or not nama:
            messagebox.showerror("Error", "ID dan nama wajib diisi")
            return
        id_int = int(idv)
        # add or update
        existing = get_produk_by_id(id_int)
        try:
            if existing:
                update_produk_db(id_int, nama, stok, harga, self.image_blob)
                messagebox.showinfo("OK", "Produk diupdate")
            else:
                add_produk_db(id_int, nama, stok, harga, self.image_blob)
                messagebox.showinfo("OK", "Produk ditambahkan")
            self.load_list()
            self.prepare_add()
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan ke database: {e}")

    def do_delete(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("Pilih", "Pilih produk yang akan dihapus")
            return
        idx = sel[0]
        text = self.listbox.get(idx)
        idp = int(text.split(" - ")[0])
        if messagebox.askyesno("Konfirmasi", "Hapus produk ini?"):
            try:
                delete_produk_db(idp)
                self.load_list()
                self.prepare_add()
                messagebox.showinfo("OK", "Produk dihapus")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal hapus: {e}")

# ---------- start ----------
def main():
    ensure_db()
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    try:
        if mysql_conn:
            mysql_conn.close()
    except:
        pass
    try:
        if sqlite_conn:
            sqlite_conn.close()
    except:
        pass

if __name__ == "__main__":
    main()
