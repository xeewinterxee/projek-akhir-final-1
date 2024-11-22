import pwinput
import csv

def akun_baru():
    try:
        with open("akuns.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return [["admin", "1234", "admin"]] 

def simpan_akun(username, password, role="user"):
    with open("akuns.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password, role])

def register():
    print("\n==== Registrasi Akun User ====")
    username = input("Masukkan username baru: ")
    cek_akun = akun_baru()
    akuna = False

    if not username:
        print("username tidak boleh kosong")
        return
    
    for akun in cek_akun:
        if len(akun) and akun[0] == username:
            akuna = True
            break
    if akuna:
        print("Username telah dipakai, silakan coba lagi")
    else:
        password = pwinput.pwinput("Masukkan password baru: ")
        if not password:
            print("password tidak boleh kosong")
            return
        
        simpan_akun(username, password)
        print(f"Akun Anda berhasil terdaftar dengan ID: {username}")

if __name__ == '__main__':
    register()
