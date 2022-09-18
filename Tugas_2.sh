#!/bin/bash

echo -n "Masukkan Nama Anda: ";
read nama 
echo -n "Masukkan nilai Matematika anda: ";
read mtk;
echo -n "Masukkan nilai IPA anda: ";
read ipa;
echo -n "Masukkan nilai B.Inggris anda: ";
read bing;

let jumlah=$mtk+$ipa+$bing

if [ $jumlah -gt 300 ]
then
  echo " Mohon maaf, ada kesalahan saat menginput niali"
elif [ $jumlah -eq 300 ]
then
  echo " Selamat $nama, Anda Lolos tanpa syarat "
elif [ $jumlah -ge 215 ]
then 
  echo " Selamat $nama, Anda Lolos bersyarat "
elif [ $jumlah -lt 215 ]
then
  echo " Mohon maaf $nama, Anda tidak lolos "
else
  echo " Nilai tidak memenuhi "
fi
