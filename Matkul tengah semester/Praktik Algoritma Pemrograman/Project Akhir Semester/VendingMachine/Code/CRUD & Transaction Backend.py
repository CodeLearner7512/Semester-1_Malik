import mysql.connector
from mysql.connector import Error
from decimal import Decimal
from typing import List,Dict,Any
from updatedelete import UpdateDelete



class dbCRUD:
    """
    Class untuk operasi ke database: CREATE & READ pada tabel produk.

    Catatan:
    - Tidak memiliki referensi ke widget GUI.
    - Hanya return nilai keberhasilan(ada exception yang di catch atau tidak) atau data yang di fetch dari database.
    - Semua error dan exception direturn, yang nantinya akan ditampiilkan melalui messagebox.
    """

    def __init__(self, connection):
        """
        Parameter(self, connection):
            connection  = object koneksi MySQL yang sudah aktif
            self = method ini adalah 'instance method'
        """
        self.conn = connection
        self.cursor = connection.cursor()

    # ---------------------------------------------------------
    # CREATE
    # ---------------------------------------------------------
    def createProduct(self, id_produk, nama_produk, harga, stok_produk, gambar_produk):
        """
        Menambahkan produk baru ke database.

        Argument:
            (self, id_produk, nama_produk, harga, stok_produk, gambar_produk)

        Return:
            method ini return 2 value untuk setiap case yaitu (bool,exception)
            (True, None) jika berhasil
            (False, Exception as ex) jika gagal
        """

        sql = """
            INSERT INTO produk
            (id_produk, nama_produk, harga, stok_produk, gambar_produk)
            VALUES (%s, %s, %s, %s, %s)
        """

        try:
            self.cursor.execute(sql, (id_produk, nama_produk, harga, stok_produk, gambar_produk))
            self.conn.commit()
            return True, None

        except Exception as ex:
            self.conn.rollback()
            return False, ex

    # ---------------------------------------------------------
    # CREATE - Batch
    # ---------------------------------------------------------
    def createProductBatch(self, list_data_produk: List[Dict[str, Any]]):
        """
        Menambahkan beberapa produk baru sekaligus ke database.

        Argument:
            (self, list_data_produk: List[Dict[str, Any]])

        Cara penggunaan parameter/argument:
            1. buat list
            2. buat dictionary dengan key ("ID","Nama","Harga","Stok","Gambar")
            3. append dictionary ke dalam list (dictionary menjadi item dari list)
            4. pass list sebagai parameter

        Return:
            method ini return 2 value untuk setiap case yaitu (bool,exception)
            (True, None) jika berhasil
            (False, Exception as ex) jika gagal
        """

        try:
            for dict_item in list_data_produk :

                self.createProduct(dict_item["ID"],dict_item["Nama"],dict_item["Harga"],dict_item["Stok"],dict_item["Gambar"])
            return True, None
        except Exception as ex:
            return False, ex


    # ---------------------------------------------------------
    # READ - semua produk
    # ---------------------------------------------------------
    def readAllProduct(self):
        """
        Mengambil seluruh data produk dari database.

        Argument:
            (self)

        Return:
            method ini return 2 value untuk setiap case yaitu (list data,exception)
            (list semua data, None) jika berhasil
            (None, Exception) jika gagal
        """

        sql = """
            SELECT id_produk, nama_produk, harga, stok_produk, gambar_produk
            FROM produk
        """

        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall(), None

        except Exception as ex:
            return None, ex

    # ---------------------------------------------------------
    # READ berdasarkan id_produk
    # ---------------------------------------------------------
    def readProductId(self, id_produk):
        """
        Mengambil data 1 produk berdasarkan id_produk.

        Argument:
            (self, id_produk)

        Return:
            method ini return 2 value untuk setiap case yaitu (data dari row yang dipilih,exception)
            (tuple_data, None) jika berhasil (atau None jika tidak ada)
            (None, Exception) jika error
        """

        sql = """
            SELECT id_produk, nama_produk, harga, stok_produk, gambar_produk
            FROM produk
            WHERE id_produk = %s
        """

        try:
            self.cursor.execute(sql, (id_produk))
            return self.cursor.fetchone(), None

        except Exception as ex:
            return None, ex

    # ---------------------------------------------------------
    # READ berdasarkan nama_produk (LIKE ...)
    # ---------------------------------------------------------
    def readProductName(self, nama):
        """
        Mengambil data 1 produk berdasarkan nama_produk (LIKE ...).

        Argument:
            (self, nama)

        Return:
            method ini return 2 value untuk setiap case yaitu (data dari row yang dipilih,exception)
            ([tuple], None) jika berhasil
            (None, Exception) jika error
        """

        sql = """
            SELECT id_produk, nama_produk, harga, stok_produk, gambar_produk
            FROM produk
            WHERE nama_produk LIKE %s
        """

        try:
            self.cursor.execute(sql, (f"%{nama}%"))
            return self.cursor.fetchall(), None

        except Exception as ex:
            return None, ex

    # ---------------------------------------------------------
    # UPDATE
    # ---------------------------------------------------------
    def updatedata(self, id_produk, nama_produk, harga, stok_produk, gambar_produk):
        """
        Memperbarui data produk di database.
        Tapi tidak boleh memperbarui id_produk.

        Argument:
            (self, id_produk, nama_produk, harga, stok_produk, gambar_produk)

        Return:
            method ini return 2 value untuk setiap case yaitu (bool,exception)
            (True, None) jika berhasil
            (False, Exception as ex) jika gagal
        """

        sql = "UPDATE produk SET nama_produk=%s, harga=%s, stok_produk=%s, gambar_produk=%s WHERE id_produk=%s"


        try:
            self.cursor.execute(sql, (nama_produk, harga, stok_produk, gambar_produk, id_produk))
            self.conn.commit()
            return True, None 
        except Exception as ex:
            self.conn.rollback()
            return False, ex
    

    # ---------------------------------------------------------
    # DELETE
    # ---------------------------------------------------------
    def deletedata(self, id_produk):
        """
        Memperbarui data produk di database.
        Tapi tidak boleh memperbarui id_produk.

        Argument:
            (self, id_produk)

        Return:
            method ini return 2 value untuk setiap case yaitu (bool,exception)
            (True, None) jika berhasil
            (False, Exception as ex) jika gagal
        """

        sql = "DELETE FROM produk WHERE id_produk=%s"


        try:
            self.cursor.execute(sql, (id_produk))
            self.conn.commit()
            return True, None
        except Exception as ex:
            self.conn.rollback()
            return False, ex
        


