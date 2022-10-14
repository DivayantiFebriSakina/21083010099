#!/bin/bash

declare -a tulis;

echo
echo -n " Masukkan Nama Mahasiswa : "; read nama;
echo -n " Masukkan Batas Semester : "; read ipk;

jumlah=0;
ipk_mhs=0;

for ((i=1; i<=ipk; i++))
do 
  echo
  echo -n " Masukkan nilai IPS Semester $i : "; read tulis[$i];
  let jumlah=$jumlah+${tulis[i]};
  let ipk_mhs=$jumlah/ipk;
done

echo
echo " Nilai IPS Mahasiswa ' $nama ' selama $ipk semester : "
echo " ${tulis[0]} ";
echo
echo " Total keseluruhan dari nilai IPS : " $jumlah;
echo
echo " Nilai IPK Mahasiswa ' $nama ' adalah $ipk_mhs "; 
