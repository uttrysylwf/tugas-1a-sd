"""Inventaris Produk (CLI) - memakai Hash Table (dict). Jalankan: python main.py"""
from inventaris import InventarisHashTable
from produk import Produk

inv = InventarisHashTable()
inv.tambah_produk(Produk("P001", "Laptop ASUS", "Elektronik", 8500000, 25))
inv.tambah_produk(Produk("P002", "Mouse Wireless", "Aksesoris", 175000, 120))
inv.tambah_produk(Produk("P003", "Kemeja Batik", "Fashion", 225000, 60))

while True:
    print("\n=== INVENTARIS PRODUK ===")
    print("1. Tambah produk\n2. Cari produk\n3. Hapus produk\n4. Tampil semua\n0. Keluar")
    pilih = input("Pilih: ")
    if pilih == "1":
        id_produk = input("ID Produk : ").upper()
        nama = input("Nama      : ")
        kategori = input("Kategori  : ")
        harga = float(input("Harga     : "))
        stok = int(input("Stok      : "))
        if inv.tambah_produk(Produk(id_produk, nama, kategori, harga, stok)):
            print("Produk berhasil ditambahkan.")
        else:
            print("Gagal: ID sudah ada.")
    elif pilih == "2":
        p = inv.cari_produk(input("ID Produk: ").upper())
        print(p if p else "Produk tidak ditemukan.")
    elif pilih == "3":
        ok = inv.hapus_produk(input("ID Produk: ").upper())
        print("Produk dihapus." if ok else "Produk tidak ditemukan.")
    elif pilih == "4":
        for p in inv.daftar_produk():
            print(p)
    elif pilih == "0":
        break
    else:
        print("Menu tidak valid.")