class dbTransaksi:
    """
    Class untuk operasi transaksi Aplikasi Vending Machine.

    Catatan:
    - Tidak memiliki referensi ke widget GUI.
    - Hanya return nilai keberhasilan(ada exception yang di catch atau tidak) atau data yang di fetch dari database.
    - Semua error dan exception direturn, yang nantinya akan ditampiilkan melalui messagebox.
    """

    def __init__(self, connection):
        """
        Parameter(self, connection):
            connection  = object koneksi MySQL yang sudah aktif
            self = method ini adalah 'instance method'
        """
        self.conn = connection
        self.cursor = connection.cursor()


    # function panggil id/stok di database
    def get_produk(self, id_produk):
        self.cursor.execute("SELECT * FROM produk WHERE id_produk = %s", (id_produk,))
        return self.cursor.fetchone()
    
    def stok_kurang(self, id_produk):
        self.cursor.execute("UPDATE produk SET stok_produk = stok_produk-1 WHERE id_produk = %s", (id_produk,))
        self.conn.commit()

    # penghitungan transaksi
    def transaksi(self):
        self.tampil_produk()
        koin_masuk = int(input("masukkan koin anda = Rp. "))
        # batal = str(input("apakah anda ingin membatalkan transaksi? (y/t) = "))
        # #tampilan awal
        # if batal == 'y':
        #     print("Transaksi dibatalkan, silahkan ambil kembali koin: Rp.", koin_masuk)
        #     return

        id_produk = int(input("masukkan kode minuman = "))
        produk = self.get_produk(id_produk)
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

        self.stok_kurang(id_produk)
        return 0
