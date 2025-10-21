import tkinter as tk
from tkinter import messagebox

# Dictionary utama untuk menyimpan data pegawai
data_pegawai = {
    "id_pegawai": [],
    "nama": [],
    "no_hp": []
}


# Function untuk menampilkan daftar pegawai di field daftar data pegawai
def refresh_list():
    list_box.delete("1.0", tk.END)
    for i in range(len(data_pegawai["id_pegawai"])):
        list_box.insert(tk.END, f"ID: {data_pegawai['id_pegawai'][i]} | "
                                f"Nama: {data_pegawai['nama'][i]} | "
                                f"Telp: {data_pegawai['no_hp'][i]}\n")


# Function untuk menghapus frame input lama
def clear_input_frame():
    for widget in input_frame.winfo_children():
        widget.destroy()


# CREATE
def create_gui():
    clear_input_frame()

    tk.Label(input_frame, text="Masukkan ID Pegawai:").pack()
    id_entry = tk.Entry(input_frame)
    id_entry.pack()

    tk.Label(input_frame, text="Masukkan Nama Pegawai:").pack()
    nama_entry = tk.Entry(input_frame)
    nama_entry.pack()

    tk.Label(input_frame, text="Masukkan Telepon Pegawai:").pack()
    hp_entry = tk.Entry(input_frame)
    hp_entry.pack()

    def submit():
        data_pegawai["id_pegawai"].append(id_entry.get())
        data_pegawai["nama"].append(nama_entry.get())
        data_pegawai["no_hp"].append(hp_entry.get())
        messagebox.showinfo("Sukses", "Data pegawai berhasil ditambahkan!")
        clear_input_frame()
        refresh_list()

    tk.Button(input_frame, text="Submit", command=submit).pack(pady=5)


# READ
def read_gui():
    clear_input_frame()

    tk.Label(input_frame, text="Masukkan ID Pegawai yang ingin dicari:").pack()
    id_entry = tk.Entry(input_frame)
    id_entry.pack()

    def submit():
        idx = id_entry.get()
        if idx in data_pegawai["id_pegawai"]:
            index_search = data_pegawai["id_pegawai"].index(idx)
            result = (f"ID: {data_pegawai['id_pegawai'][index_search]}\n"
                      f"Nama: {data_pegawai['nama'][index_search]}\n"
                      f"No HP: {data_pegawai['no_hp'][index_search]}")
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, result)
        else:
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, "Error: Pegawai tidak ditemukan")

    tk.Button(input_frame, text="Cari", command=submit).pack(pady=5)


# UPDATE
def update_gui():
    clear_input_frame()

    tk.Label(input_frame, text="Masukkan ID Pegawai yang ingin diubah:").pack()
    id_entry = tk.Entry(input_frame)
    id_entry.pack()

    tk.Label(input_frame, text="Masukkan ID Baru:").pack()
    id_new_entry = tk.Entry(input_frame)
    id_new_entry.pack()

    tk.Label(input_frame, text="Masukkan Nama Baru:").pack()
    nama_new_entry = tk.Entry(input_frame)
    nama_new_entry.pack()

    tk.Label(input_frame, text="Masukkan Telepon Baru:").pack()
    hp_new_entry = tk.Entry(input_frame)
    hp_new_entry.pack()

    def submit():
        idx = id_entry.get()
        if idx in data_pegawai["id_pegawai"]:
            index_search = data_pegawai["id_pegawai"].index(idx)
            data_pegawai["id_pegawai"][index_search] = id_new_entry.get()
            data_pegawai["nama"][index_search] = nama_new_entry.get()
            data_pegawai["no_hp"][index_search] = hp_new_entry.get()
            messagebox.showinfo("Sukses", "Data pegawai berhasil diubah!")
            clear_input_frame()
            refresh_list()
        else:
            messagebox.showerror("Error", "Pegawai tidak ditemukan")

    tk.Button(input_frame, text="Submit", command=submit).pack(pady=5)


# DELETE
def delete_gui():
    clear_input_frame()

    tk.Label(input_frame, text="Masukkan ID Pegawai yang ingin dihapus:").pack()
    id_entry = tk.Entry(input_frame)
    id_entry.pack()

    def submit():
        idx = id_entry.get()
        if idx in data_pegawai["id_pegawai"]:
            index_search = data_pegawai["id_pegawai"].index(idx)
            data_pegawai["id_pegawai"].pop(index_search)
            data_pegawai["nama"].pop(index_search)
            data_pegawai["no_hp"].pop(index_search)
            messagebox.showinfo("Sukses", "Data pegawai berhasil dihapus!")
            clear_input_frame()
            refresh_list()
        else:
            messagebox.showerror("Error", "Pegawai tidak ditemukan")

    tk.Button(input_frame, text="Hapus", command=submit).pack(pady=5)


# Window utama
window = tk.Tk()
window.title("Data Pegawai menggunakan Dictionary")
window.geometry("700x500")

# Tombol CRUD
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Create", command=create_gui, width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Read", command=read_gui, width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Update", command=update_gui, width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Delete", command=delete_gui, width=10).pack(side=tk.LEFT, padx=5)

# Frame input 
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

# field output
output_box = tk.Text(window, height=6, width=70, relief="solid", borderwidth=1)
output_box.pack(pady=5)

# Field daftar data pegawai
tk.Label(window, text="Daftar Data Pegawai:").pack()
list_box = tk.Text(window, height=10, width=70, relief="solid", borderwidth=1)
list_box.pack()

# Start program GUI
window.mainloop()
