import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Point Of Sales - YULI TOBAKU")
root.geometry("1100x700")
root.configure(bg="white")

# ---------------------------------------------------------
# 1. SIDEBAR (BAGIAN KIRI) - Tetap
# ---------------------------------------------------------
sidebar = tk.Frame(root, bg="#f8f8f8", width=120, bd=1, relief="flat")
sidebar.pack(side="left", fill="y")


def buat_tombol_menu(teks, warna="black"):
    btn = tk.Button(
        sidebar,
        text=teks,
        fg=warna,
        bg="white",
        font=("Arial", 9),
        relief="groove",
        height=3,
        width=12,
    )
    btn.pack(pady=2, padx=5)


buat_tombol_menu("Keluar / Esc", "red")
buat_tombol_menu("Baru / F1")
buat_tombol_menu("Simpan / F2")
buat_tombol_menu("Buka / F3")
buat_tombol_menu("Retur / F4")
buat_tombol_menu("Bayar / F5", "blue")

# ---------------------------------------------------------
# 2. AREA KANAN (ISI UTAMA)
# ---------------------------------------------------------
area_kanan = tk.Frame(root, bg="white")
area_kanan.pack(side="right", expand=True, fill="both")

header = tk.Frame(area_kanan, bg="#ed1c24", height=30)
header.pack(fill="x")
tk.Label(
    header,
    text="Point Of Sales - YULI TOBAKU",
    fg="white",
    bg="#ed1c24",
    font=("Arial", 10, "bold"),
).pack(pady=5)

# -- Info Kasir & Kotak Hitam (Dibuat Sejajar) --
info_bar = tk.Frame(area_kanan, bg="white", height=80)  # Beri height agar stabil
info_bar.pack(fill="x", padx=10, pady=5)
info_bar.pack_propagate(False)  # Kunci ukuran frame

# Teks Kasir di Kiri
tk.Label(
    info_bar, text="KASIR: ADMIN - B1", bg="white", font=("Arial", 11, "bold")
).place(relx=0.5, rely=0.5, anchor="center")

# Kotak Hitam di Kanan
layar_hitam = tk.Frame(info_bar, bg="black", width=300, height=70)
layar_hitam.pack(side="right")
layar_hitam.pack_propagate(False)
tk.Label(
    layar_hitam, text="0", fg="#ccff00", bg="black", font=("Arial", 40, "bold")
).pack(side="right", padx=15)

# ---------------------------------------------------------
# 3. TABEL BARANG (TREEVIEW)
# ---------------------------------------------------------
tabel_frame = tk.Frame(area_kanan)
tabel_frame.pack(fill="both", expand=True, padx=10, pady=5)

kolom = ("no", "kode", "nama", "qty", "harga", "jumlah", "disc")
tabel = ttk.Treeview(tabel_frame, columns=kolom, show="headings")
for col in kolom:
    tabel.heading(col, text=col.capitalize())
tabel.column("no", width=30, anchor="center")
tabel.column("nama", width=300)
tabel.pack(fill="both", expand=True)

# ---------------------------------------------------------
# 4. AREA INPUT (BAWAH) - PERBAIKAN KERAPIAN
# ---------------------------------------------------------
input_frame = tk.Frame(area_kanan, bg="white")
input_frame.pack(fill="x", padx=10, pady=10)

# Mengunci lebar kolom agar sejajar lurus ke bawah
input_frame.columnconfigure(0, minsize=100)  # Kolom Label (No. Member, Kode, dll)
input_frame.columnconfigure(1, minsize=250)  # Kolom Input Kiri
input_frame.columnconfigure(2, minsize=100)  # Kolom Label Tengah (No Telp)

font_input = ("Arial", 9)

# Baris 1: No. Member & No Telp
tk.Label(input_frame, text="No. Member", bg="white", font=font_input).grid(
    row=0, column=0, sticky="w", pady=2
)
tk.Entry(input_frame, width=30).grid(row=0, column=1, sticky="w")

tk.Label(input_frame, text="No Telp", bg="white", font=font_input).grid(
    row=0, column=2, sticky="w", padx=10
)
tk.Entry(input_frame, width=30).grid(row=0, column=3, sticky="w")

# Baris 2: Kode
tk.Label(input_frame, text="Kode", bg="white", font=font_input).grid(
    row=1, column=0, sticky="w", pady=2
)
f_kode = tk.Frame(input_frame, bg="white")
f_kode.grid(row=1, column=1, sticky="w")
tk.Entry(f_kode, width=25).pack(side="left")
tk.Button(f_kode, text="🔍", font=("Arial", 7), width=2).pack(side="left", padx=2)

# Baris 3: Deskripsi
tk.Label(input_frame, text="Deskripsi", bg="white", font=font_input).grid(
    row=2, column=0, sticky="w", pady=2
)
tk.Entry(input_frame, width=72).grid(row=2, column=1, columnspan=3, sticky="w")

# Baris 4: Qty
tk.Label(input_frame, text="Qty", bg="white", font=font_input).grid(
    row=3, column=0, sticky="w", pady=2
)
tk.Entry(input_frame, width=15).grid(row=3, column=1, sticky="w")

root.mainloop()
