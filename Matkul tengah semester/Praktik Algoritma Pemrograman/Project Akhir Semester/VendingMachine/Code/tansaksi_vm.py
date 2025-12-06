import mysql.connector
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_vm"
    )
    cursor = db.cursor(dictionary=True)
except mysql.connector.Error as err:
    print("Koneksi ke database gagal:", err)
    db = None
    cursor = None

#tamplan menu produk dari database
def tampil_produk():
   cursor.execute("SELECT * FROM produk")
   results = cursor.fetchall()
   print("======================= Selamat Datang Di Vending Machine Kel 6 ======================")
   for row in results:
       print(f"Nama produk = {row['nama_produk']} || Kode produk = {row['id_produk']} || Stok tersedia = {row['stok_produk']} || Harga = Rp.{row['harga']} ")
       print("=====================================================================================")
   print("\n")

# function panggil id/stok di database
def get_produk(id_produk):
    cursor.execute("SELECT * FROM produk WHERE id_produk = %s", (id_produk,))
    return cursor.fetchone()
def stok_kurang(id_produk):
    cursor.execute("UPDATE produk SET stok_produk = stok_produk-1 WHERE id_produk = %s", (id_produk,))
    db.commit()

# penghitungan transaksi
def transaksi():
    tampil_produk()
    koin_masuk = int(input("masukkan koin anda = Rp. "))
    # batal = str(input("apakah anda ingin membatalkan transaksi? (y/t) = "))
    # #tampilan awal
    # if batal == 'y':
    #     print("Transaksi dibatalkan, silahkan ambil kembali koin: Rp.", koin_masuk)
    #     return

    id_produk = int(input("masukkan kode minuman = "))
    produk = get_produk(id_produk)
    if produk is None:
        print("Produk yang anda pilih tidak ditemukan, ambil koin anda kembali: Rp.",koin_masuk)
        return
    harga = produk['harga']
    print(f"Anda memilih {produk['nama_produk']} dengan harga Rp.{harga}")
    
    # kalkulasi pembayaran
    if koin_masuk == harga:
        print("Koin anda sudah pas silahkan ambil minuman", produk['nama_produk'], "anda")
        total_koin = koin_masuk
    elif koin_masuk > harga:
         hasil_kembalian = koin_masuk - harga
         total_koin = koin_masuk - harga
         print("Pembayaran berhasil, silahkan ambil kembalian = Rp.", hasil_kembalian, ", silahkan ambil minuman", produk['nama_produk'], "anda")
    elif koin_masuk < harga:
         kurang = harga - koin_masuk
         print("koin anda tidak cukup, kekurangan koin = Rp.", kurang, )
         tambahan = int(input("masukkan koin tambahan = Rp. "))
         total_koin = koin_masuk + tambahan
        # kondisi jika koin masuk masih kurang dari harga produk
         while total_koin < harga:
            kurang_lagi = harga - total_koin
            print("koin anda masih kurang sebesar Rp.", kurang_lagi)
            tambah_lagi = int(input("masukkan koin tambahan lagi = Rp. "))
            total_koin += tambah_lagi
            if total_koin == harga:
                print("Pembayaran berhasil, silahkan ambil minuman", produk['nama_produk'], "anda")
            elif total_koin > harga:
                hasil_kembalian = total_koin - harga
                print("Pembayaran berhasil, silahkan ambil kembalian = Rp.", hasil_kembalian, ", silahkan ambil minuman", produk['nama_produk'],"anda")               
    else:
        print("Pembayaran gagal, silahkan ambil kembali koin anda: Rp.", koin_masuk)
        return
    
    print("\n")
    print("======== Nota Vending Machine kel 5 ========")
    print("Produk Yang dibeli :", produk['nama_produk'])
    print("Kode Produk :", produk['id_produk'])
    print("Harga produk :  Rp.", harga)
    print("Koin yang dimasukkan : Rp.", koin_masuk)
    if koin_masuk < harga:
        print("Koin tambahan : Rp. ", tambahan)
        if tambahan < koin_masuk:
            print("Total koin yang dimasukkan : Rp.", tambahan + tambah_lagi)
    if koin_masuk > harga:
        print("Kembalian : Rp.", hasil_kembalian)
    elif total_koin == harga:
        print("Kembalian : Rp. 0")
    else:
        print("Kembalian : Rp. 0")
    print("Jumlah Stok Yang Tersedia:", produk['stok_produk'] -1)
    print("=============================================")

    stok_kurang(id_produk)
    return 0
transaksi()







