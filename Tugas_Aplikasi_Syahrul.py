import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Data Awal
list_data = []

def show_menu():
    clear_screen()
    print("===Aplikasi Kontak===")
    print("1. Lihat Data")
    print("2. Tambah Data")
    print("3. Edit Data")
    print("4. Hapus Data")
    print("5. Exit")
    print("-------------------------------------------------")
    
    menu = input("Pilih menu : ")
    if menu == '1':
        menu1()
    elif menu == '2':
        menu2()
    elif menu == '3':
        menu3()
    elif menu == '4':
        menu4()
    elif menu == '5':
        print("Terima Kasih Telah Berkunjung")
        exit()
    else:
        print("Menu yang anda masukan tidak tersedia")
        kembali()

def menu1():
    print("     NIM          ||         Nama     ")
    print("=======================================")
    if len(list_data) <= 0:
        print("Data Masih Kosong")
    else:
        for data in list_data:
            nim = data[0]
            nama = data[1]
            print(nim+"       -      "+nama)
    kembali()

def menu2():
    nim = str(input("Masukan NIM Anda : "))
    nama = input("Masukkan Nama Anda : ")
    list_data.append([nim, nama])
    print("NIM dan Nama berhasil ditambahkan")
    kembali()

def menu3():
    nim = str(input("Masukan Nomor NIM yang ingin diubah : "))
    index = cari_index(nim)
    if index == -1:
        print("NIM tidak ditemukan")
    else:
        nama_lama = list_data[index][1]
        nama_baru = input("Masukan Nama Baru : ")
        list_data[index][1] = nama_baru
        print("Nama Telah Dirubah")
    kembali()

def menu4():
    nim = str(input("Masukan Nomor NIM yang ingin dihapus : "))
    index = cari_index(nim)
    if index == -1:
        print("NIM tidak ditemukan")
    else:
        nama = list_data[index][1]
        del list_data[index]
        print("Data Berhasil Dihapus")
    kembali()

def cari_index(nim):
    for i, data in enumerate(list_data):
        if data[0] == nim:
            return i
    return -1

def kembali():
    print("\n")
    input("Tekan Enter untuk Kembali...")
    show_menu()

while(True):
    show_menu()