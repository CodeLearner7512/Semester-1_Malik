# merged_apps.py
import threading
import tkinter as tk
from tkinter import messagebox

# === Program 1: Bonus Pembelian ===
def bonus_pembelian():
    root = tk.Tk()
    root.title("Bonus Pembelian")
    root.configure(background='#292b2c')

    # Variabel, list, dan dictionary (local to function)
    daftarPembelian = []
    button_items = [
        'RTX 5090',
        'Mouse',
        'SanDisk 64 GB',
        'Keyboard',
        'Ethernet-to-USB',
        'Charger 12V'
    ]

    daftarHarga = {
        'RTX 5090': 60000000,
        'Mouse': 30000,
        'SanDisk 64 GB': 70000,
        'Keyboard': 50000,
        'Ethernet-to-USB': 60000,
        'Charger 12V': 65000,
    }

    # Fungsi untuk menambah daftarPembelian dan memperbarui checkout
    def beli(item):
        daftarPembelian.append((item, daftarHarga[item]))
        update_checkout()

    # Fungsi untuk memperbarui tampilan checkout
    checkout_text = tk.StringVar()
    def update_checkout():
        if not daftarPembelian:
            checkout_text.set("Belum ada produk yang dibeli.")
        else:
            teks = "Produk yang dibeli:\n"
            for i, (nama, harga) in enumerate(daftarPembelian, start=1):
                teks += f"{i}. {nama} - Rp {harga:,.0f}\n"
            checkout_text.set(teks)

    # Fungsi untuk menghitung total dan hadiah diskon
    def hitungTotal():
        total = sum(harga for _, harga in daftarPembelian)
        if total >= 100000:
            reward = "🎉 Selamat! Anda mendapat diskon 10%!"
            totalAkhir = total * 0.9
        else:
            reward = "Belanja lagi hingga total 100.000 untuk dapat diskon!"
            totalAkhir = total

        label_total.config(text=f"Harga Asli: Rp {total:,.0f}\nTotal Pembayaran: Rp {totalAkhir:,.0f}")
        label_reward.config(text=reward)

    # Judul
    judul = tk.Label(root, text="Pilih Produk yang Ingin Dibeli", font=('Arial', 16, 'bold'),
                      bg='#292b2c', fg='white', pady=10)
    judul.grid(row=0, column=0, columnspan=3)

    # Membuat tombol-tombol barang
    row, col = 1, 0
    for nama in button_items:
        harga = daftarHarga[nama]
        teks_tombol = f"{nama}\nRp {harga:,.0f}"
        tk.Button(root, text=teks_tombol, width=18, height=4, font=('Arial', 13),
                  bg='#343a40', fg='white', command=lambda n=nama: beli(n)).grid(row=row, column=col, padx=10, pady=10)
        col += 1
        if col > 2:
            col = 0
            row += 1

    # Area checkout
    checkout_text.set("Belum ada produk yang dibeli.")
    label_checkout = tk.Label(root, textvariable=checkout_text, font=('Arial', 13),
                               bg='#292b2c', fg='#f7f7f7', justify='left', anchor='w')
    label_checkout.grid(row=row+1, column=0, columnspan=3, sticky='w', padx=10)

    # Tombol hitung total
    tk.Button(root, text="Hitung Total", font=('Arial', 14), bg='#0275d8', fg='white',
               command=hitungTotal).grid(row=row+2, column=0, columnspan=3, pady=10)

    # Label hasil
    label_total = tk.Label(root, text="Total Pembayaran: Rp 0", font=('Arial', 16), bg='#292b2c', fg='white')
    label_total.grid(row=row+3, column=0, columnspan=3)

    label_reward = tk.Label(root, text="", font=('Arial', 14), bg='#292b2c', fg='#5bc0de')
    label_reward.grid(row=row+4, column=0, columnspan=3)

    root.mainloop()


# === Program 2: Kalkulator Aritmatika ===
def kalkulator_aritmatika():
    root = tk.Tk()
    root.title("Kalkulator aritmatika basic")
    root.configure(background='#292b2c')

    # kolom input
    entry_calc = tk.Entry(root, width=20, font=("Arial", 20), justify='right', relief='ridge', background='white')
    entry_calc.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # kolom hasil
    hasil_var = tk.StringVar(value='hasil')
    label_hasil = tk.Label(root, textvariable=hasil_var, font=('Arial', 18), anchor='e', background='white',
                           relief='sunken', width=20)
    label_hasil.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

    # fungsi untuk kalskulasi aritmatika
    def calculate():
        # debug print left in as in original
        try:
            expression = entry_calc.get()
            value = eval(expression)
            # convert float that is integer-valued to int for nicer display
            if isinstance(value, float) and value.is_integer():
                value = int(value)
            hasil_var.set(str(value))
        except ZeroDivisionError:
            hasil_var.set('0')
        except Exception:
            hasil_var.set("Input tidak valid")

    def tombolClear():
        entry_calc.delete(0, tk.END)
        hasil_var.set("hasil")

    def tombolBackspace():
        current = entry_calc.get()
        if current:
            # delete last character
            entry_calc.delete(len(current)-1, tk.END)

    # list/array Button dalam bentuk matrix
    buttons = [
        '7','8','9','/',
        '4','5','6','*',
        '1','2','3','-',
        '0','.','=','+'
    ]

    # loop untuk generate tombol
    row, col = 2, 0
    for i in buttons:
        if i == '=':
            cmd = calculate  # pass fungsi calculate ke tombol '='
        else:
            cmd = lambda x=i: entry_calc.insert(tk.END, x)
        tk.Button(root, text=i, width=5, height=2, font=('Arial', 14), pady=5, command=cmd).grid(row=row, column=col)

        col += 1
        if col > 3:
            col = 0
            row += 1

    # tombol clear
    tk.Button(root, text='Clear', width=5, height=2, font=('Arial', 14), background='#BB86FC',
               command=tombolClear).grid(row=row, column=0)

    # tombol backspace
    tk.Button(root, text='⌫', width=5, height=2, font=('Arial', 14), background='#BB86FC',
               command=tombolBackspace).grid(row=row, column=1)

    root.mainloop()


# === Program 3: Vending Machine Penjualan Minuman ===
def vending_machine():
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

    # Variabel lokal
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
        nonlocal total_harga
        harga = produk[nama]
        keranjang.append((nama, harga))
        total_harga += harga
        log(f"Produk dipilih: {nama} - Rp{harga:,}")

    def masukkan_uang(nilai):
        nonlocal total_uang
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
        nonlocal total_harga, total_uang, keranjang
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
        nonlocal total_harga, total_uang, keranjang
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


if __name__ == "__main__":
    # Start all three GUIs in separate threads so windows appear at once
    threads = []
    threads.append(threading.Thread(target=bonus_pembelian))
    threads.append(threading.Thread(target=kalkulator_aritmatika))
    threads.append(threading.Thread(target=vending_machine))

    for t in threads:
        t.start()

    # Wait for all GUIs to finish (this will block until windows are closed)
    for t in threads:
        t.join()
