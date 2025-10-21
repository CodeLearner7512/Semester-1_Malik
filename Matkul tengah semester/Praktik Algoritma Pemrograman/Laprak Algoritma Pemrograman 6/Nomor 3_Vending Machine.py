import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Vending Machine Penjualan Minuman")
window.configure(bg="#292b2c")

# Data produk dan harga
produk = {
    "Teh Botol": 5000,
    "Air Mineral": 3000,
    "Kopi Hitam": 7000,
    "Susu Coklat": 8000,
    "Jus Jeruk": 9000
}

# Pecahan uang yang diterima
pecahan_uang = [1000, 2000, 5000, 10000, 20000, 50000, 100000]

# Variabel global
total_harga = 0
total_uang = 0
keranjang = []

# FRAME utama
frame_produk = tk.Frame(window, bg="#292b2c")
frame_produk.pack(pady=10)

frame_uang = tk.Frame(window, bg="#292b2c")
frame_uang.pack(pady=10)

# FRAME untuk log pembelian (dengan scrollbar)
frame_log = tk.Frame(window, bg="#292b2c")
frame_log.pack(pady=10)

log_text = tk.Text(frame_log, width=50, height=10, bg="#1c1e1f", fg="white", state="disabled", wrap="word")
log_text.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame_log, command=log_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
log_text.config(yscrollcommand=scrollbar.set)

# Fungsi bantu
def log(msg):
    """Menambahkan teks ke area log tanpa memperbesar window"""
    log_text.config(state="normal")
    log_text.insert(tk.END, msg + "\n")
    log_text.config(state="disabled")
    log_text.see(tk.END)

def pilih_produk(nama):
    global total_harga
    harga = produk[nama]
    keranjang.append((nama, harga))
    total_harga += harga
    log(f"Produk dipilih: {nama} - Rp{harga:,}")

def masukkan_uang(nilai):
    global total_uang
    total_uang += nilai
    log(f"Uang dimasukkan: Rp{nilai:,}")

def Checkout():
    if not keranjang:
        messagebox.showinfo("Info", "Belum ada produk yang dipilih.")
        return
    log("\n=== Checkout ===")
    for nama, harga in keranjang:
        log(f"{nama} - Rp{harga:,}")
    log(f"Total harga: Rp{total_harga:,}")
    log(f"Total uang: Rp{total_uang:,}")

def Submit():
    global total_harga, total_uang, keranjang
    if total_uang == 0:
        messagebox.showwarning("Peringatan", "Masukkan uang terlebih dahulu!")
        return
    if not keranjang:
        messagebox.showwarning("Peringatan", "Pilih minuman terlebih dahulu!")
        return

    if total_uang >= total_harga:
        kembalian = total_uang - total_harga
        messagebox.showinfo("Transaksi Sukses", f"Pembelian berhasil!\nKembalian Anda: Rp{kembalian:,}")
        log(f"Transaksi selesai. Kembalian: Rp{kembalian:,}\n")
    else:
        kekurangan = total_harga - total_uang
        messagebox.showwarning("Uang Kurang", f"Uang Anda kurang Rp{kekurangan:,}!")

def reset():
    global total_harga, total_uang, keranjang
    total_harga = 0
    total_uang = 0
    keranjang.clear()
    log_text.config(state="normal")
    log_text.delete(1.0, tk.END)
    log_text.config(state="disabled")
    log("Aplikasi telah direset.\n")

# Tombol produk
tk.Label(frame_produk, text="Pilih Produk:", bg="#292b2c", fg="white").pack()
for nama, harga in produk.items():
    tk.Button(frame_produk, text=f"{nama} (Rp{harga:,})", command=lambda n=nama: pilih_produk(n),
              bg="#007bff", fg="white", width=25).pack(pady=2)

# Tombol pecahan uang
tk.Label(frame_uang, text="Masukkan Uang:", bg="#292b2c", fg="white").pack()
for uang in pecahan_uang:
    tk.Button(frame_uang, text=f"Rp{uang:,}", command=lambda u=uang: masukkan_uang(u),
              bg="#28a745", fg="white", width=15).pack(pady=1)

# Tombol kontrol
tk.Button(window, text="Checkout", command=Checkout, bg="#ffc107", fg="black", width=15).pack(pady=0)
tk.Button(window, text="Submit", command=Submit, bg="#17a2b8", fg="white", width=15).pack(pady=0)
tk.Button(window, text="Reset", command=reset, bg="#dc3545", fg="white", width=15).pack(pady=0)

window.mainloop()
