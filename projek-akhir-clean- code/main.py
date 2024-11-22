import os
from tools import loading
from auth import login, register

# start menu
def menu():
    while True:
        print("\nSelamat Datang di E-GUDANG ELEKTRONIK\n 1.register\n 2.Login\n 3.Exit ")
        try:
            opsi = int(input("\nPilih opsi: "))
            os.system('cls || clear')
            if opsi == 1:
                register.register()
                input("Tekan enter untuk kembali ke menu utama")
                loading.loading_efek()
                os.system('cls || clear')
            elif opsi == 2:
                login.login()
                loading.loading_efek()
                os.system('cls || clear')
            elif opsi == 3:
                print("Terima kasih telah mengunjungi E-GUDANG\nProgram akan keluar")
                loading.loading_efek()
                os.system('cls || clear')
                break
            else:
                print("Opsi tidak valid. Silakan pilih 1,2 dan 3")
        # except ValueError:
        #     print("Input tidak valid. Harap masukkan angka.")
        except KeyboardInterrupt:
            print("\nKeluar dari program secara paksa.")
            break

if __name__ == "__main__":
    menu()
