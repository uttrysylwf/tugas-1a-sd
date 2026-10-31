from dataclasses import dataclass


@dataclass
class Produk:
    id_produk: str
    nama: str
    kategori: str
    harga: float
    stok: int
