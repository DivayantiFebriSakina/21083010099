#!/bin/bash

# inisialisasi var
a=55;
b=4;
distroLinux="Ubuntu 19.04 LTS";
let c=a%b;

#Output Print
printf "OS : $distroLinux \n";
printf "$c \n";
printf "%.2f float \n" $a;
printf "%.lf float \n" $a;
