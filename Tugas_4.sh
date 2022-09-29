#!/bin/bash

echo " Masukkan Angka: "
a=0
read angka

until [ ! $angka -gt $a ]
do
  echo $angka
  angka=$((angka - 2))
done
