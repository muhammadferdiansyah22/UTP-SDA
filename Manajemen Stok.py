import os as os

class NamaBuah:
    def __init__(self):
        self.nama = input("Masukkan Nama Buah   : ")
        self.kode_buah = input("Masukkan Kode Buah   : ")
        self.harga_beli = int(input("Masukkan Harga Beli  : "))
        self.stok = int(input("Masukkan Stok Barang : "))
        print("!!",self.nama, "berhasil ditambahkan ke daftar buah ~")

    def Info_Buah(self):
        print("Nama Buah  : ", self.nama)
        print("Kode Buah  : ", self.kode_buah)
        print("Stok Buah  : ", self.stok,"Kg")
        print("Harga Beli : ", self.harga_beli)
        print("\n")
    
    def Tambah_Stok(self, total):
        self.total = total
        self.stok += total
        print("Stok Buah ", self.nama, "berhasil ditambah sebanyak", total)


class TokoBuah:
    def __init__(self, nama):
        self.nama = nama
        self.list_buah = []

    def header(self):
        print("==================================================")
        print("||      Selamat Datang di Sistem Manajemen      ||")
        print(self.nama)
        print("==================================================\n")

        print("Masukan Data Buah ")
        print("--------------------------------------------------")

    def info_toko(self):
        print("List Buah: ")
        print("--------------------------------------------------")
        for Buah in self.list_buah:
            Buah.Info_Buah()

    def TambahBuah(self):
        Buah = NamaBuah()
        self.list_buah.append(Buah)
        print("\n")

    def CariKodeBuah(self, code):
        for Buah in self.list_buah:
            if Buah.kode_buah.lower() == code.lower():
                return Buah
        return None

    def Total_Harga_Beli(self):
        TotalHarga = 0
        for Buah in self.list_buah:
            TotalHarga = Buah.harga_beli * Buah.stok
        return TotalHarga

    def Total_Harga_Beli2(self, total):
        TotalHarga = 0
        for Buah in self.list_buah:
            if Buah == total:
                TotalHarga += Buah.harga_beli * total
            else:
                TotalHarga += Buah.harga_beli * Buah.stok
        return TotalHarga

if __name__ == "__main__":

    Toko_Buah = TokoBuah("||             Toko Buah_Segar Kita             ||")

    Toko_Buah.header()

    while True:
        Toko_Buah.TambahBuah()
        Pilihan = input("Apakah Anda ingin menambahkan buah lain? (y/n): ")
        print("--------------------------------------------------")
        if Pilihan.lower() == "n":
            break

    Toko_Buah.info_toko()

    print("Mencari Buah")
    print("--------------------------------------------------")
    x=input('Masukkan Kode Buah: ')
    Cari_Buah = Toko_Buah.CariKodeBuah(x)
    print("\n")
    if Cari_Buah:
        print("!! Menemukan buah yang Anda cari: ")
        Cari_Buah.Info_Buah()
    else:
        print("!! Maaf, tidak dapat menemukan buah.")

    total_price_sebelum = Toko_Buah.Total_Harga_Beli()
    Toko_Buah.list_buah[0].Tambah_Stok(int(input("Banyak buah yang Anda inginkan : ")))

    total_price_sesudah = Toko_Buah.Total_Harga_Beli2(Toko_Buah.list_buah[0].total)

    print("\n")
    print("Total Harga Beli")
    print("--------------------------------------------------") 
    print("Total Harga Beli Buah Sebelum Penambahan Stok: ", total_price_sebelum)
    print("Total Harga Beli Buah Sesudah Penambahan Stok: ", total_price_sesudah)
