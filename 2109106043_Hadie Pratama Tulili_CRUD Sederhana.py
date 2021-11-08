import os


Menu = ['Nasi Goreng','Mie Goreng','Es Kopi Hitam','Es Kopi Susu','Es Kopi Cokelat']


def tambah_menu():
	ulang = 'Y'
	while ulang in('y', 'Y'):
		os.system('cls')
		print("Input List Menu Dari Belakang") 
		nama = (str(input("masukkan nama menu yang ingin ditambahkan : ")))
		Menu.append(nama)
		ulang = input("Menu berhasil ditambahkan !!!\nApakah Anda Ingin Menambahkan menu lagi (Y / T) ? ")

def List_Menu():
    os.system('cls')
    print('==================================================================================')
    print(Menu)
    print('==================================================================================')

def tambah_insert():
    ulang = 'Y'
    while ulang in ('y','Y') :
        os.system('cls')
        print("Input List Menu Di Tengah")
        nama = str(input("Masukkan nama menu yang ingin ditampilkan : "))
        Menu.insert(2,nama)
        ulang = input("Menu berhasil ditambahkan !!!\nApakah Anda Ingin Menambahkan menu lagi (Y / T) ? ")

def update():
	update = -1
	List_Menu()
	edit = int(input("Input Menu yang akan di update ")) 
	for a in range(0, len(Menu)): 
		if edit == Menu[a]: 
				update = a 
				break 
	if(update > -1): 
		print("INPUT MENU YANG DI UPDATE ") 
		Nama = (input("masukkan nama menu : ")) 
		Menu[update] = Nama 
		print("berhasil update menu") 
	else:
         print("Menu tidak ditemukan")
         input("Kembali ke menu utama")




def menu_delete():
    os.system('cls')
    ulang = 'Y'
    while ulang in ('y','Y'):
        hapus = input("Masukkan nama menu yang ingin dihapus : ")
        delete = -1
        for a in range(0, len(Menu)):
            if hapus == Menu[a]:
                delete = a
                break
        if(delete > -1):
            del Menu[delete]
            print(Menu)
            print("Menu telah di hapus")
        else:
            print("Menu tidak di temukan")
        input("Kembali ke Menu Utama")
        pilih()

def menu_remove():
    os.system('cls')
    ulang = 'Y'
    while ulang in ('y','Y'):
        hapus = input("Masukkan nama menu yang ingin dihapus : ")
        delete = -1
        for a in range(0, len(Menu)):
            if hapus == Menu[a]:
                delete = a
                break
        if(delete > -1):
            Menu.remove(hapus)
            print(Menu)
            print("Menu telah di hapus")
        else:
            print("Menu tidak di temukan")
        input("Kembali ke Menu Utama")
        pilih()

def menu_update():
	ubah = -1
	List_Menu()
	edit = str(input("Input Menu yang akan di ubah namanya : ")) 
	for a in range(0, len(Menu)): 
		if edit == Menu[a]: 
				ubah = a 
				break 
	if(ubah > -1): 
		print("INPUT MENU YANG AKAN DI UPDATE ") 
		nama = (input("masukkan nama menu : "))
		Menu[ubah] = nama
		print("berhasil update menu")
	else : print("menu tidak ditemukan")
	input("kembali menu utama") 
    
def pilih():
    print(""" Author
    1.Tambah menu dari belakang
    2.Tambah menu dari tengah
    3.Hapus menu (1)
    4.Hapus_menu (2)
    5.Ubah nama menu
    6.Keluar dari program
    """)
    pilihan = input("Masukkan pilihan : ")
    if pilihan == "1":
        tambah_menu()
        print(Menu)
        pilih()

    elif pilihan == "2":
        tambah_insert()
        print(Menu)
        pilih()

    elif pilihan == "3":
        menu_delete()
        pilih()
    elif pilihan == "4":
        menu_remove()
        pilih()
    elif pilihan == "5":
        os.system('cls')
        menu_update()
        print(Menu)
        pilih()
    elif pilihan == "6":
        os.system('cls')
        print("====================================================")
        print("Terimakasih telah menggunakan program ini :)\nSilahkan datang kembali")
        print("====================================================")
        exit()

List_Menu()
pilih()