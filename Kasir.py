import os
import sys
total = []

def clear_screen():
    os.system('clear' if(os.name=='nt') else 'clear')


print ("======================================================================")
print ("                                                                      ")
print ("             Selamat Datang di Sistem Perhitungan Diskon              ")
print ("                                                                      ")
print ("======================================================================")

menu = {
    " 1. Takoyaki    ": 15000,
    " 2. Okonomiyaki ": 17000,
    " 3. Sushi Fried ": 21000,
    " 4. Miso Ramen  ": 23000,
    " 5. Dry Ramen   ": 25000,
    " 6. Gyoza       ": 18000,
    " 7. Onigiri     ": 15000,
    " 8. Dango       ": 10000,
    " 9. Mochi       ": 11000,
    " 10. Dorayaki   ": 10000,
    " 11. Ocha       ": 10000
}
print(" ======================= Daftar Menu Jejepangan ====================== ")
for i in menu:
  print( i, "\t Harga : ", menu[i])
print(" Semakin banyak pembelianmu, semakin banyak diskon yang kamu dapat!!!! ")
print("====================================================================== ")


print("--------------------------- Kasir Jejepangan -------------------------")

def daftar_menu():
    print(" Masukkan pembelian customer ")
    kode = int(input(" Masukkan kode menu: "))
    if kode == 1:
      jumlah1 = int(input("Masukkan jumlah pesanan : "))
      total1 = 15000 * jumlah1
      total.append(total1)
      tanya()
    elif kode == 2:
      jumlah2 = int(input("Masukkan jumlah pesanan : "))
      total2 = 17000 * jumlah2
      total.append(total2)
      tanya()
    elif kode == 3:
      jumlah3 = int(input("Masukkan jumlah pesanan : "))
      total3 = 21000 * jumlah3 
      total.append(total3)
      tanya()
    elif kode == 4:
      jumlah4 = int(input("Masukkan jumlah pesanan : "))
      total4 = 23000 * jumlah4
      total.append(total4)
      tanya()
    elif kode == 5:
      jumlah5 = int(input("Masukkan jumlah pesanan : "))
      total5 = 25000 * jumlah5   
      total.append(total5)
      tanya()
    elif kode == 6:
      jumlah6 = int(input("Masukkan jumlah pesanan : "))
      total6 = 18000 * jumlah6
      total.append(total6)
      tanya()
    elif kode == 7:
      jumlah7 = int(input("Masukkan jumlah pesanan : "))
      total7 = 15000 * jumlah7
      total.append(total7)
      tanya()
    elif kode == 8:
      jumlah8 = int(input("Masukkan jumlah pesanan : "))
      total8 = 10000 * jumlah8
      total.append(total8)
      tanya()
    elif kode == 9:
      jumlah9 = int(input("Masukkan jumlah pesanan : "))
      total9 = 11000 * jumlah9
      total.append(total9)
      tanya()
    elif kode == 10:
      jumlah10 = int(input("Masukkan jumlah pesanan : "))
      total10 = 10000 * jumlah10
      total.append(total10)
      tanya()
    elif kode == 11: 
      jumlah11 = int(input("Masukkan jumlah pesanan : "))
      total11 = 10000 * jumlah11
      total.append(total11)
      tanya()
    return

def tanya():
    print("\n-------------------------------")
    tanya = input("Ada tambahan pesanan? [y/t] : ")
    print("-------------------------------")
    if tanya == "y":
        daftar_menu()
    elif tanya == "t":
        akhir()
    else:
        print("Pilihan yang anda masukan salah!")

def akhir():
    for harga in total:
        print("Total Pemesanan              : ", sum(total))
        diskon = 0
        a = sum(total)
        if a > 200000:
            diskon = a * 30/100
        elif a > 180000:
            diskon = a * 20/100
        elif a > 150000:
            diskon = a * 15/100
        elif a > 100000:
            diskon = a * 10/100
        else:
            diskon = 0
        print("Potongan Harga Spesial       : ", diskon)
        pajak = sum(total) * 10/100
        print("PPN 10%                      : ", pajak)
        totalakhir = a - diskon + pajak
        print("Harga setelah diskon         : ", totalakhir)
        print("---------------------------------------------")
        bayar = int(input("Bayar                        : "))
        kembalian = bayar - totalakhir
        print("Kembalian                    : ", kembalian)
        print("---------------------------------------------")
        print("       Terima Kasih Telah berkunjung         ")
        print("---------------------------------------------")
        break

daftar_menu()
