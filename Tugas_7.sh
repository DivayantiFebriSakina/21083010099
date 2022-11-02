#!/bin/bash

persegi_panjang() {

        panjang=$p
        lebar=$l
        echo "$panjang"
        echo "$lebar"
}
echo "Masukkan Panjang : "
read panjang
echo "Masukkan Lebar : "
read lebar
let luas=$panjang*$lebar
echo " Luas dari Persegi Panjang tersebut adalah $luas "

