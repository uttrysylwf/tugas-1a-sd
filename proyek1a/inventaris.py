"""Tiga implementasi inventaris dengan operasi yang sama:
tambah_produk, cari_produk, hapus_produk, daftar_produk."""


# 1) Hash Table (dict) -> struktur data terpilih
class InventarisHashTable:
    def __init__(self):
        self.data = {}                      # kunci: id_produk

    def tambah_produk(self, produk):        # O(1)
        if produk.id_produk in self.data:
            return False
        self.data[produk.id_produk] = produk
        return True

    def cari_produk(self, id_produk):       # O(1)
        return self.data.get(id_produk)

    def hapus_produk(self, id_produk):      # O(1)
        return self.data.pop(id_produk, None) is not None

    def daftar_produk(self):
        return list(self.data.values())

    def muat(self, daftar):                 # isi awal (untuk benchmark)
        for p in daftar:
            self.data[p.id_produk] = p


# 2) Array-based List (list)
class InventarisList:
    def __init__(self):
        self.data = []

    def tambah_produk(self, produk):        # O(n): cek duplikat
        if self.cari_produk(produk.id_produk):
            return False
        self.data.append(produk)
        return True

    def cari_produk(self, id_produk):       # O(n)
        for p in self.data:
            if p.id_produk == id_produk:
                return p
        return None

    def hapus_produk(self, id_produk):      # O(n)
        for i, p in enumerate(self.data):
            if p.id_produk == id_produk:
                del self.data[i]
                return True
        return False

    def daftar_produk(self):
        return list(self.data)

    def muat(self, daftar):
        self.data.extend(daftar)


# 3) Linked List (Custom ADT)
class NodeProduk:
    def __init__(self, produk):
        self.produk = produk
        self.next = None


class InventarisLinkedList:
    def __init__(self):
        self.head = None

    def tambah_produk(self, produk):        # O(n): cek duplikat, sisip di head O(1)
        if self.cari_produk(produk.id_produk):
            return False
        node = NodeProduk(produk)
        node.next = self.head
        self.head = node
        return True

    def cari_produk(self, id_produk):       # O(n)
        cur = self.head
        while cur:
            if cur.produk.id_produk == id_produk:
                return cur.produk
            cur = cur.next
        return None

    def hapus_produk(self, id_produk):      # O(n)
        prev, cur = None, self.head
        while cur:
            if cur.produk.id_produk == id_produk:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return True
            prev, cur = cur, cur.next
        return False

    def daftar_produk(self):
        hasil, cur = [], self.head
        while cur:
            hasil.append(cur.produk)
            cur = cur.next
        return hasil

    def muat(self, daftar):
        for p in daftar:
            node = NodeProduk(p)
            node.next = self.head
            self.head = node
