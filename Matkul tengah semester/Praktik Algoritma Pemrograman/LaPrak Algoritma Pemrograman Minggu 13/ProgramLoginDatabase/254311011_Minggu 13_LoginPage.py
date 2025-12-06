from tkinter import *
import tkinter.messagebox as mb
import hashlib
import mysql.connector

root = None 
current_frame = None 
login_data_frame = None 

def GetConnection():
    return mysql.connector.connect(host='localhost', database='db_simpeg', user='root', password='', port=3306)

def clear_window():
    global current_frame
    if current_frame:
        current_frame.destroy()

def Logout():
    clear_window()
    OpenLoginInterface()


def OpenLogoutInterface(username):
    global root
    clear_window() 
    
    root.title("Logout Page")
    root.geometry("400x300") 
    
    global current_frame
    current_frame = Frame(root, bd=10)
    current_frame.pack(fill=BOTH, expand=YES)
    
    Label(current_frame, text=f"Welcome, {username}!", font=('Arial', 16)).pack(pady=50)
    
    Button(current_frame, text="Logout", command=Logout, font=('Arial', 14), bg='red', fg='white').pack(pady=20)


def ProsesLogin():
    global root
    global login_data_frame 
    
    namauser = login_data_frame.entUser.get()
    password = login_data_frame.entPass.get()

    if not namauser and not password:
        mb.showerror('Input Error', 'Username dan Password tidak boleh kosong.', parent=root)
        login_data_frame.entUser.focus_set() 
        return
    if not namauser:
        mb.showerror('Input Error', 'Username tidak boleh kosong.', parent=root)
        login_data_frame.entUser.focus_set() 
        return
    if not password:
        mb.showerror('Input Error', 'Password tidak boleh kosong.', parent=root)
        login_data_frame.entPass.focus_set() 
        return

    password_hash = hashlib.md5(password.encode()).hexdigest()
    
    conn = None
    cursor = None
    try:
        conn = GetConnection()
        query = "SELECT * FROM ms_user WHERE namauser=%s AND password=%s"
        cursor = conn.cursor()
        
        cursor.execute(query, (namauser, password_hash))
        results = cursor.fetchall()

        if (len(results)):
            for row in results:
                if (row[3] == 'Aktif'):
                    mb.showinfo('Login Berhasil', 'Selamat, login berhasil', parent=root)
                    # Success opens the Main App
                    OpenLogoutInterface(namauser) 
                    
                else:
                    mb.showerror('Login Gagal', 'User tidak aktif.', parent=root)
                    login_data_frame.entUser.focus_set() 
                    
        else:
            mb.showerror('Login Gagal', 'Nama user atau password salah.', parent=root)
            login_data_frame.entUser.focus_set() 
            
    except mysql.connector.Error as err:
        mb.showerror('Database Error', f'An error occurred: {err}', parent=root)
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()


def OpenLoginInterface():
    global root
    global login_data_frame 
    
    clear_window() # Clear any existing frame
    root.title("Login User")
    root.geometry("300x200") 
    
    global current_frame
    frameUtama = Frame(root, bd=10)
    current_frame = frameUtama 
    frameUtama.pack(fill=BOTH, expand=YES)

    frData = Frame(frameUtama, bd=5)
    login_data_frame = frData 
    frData.pack(fill=BOTH, expand=YES)

    # 3. atur input username
    Label(frData, text="Nama User").grid(row=0, column=0, sticky=W)
    frData.entUser = Entry(frData) 
    frData.entUser.grid(row=0, column=1)

    # 4. atur input password
    Label(frData, text="Password").grid(row=1, column=0, sticky=W)
    frData.entPass = Entry(frData, show='*')
    frData.entPass.grid(row=1, column=1)

    # 5. atur frame tombol
    frTombol = Frame(frameUtama, bd=5)
    frTombol.pack(fill=BOTH, expand=YES)

    # 6. atur tombol Login
    Button(frTombol, text='Batal', command=root.destroy, width=8).pack(side=LEFT, padx=5, pady=5)
    Button(frTombol, text='Login', command=ProsesLogin, width=8).pack(side=LEFT, padx=5, pady=5)


if __name__ == "__main__":
    root = Tk()
    root.resizable(False, False)
    root.geometry("300x200") 
    root.eval('tk::PlaceWindow . center')
    
    OpenLoginInterface()
    
    root.mainloop()