#Program Vending Machine
def transaksi(input_koin, input_id_produk, produk_dict):
    if input_id_produk not in produk_dict:
        return "Produk Tidak Tersedia"
    
    harga_dipilih = produk_dict[input_id_produk]["harga"]
    
    if input_koin == harga_dipilih:
        return "Koin Pas"
    elif input_koin > harga_dipilih:
        return float(input_koin - harga_dipilih)
    else:
        return "Koin Kurang"

def tampilkan_daftar_produk(produk_dict):
    print("\n=== DAFTAR PRODUK TERSEDIA ===")
    print(f"{'ID':<6} {'Nama Produk':<20} {'Harga (Rp)':>10}")
    print("-" * 40)
    for pid, info in produk_dict.items():
        print(f"{pid:<6} {info['nama']:<20} {info['harga']:>10}")
    print("-" * 40)

def menu_transaksi(produk_dict):
    print("\n=== MENU TRANSAKSI ===")
    tampilkan_daftar_produk(produk_dict)

    try:
        input_koin = int(input("Masukkan nominal koin Anda (Rp): "))
    except ValueError:
        print("--- Input tidak valid! Harap masukkan angka. ---")
        return

    input_id = input("Masukkan ID produk yang ingin dibeli: ").upper()

    hasil = transaksi(input_koin, input_id, produk_dict)

    if hasil == "Koin Pas":
        print(f"++++ Transaksi berhasil! Produk '{produk_dict[input_id]['nama']}' dikeluarkan. ++++")
    elif hasil == "Koin Kurang":
        print("++++ Koin yang dimasukkan kurang. Silakan masukkan nominal yang cukup atau batalkan. ++++")
        opsi = input("Apakah Anda ingin membatalkan transaksi? (y/n): ").lower()
        if opsi == "y":
            print(f"++++ Koin sebesar Rp{input_koin} dikembalikan. ++++")
        else:
            print("++++ Silakan coba lagi dengan nominal koin yang sesuai. ++++")
    elif hasil == "Produk Tidak Tersedia":
        print("++++ Produk dengan ID tersebut tidak tersedia. ++++")
        print(f"++++ Koin sebesar Rp{input_koin} dikembalikan. ++++")
    elif isinstance(hasil, float):
        print(f"++++ Transaksi berhasil! Produk '{produk_dict[input_id]['nama']}' dikeluarkan. ++++")
        print(f"++++ Kembalian Anda: Rp{int(hasil)} ++++")
    else:
        print("!!! Terjadi kesalahan yang tidak diketahui, Hubungi Admin(Malik). !!!")

def menu_admin(produk_dict):
    print("\n=== MENU ADMIN - TAMBAH PRODUK ===")
    while True:
        print("\nKetik 'kembali' untuk kembali ke menu utama.")
        pid = input("Masukkan ID Produk (contoh: D4): ").upper()
        if pid == "KEMBALI":
            break

        nama = input("Masukkan Nama Produk: ")
        if nama.lower() == "kembali":
            break

        try:
            harga = int(input("Masukkan Harga Produk (Rp): "))
        except ValueError:
            print("Input harga tidak valid. Harap masukkan angka.")
            continue

        produk_dict[pid] = {"nama": nama, "harga": harga}
        print(f"++++ Produk '{nama}' berhasil ditambahkan dengan ID {pid} dan harga Rp{harga}. ++++")

def main():
    produk = {
        "A1": {"nama": "Cola", "harga": 5000},
        "B2": {"nama": "Chips", "harga": 7000},
        "C3": {"nama": "Aqua", "harga": 3000},
    }

    while True:
        print("\n===============================")
        print("   PROGRAM VENDING MACHINE")
        print("===============================")
        print("1. Menu Transaksi (Untuk Pembeli)")
        print("2. Menu Admin (Tambah Produk)")
        print("3. Lihat Daftar Produk")
        print("4. Keluar Program")
        print("===============================")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            menu_transaksi(produk)
        elif pilihan == "2":
            menu_admin(produk)
        elif pilihan == "3":
            tampilkan_daftar_produk(produk)
        elif pilihan == "4":
            print("++++ Terima kasih telah menggunakan mesin penjual otomatis. Program ditutup. ++++")
            break
        else:
            print("!!! Pilihan tidak valid! Harap pilih antara 1-4. !!!")

# Jalankan program utama(loop supaya tidak terminated)
if __name__ == "__main__":
    main()
