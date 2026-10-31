"""Ukur waktu rata-rata (mikrodetik) tambah, cari, hapus. Jalankan: python benchmark.py"""
import json, random, statistics, time
from inventaris import InventarisHashTable, InventarisList, InventarisLinkedList
from produk import Produk

UKURAN = [1000, 10000, 100000]
OPERASI = 100
BACKEND = {"Hash Table (dict)": InventarisHashTable,
           "Array List (list)": InventarisList,
           "Linked List": InventarisLinkedList}


def buat(i):
    return Produk(f"P{i:07d}", f"Produk {i}", "Umum", 10000, 10)


def waktu(fungsi, daftar):
    t = time.perf_counter()
    for x in daftar:
        fungsi(x)
    return (time.perf_counter() - t) / len(daftar) * 1e6


random.seed(42)
hasil = {}
for n in UKURAN:
    semua = [buat(i) for i in range(n)]
    acak = [semua[i].id_produk for i in random.sample(range(n), OPERASI)]
    baru = [buat(n + i) for i in range(OPERASI)]
    hasil[str(n)] = {}
    for nama, kelas in BACKEND.items():
        ukur = {"tambah": [], "cari": [], "hapus": []}
        for _ in range(3):                      # 3 kali ulang, ambil median
            inv = kelas()
            inv.muat(semua)
            ukur["tambah"].append(waktu(inv.tambah_produk, baru))
            ukur["cari"].append(waktu(inv.cari_produk, acak))
            ukur["hapus"].append(waktu(inv.hapus_produk, acak))
        hasil[str(n)][nama] = {k: statistics.median(v) for k, v in ukur.items()}

for op in ("tambah", "cari", "hapus"):
    print(f"\n{op.upper()} (us per operasi)")
    for nama in BACKEND:
        print(f"{nama:<20}" + "".join(f"{hasil[str(n)][nama][op]:>14.2f}" for n in UKURAN))
json.dump(hasil, open("hasil_benchmark.json", "w"), indent=2)
