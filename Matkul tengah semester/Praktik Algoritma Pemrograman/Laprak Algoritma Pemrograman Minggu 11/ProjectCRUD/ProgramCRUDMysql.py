import mysql.connector
import sys
import time

#Deklarasi Class ConnectDatabase dan CRUD
class ConnectDatabase:
    def GetConnection():

        return mysql.connector.connect(host='localhost', db='db_mahasiswa', user='root',password='', port=3306)
    

    conn = None
    try:
        conn = GetConnection()
    except mysql.connector.Error as err:
        print("Koneksi database gagal saat startup.")
        print(f"Error: {err}")

class CreateClass:
    def AddData():
        conn = ConnectDatabase.conn
        if not conn:
            print("Gagal: Koneksi database tidak tersedia.")
            return

        try:
            npm = input("Masukkan NPM: ")
            namaMahasiswa = input("Masukkan Nama Mahasiswa: ")
            alamat = input("Masukkan Alamat: ")
            
            data = (npm, namaMahasiswa, alamat)
            
            query = "INSERT INTO mahasiswa (npm, namaMahasiswa, alamat) VALUES (%s, %s, %s)"
            
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            print("Data mahasiswa berhasil ditambahkan.")
            
        except mysql.connector.Error as e:
            print(f"Gagal menambahkan data. Error: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

class ReadClass:
    def ReadData():
        conn = ConnectDatabase.conn
        if not conn:
            print("Gagal: Koneksi database tidak tersedia.")
            return
            
        try:
            query = "SELECT * FROM mahasiswa"
            
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            
            print("\n" + "="*50)
            print("DATA MAHASISWA")
            print("="*50)

            if results:
                for row in results:
                    print(f"NPM: {row[0]}, Nama: {row[1]}, Alamat: {row[2]}")
            else:
                print("Tidak ada data mahasiswa ditemukan.")
            
            print("="*50)

        except mysql.connector.Error as e:
            print(f"Gagal membaca data. Error: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

class UpdateClass:
    def UpdateData():
        conn = ConnectDatabase.conn
        if not conn:
            print("Gagal: Koneksi database tidak tersedia.")
            return

        try:
            key = input("Masukkan NPM Lama (data yang ingin diubah): ")
            npm = input("Masukkan NPM Baru: ")
            namaMahasiswa = input("Masukkan Nama Mahasiswa Baru: ")
            alamat = input("Masukkan Alamat Baru: ")

            data = (npm, namaMahasiswa, alamat, key)

            query = "UPDATE mahasiswa SET npm=%s, namaMahasiswa=%s, alamat=%s WHERE npm=%s"

            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            
            if cursor.rowcount > 0:
                print(f"Data mahasiswa dengan NPM '{key}' berhasil diupdate.")
            else:
                print(f"Data mahasiswa dengan NPM '{key}' tidak ditemukan.")

        except mysql.connector.Error as e:
            print(f"Gagal mengupdate data. Error: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

class DeleteClass:
    def DeleteData():
        conn = ConnectDatabase.conn
        if not conn:
            print("Gagal: Koneksi database tidak tersedia.")
            return

        try:
            key = input("Masukkan NPM Mahasiswa yang ingin dihapus: ")

            data = (key,) 

            query = "DELETE FROM mahasiswa WHERE npm=%s"
            
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            
            if cursor.rowcount > 0:
                print(f"Data mahasiswa dengan NPM '{key}' berhasil dihapus.")
            else:
                print(f"Data mahasiswa dengan NPM '{key}' tidak ditemukan.")

        except mysql.connector.Error as e:
            print(f"Gagal menghapus data. Error: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
    
#Main Program(mode Loop)

def display_menu():
    """Menampilkan pilihan menu CLI."""
    print("\n" + "="*50)
    print("SISTEM INFORMASI MANAJEMEN DATA MAHASISWA")
    print("="*50)
    print("1. Lihat Data")
    print("2. Tambah Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Keluar dari Program")
    print("-" * 50)

def main_loop():
    """Loop utama aplikasi CLI."""
    
    is_running = True
    
    if ConnectDatabase.conn is None:
        print("APLIKASI TIDAK DAPAT BERJALAN. Harap periksa koneksi MySQL Anda.")
        is_running = False

    while is_running:
        display_menu()
        
        try:
            choice = input("Pilih menu (1-5): ").strip()

            if choice == '1':
                print("\n--- Tampilkan Data ---")
                ReadClass.ReadData()
                
            elif choice == '2':
                print("\n--- Tambahkan Data ---")
                CreateClass.AddData()  
                
            elif choice == '3':
                print("\n--- Ubah Data ---")
                UpdateClass.UpdateData()
                
            elif choice == '4':
                print("\n--- Hapus Data ---")
                DeleteClass.DeleteData()
                
            elif choice == '5':
                if ConnectDatabase.conn:
                    ConnectDatabase.conn.close()
                    print("\nKoneksi database ditutup.")
                print("Terima kasih. Program diakhiri.")
                is_running = False
                
            else:
                print("\nPilihan tidak valid. Silakan masukkan angka 1 sampai 5.")

        except EOFError:
            print("\nInput terhenti. Keluar dari program.")
            is_running = False
        except Exception as e:
            print(f"\nKesalahan umum terjadi di loop: {e}")
            time.sleep(1)

if __name__ == "__main__":
    main_loop()