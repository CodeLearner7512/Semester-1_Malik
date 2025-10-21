import tkinter as gui

# List utama untuk menyimpan data pegawai
id_pegawai = []
nama = []
nomor_hp = []

# ==GUI setup untuk tampilan GUI utama/root==
root = gui.Tk()
root.title("Data Pegawai")
root.geometry("450x550")

# ==Frame untuk grouping field==
frame_menu = gui.Frame(root)
frame_menu.pack(pady=10)

frame_input = gui.Frame(root)
frame_input.pack(pady=10)

frame_output = gui.Frame(root)
frame_output.pack(pady=10, fill="both", expand=True)

frame_list = gui.Frame(root)
frame_list.pack(pady=10, fill="both", expand=True)

# === field untuk output CRUD ===
output_box = gui.Text(frame_output, height=6, width=50, wrap="word", relief="groove", borderwidth=2)
output_box.pack()

# === field untuk menampilkan List data prgawai===
gui.Label(frame_list, text="Daftar Data Pegawai:", font=("Arial", 10, "bold")).pack()
list_box = gui.Text(frame_list, height=8, width=50, wrap="none", relief="sunken", borderwidth=2, state="disabled")
list_box.pack()

# === functon untuk refresh output dan cleaar field khusus untuk  CRUD ===
def clear_input_frame():
    """menghapus semua widget di input field"""
    for widget in frame_input.winfo_children():
        widget.destroy()

def show_output(text):
    """menampilkan teks di output field"""
    output_box.delete(1.0, gui.END)
    output_box.insert(gui.END, text)

def refresh_list():
    """menampilkan list data pegawai"""
    list_box.config(state="normal")
    list_box.delete(1.0, gui.END)
    if len(id_pegawai) == 0:
        list_box.insert(gui.END, "Belum ada data pegawai.\n")
    else:
        list_box.insert(gui.END, f"{'ID':<10} | {'Nama':<20} | {'No HP':<15}\n")
        list_box.insert(gui.END, "-" * 50 + "\n")
        for i in range(len(id_pegawai)):
            list_box.insert(gui.END, f"{id_pegawai[i]:<10} | {nama[i]:<20} | {nomor_hp[i]:<15}\n")
    list_box.config(state="disabled")

# === function CRUD dengan generate input field  ===
def create():
    clear_input_frame()
    gui.Label(frame_input, text="Masukkan ID Pegawai:").pack()
    entry_id = gui.Entry(frame_input, width=30)
    entry_id.pack()

    gui.Label(frame_input, text="Masukkan Nama Pegawai:").pack()
    entry_nama = gui.Entry(frame_input, width=30)
    entry_nama.pack()

    gui.Label(frame_input, text="Masukkan Nomor HP Pegawai:").pack()
    entry_hp = gui.Entry(frame_input, width=30)
    entry_hp.pack()

    #function untuk append data
    def save():
        id_pegawai.append(entry_id.get())
        nama.append(entry_nama.get())
        nomor_hp.append(entry_hp.get())
        show_output(f"Data pegawai '{entry_nama.get()}' berhasil ditambahkan.")
        clear_input_frame()
        refresh_list()

    gui.Button(frame_input, text="Simpan", command=save).pack(pady=5)


def read():
    clear_input_frame()
    gui.Label(frame_input, text="Masukkan ID Pegawai yang ingin dicari:").pack()
    entry_id = gui.Entry(frame_input, width=30)
    entry_id.pack()

    def find():
        id_search = entry_id.get()
        if id_search in id_pegawai:
            i = id_pegawai.index(id_search)
            result = (f"ID: {id_pegawai[i]}\n"
                      f"Nama: {nama[i]}\n"
                      f"Nomor HP: {nomor_hp[i]}")
        else:
            result = "Error: Pegawai tidak ditemukan"
        show_output(result)
        clear_input_frame()

    gui.Button(frame_input, text="Cari", command=find).pack(pady=5)


def update():
    clear_input_frame()
    gui.Label(frame_input, text="Masukkan ID Pegawai yang akan diubah:").pack()
    entry_id = gui.Entry(frame_input, width=30)
    entry_id.pack()

    def edit():
        id_search = entry_id.get()
        if id_search in id_pegawai:
            index = id_pegawai.index(id_search)
            clear_input_frame()
            gui.Label(frame_input, text="ID Baru:").pack()
            entry_new_id = gui.Entry(frame_input, width=30)
            entry_new_id.pack()
            gui.Label(frame_input, text="Nama Baru:").pack()
            entry_new_nama = gui.Entry(frame_input, width=30)
            entry_new_nama.pack()
            gui.Label(frame_input, text="Nomor HP Baru:").pack()
            entry_new_hp = gui.Entry(frame_input, width=30)
            entry_new_hp.pack()

            def save_update():
                id_pegawai[index] = entry_new_id.get()
                nama[index] = entry_new_nama.get()
                nomor_hp[index] = entry_new_hp.get()
                show_output(f"Data pegawai '{id_search}' berhasil diupdate.")
                clear_input_frame()
                refresh_list()

            gui.Button(frame_input, text="Simpan Perubahan", command=save_update).pack(pady=5)
        else:
            show_output("Error: Pegawai tidak ditemukan")
            clear_input_frame()

    gui.Button(frame_input, text="Lanjut", command=edit).pack(pady=5)


def delete():
    clear_input_frame()
    gui.Label(frame_input, text="Masukkan ID Pegawai yang akan dihapus:").pack()
    entry_id = gui.Entry(frame_input, width=30)
    entry_id.pack()

    def remove():
        id_search = entry_id.get()
        if id_search in id_pegawai:
            index = id_pegawai.index(id_search)
            id_pegawai.pop(index)
            nama.pop(index)
            nomor_hp.pop(index)
            show_output(f"Data pegawai '{id_search}' telah dihapus.")
            refresh_list()
        else:
            show_output("Error: Pegawai tidak ditemukan")
        clear_input_frame()

    gui.Button(frame_input, text="Hapus", command=remove).pack(pady=5)


# === tombol menu CRUD ===
gui.Label(frame_menu, text="Menu CRUD Pegawai", font=("Arial", 14, "bold")).pack(pady=5)
gui.Button(frame_menu, text="Create", width=10, command=create).pack(side="left", padx=5)
gui.Button(frame_menu, text="Read", width=10, command=read).pack(side="left", padx=5)
gui.Button(frame_menu, text="Update", width=10, command=update).pack(side="left", padx=5)
gui.Button(frame_menu, text="Delete", width=10, command=delete).pack(side="left", padx=5)

# refresh field untuk menampilkan list data pegawai
refresh_list()

root.mainloop()
