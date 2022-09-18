#!/bin/bash

#deklarasi Array
distrolinux=("Mint" "Ubuntu" "Kali" "Arch" "Debbian")

#random distro
let pilih=$RANDOM%5

#eksekusi
echo "saya memiliih distro $pilih, ${distroLinux[$pilih]} !"
