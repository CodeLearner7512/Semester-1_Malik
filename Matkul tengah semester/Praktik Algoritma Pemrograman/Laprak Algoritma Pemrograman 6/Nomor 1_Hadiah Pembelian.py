import tkinter as gui

# Variabel, list, dan dictionary
daftarPembelian = []
Button = [
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

# Root Window
root = gui.Tk()
root.title("Bonus Pembelian")
root.configure(background='#292b2c')

# Judul
judul = gui.Label(root, text="Pilih Produk yang Ingin Dibeli", font=('Arial', 16, 'bold'),
                  bg='#292b2c', fg='white', pady=10)
judul.grid(row=0, column=0, columnspan=3)

# Membuat tombol-tombol barang
row, col = 1, 0
for nama in Button:
    harga = daftarHarga[nama]
    teks_tombol = f"{nama}\nRp {harga:,.0f}"
    gui.Button(root, text=teks_tombol, width=18, height=4, font=('Arial', 13),
               bg='#343a40', fg='white', command=lambda n=nama: beli(n)).grid(row=row, column=col, padx=10, pady=10)
    col += 1
    if col > 2:
        col = 0
        row += 1

# Area checkout
checkout_text = gui.StringVar()
checkout_text.set("Belum ada produk yang dibeli.")
label_checkout = gui.Label(root, textvariable=checkout_text, font=('Arial', 13),
                           bg='#292b2c', fg='#f7f7f7', justify='left', anchor='w')
label_checkout.grid(row=row+1, column=0, columnspan=3, sticky='w', padx=10)

# Tombol hitung total
gui.Button(root, text="Hitung Total", font=('Arial', 14), bg='#0275d8', fg='white',
           command=hitungTotal).grid(row=row+2, column=0, columnspan=3, pady=10)

# Label hasil
label_total = gui.Label(root, text="Total Pembayaran: Rp 0", font=('Arial', 16), bg='#292b2c', fg='white')
label_total.grid(row=row+3, column=0, columnspan=3)

label_reward = gui.Label(root, text="", font=('Arial', 14), bg='#292b2c', fg='#5bc0de')
label_reward.grid(row=row+4, column=0, columnspan=3)

root.mainloop()
