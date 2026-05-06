import tkinter as tk

root = tk.Tk()
root.title("Kasir Dasar")
root.geometry("400x400")

# --- TAMBAHKAN INI ---
# 1. Buat kalimatnya
tulisan = tk.Label(root, text="Selamat Datang di Sistem Kasir")

# 2. Masukkan ke dalam window agar muncul
tulisan.pack()
# ---------------------

root.mainloop()
