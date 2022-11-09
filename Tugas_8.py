# Muat built-in libraries yang akan digunakan :
from os import getpid
from time import time, sleep
from multiprocessing import Pool, Process 

# Inisialisasi function yang akan  digunakan :
def cetak(a):
    angka = a % 2
    if angka == 0:
        print(a, "Genap - ID proses", getpid())
    else:
        print(a, "Ganjil - ID proses", getpid())
    sleep(1)

# Menginput bilangan
y = int(input("Input bilangan: "))

# Sekuensial
print("\nPemprosesan Sukensial")
sekuensial_awal = time()

for a in range(1, y + 1):
    cetak(a)

sekuensial_akhir = time()

# Kelas Proses
print("\nMultiprocessing dengan multiprocessing.Process")

kumpulan_proses = []
proses_awal = time()

for a in range(1, y + 1):
    p = Process(target=cetak, args=(a,))
    kumpulan_proses.append(p)
    p.start()

for a in kumpulan_proses:
    p.join()

proses_akhir = time()

# Pool
print("\nMultiprocessing dengan multiprocessing.Pool")
pool_awal = time()

pool = Pool()
pool.map(cetak, range(1, y + 1))
pool.close()

pool_akhir = time()

# Perbandingan waktu eksekusi
print("\nWaktu eksekusi sekuensial            :", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu eksekusi multiprocessing.Process :", proses_akhir - proses_awal, "detik")
print("Waktu eksekusi multiprocessing.Process :", pool_akhir - pool_awal, "detik")  
