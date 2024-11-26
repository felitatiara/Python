username = "ngoding bozt"
password = "cemangat uas"

def login (user_name, pass_word) :
    if user_name != username and pass_word != password:
        hasil = False
    else :
        hasil = True

    return hasil

i=3
while i>=1:
    userName_=input("masukan username anda : ")
    password_=input("masukan password : ")
    hasil=(login(userName_, password_))
    if hasil == True :
        print("\nSelamat Datang di The Voyage Coffe")
        break
    else :
        i-=1
        print("gagal login, sisa percobaan login adalah :", i )
        
print ("===================================================")
pembeli = input("Masukkan nama Pembeli : ")
nmrtelp = str(input("Masukan Nomor Telepon : "))
alamat = str(input("Masukan Nomor Meja : "))
id = [pembeli, nmrtelp, alamat]
print ("\nHalo,", id[0],"!", "\nNomor Telepon :", id[1], "\nNomor Meja :", id[2]) 

menu = [" Kopi Susu - Rp15.000", " Red Velvet - Rp18.000", " Matcha Latte - Rp18.000",
         " Lychee Tea - Rp15.000", " Americano - Rp20.000"]

jml =[]
psn = []

pilihan="yes"
while pilihan=="yes":
    
    print("\n--------------=--- Menu Minuman --------------------")
    for j in range (0, len(menu)):
        print(f"{j+1} {menu[j]}")
    pesan=str(input("Masukan Pilihan (Ketik angka): "))
    jumlahpesan=int(input("Masukkan Jumlah Pesanan = "))
    if pesan == "1":
        listnama= "Kopi Susu"
        harga=(15000*jumlahpesan)
        totalharga=int(harga)
    elif pesan == "2":
        listnama= "Red Velvet"
        harga = (18000*jumlahpesan)
        totalharga =int(harga)
    elif pesan == "3":
        listnama= "Matcha Latte"
        harga=int(18000*jumlahpesan)
        totalharga = int(harga)
    elif pesan == "4":
        listnama= "Lychee Tea"
        harga=int(15000*jumlahpesan)
        totalharga = int(harga)
    elif pesan == "5":
        listnama= "Americano"
        harga=int(20000*jumlahpesan)
        totalharga = int(harga)
    else:
        listnama = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan menu yang tersedia, ulangi kembali (yes/no) =")
 
    print("----------------------------------------------------")
    print("THE VOYAGE COFFEE")
    print("----------------------------------------------------")
    print("Menu : ",listnama)
    print("Jumlah Pesan : ", jumlahpesan)
    print("Harga : ", harga)
    print("----------------------------------------------------")
    print("Jumlah Bayar : ", totalharga)
    print("----------------------------------------------------")

    jml.append(totalharga)
    sum(jml)
    psn.append(jumlahpesan)
    sum(psn)

    pilihan=input("apakah anda ingin order kembali (yes/no) = ")

def linearsearch(via, pilih):
    for i in range(len(via)):
        if via[i] == pilih:
            return i
    return -1
via = ["cash", "debit", "qris"]

def struk():
    print("\nTotal harus Dibayar: Rp",sum(jml))
    print("========================================")
    for x in range (0, len(via)):
        print(f"{x+1} {via[x]}")
    pilih = str(input("Pilih metode pembayaran : "))
    idx = linearsearch(via, pilih)
    if pilih == "cash":
        uang=int(input("Uang Tunai Pembeli: Rp "))
        kembalian=int(uang-sum(jml))
        print("Kembalian :",kembalian)
        print("\n========================================")
        print("========== S T R U K   B E L I =========")
        print("========================================")
        print ("Nama\t\t:",pembeli)
        print ("Beli\t\t:",sum(psn),pesan,"( Rp", sum(jml),")")
        print ("Tagihan\t\t: Rp",sum(jml))
        print ("Dibayar\t\t: Rp",uang)
        print ("Kembalian\t: Rp",kembalian)
        print("========================================")
        print("========================================")
    elif pilih == "debit":
        print ("Masukkan kartu anda")
        print(input("Masukkan PIN kartu anda : "))
        print("\n========================================")
        print("========== S T R U K   B E L I =========")
        print("========================================")
        print ("Nama\t\t:",pembeli)
        print ("Beli\t\t:",sum(psn),pesan,"( Rp", sum(jml),")")
        print ("Tagihan\t\t: Rp",sum(jml))
        print ("Dibayar\t\t: Rp", sum(jml))
        print("========================================")
        print("========================================")
    elif pilih == "qris":
        print ("Silahkan pindai barcode diatas")
        print ("Masukkan nominal yang harus di bayarkan : ")
        print ("Masukkan Password anda : ")
        print("\n========================================")
        print("========== S T R U K   B E L I =========")
        print("========================================")
        print ("Nama\t\t:",pembeli)
        print ("Beli\t\t:",sum(psn),pesan,"( Rp", sum(jml),")")
        print ("Tagihan\t\t: Rp",sum(jml))
        print ("Dibayar\t\t: Rp", sum(jml))
        print("========================================")
        print("========================================")
    else :
        print ("Maaf metode pembayaran tidak ada, silahkan mengulangi pemesanan")

if pilihan == "no":
        jalankan = struk()

print ("Terima kasih !!!")

exit = input ("\nLOG OUT (yes/no) : ")
if exit =="yes":
    print("Terima Kasih sudah Memesan! Sampai Jumpa !")
elif exit =="no":
    login ()