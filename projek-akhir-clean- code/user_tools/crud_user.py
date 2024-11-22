import csv
import os
from datetime import datetime,  timedelta
from prettytable import PrettyTable

gudang = os.path.join(os.path.dirname(__file__), '..', 'gudang.csv')
riwayat = os.path.join(os.path.dirname(__file__), '..', 'riwayat.csv')

def lihat_barang():
    try:
        with open(gudang, mode="r", newline='') as file:
            csvreader = csv.DictReader(file)
            data = list(csvreader)
            table = PrettyTable()

            if data:
                table.field_names = data[0].keys()
                for row in data:
                    table.add_row([row["nama barang"], row["tipe barang"], row["stok barang"], row["id"]])
                print(table)
            else:
                print("\nData kosong.")
            
    except FileNotFoundError:
        print("File tidak ditemukan, buat data baru terlebih dahulu.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def peminjaman_barang():
    lihat_barang() 
    id_barang = input("Masukkan ID Barang: ")
    barang_ditemukan = False
    riwayat_row = None

    with open(gudang, mode="r", newline='') as file:
        read = csv.DictReader(file)
        rows = list(read)

        for row in rows:
            if row["id"] == id_barang:
                barang_ditemukan = True
                nama_user = input("Masukkan nama peminjam: ").capitalize()

                try:
                    stok_user = int(input("Berapa stok yang ingin dipinjam (maks 10): "))
                    if 0 < stok_user <= 10:
                        jumlah_hari = int(input("Masukkan jumlah hari peminjaman: "))
                        tanggal_peminjaman = datetime.now()
                        print("Tanggal peminjaman:", tanggal_peminjaman.strftime("%Y-%m-%d"))
                        tanggal_pengembalian = tanggal_peminjaman + timedelta(days=jumlah_hari)
                        print("Tanggal pengembalian:", tanggal_pengembalian.strftime("%Y-%m-%d"))

                        riwayat_row = {
                            "nama": nama_user,
                            "id barang": id_barang,
                            "stok": stok_user,
                            "waktu awal minjam": tanggal_peminjaman.strftime("%Y-%m-%d"),
                            "waktu akhir peminjaman": tanggal_pengembalian.strftime("%Y-%m-%d")
                        }

                        with open('riwayat.csv', 'a', newline='') as file_riwayat:
                            fieldnames = ["nama", "id barang", "stok", "waktu awal minjam", "waktu akhir peminjaman"]
                            writer = csv.DictWriter(file_riwayat, fieldnames=fieldnames)
                            writer.writerow(riwayat_row)

                        print(f"Data barang dengan ID: {id_barang} berhasil dipinjam.")
                        break

                    else:
                        print("Peminjaman barang tidak boleh melebihi 10 stok")

                except ValueError:
                    print("Input tidak valid, harus berupa angka")
                    
    if not barang_ditemukan:
        print(f"Barang dengan ID: {id_barang} tidak ditemukan.")

if __name__ == "__main__":
    lihat_barang()
    peminjaman_barang()