#!/bin/bash

set -e
dir=/media/shagbag913/Roms/factimages
url=$1
ZIP=$(basename ${url})
folder=$(echo ${ZIP} | awk -F-factory '{print $1}')
image=image-${folder}.zip
device=sailfish
savedir=/media/shagbag913/Roms/factimages/${folder}-images
mkdir -p $savedir
cd $dir
wget $url
unzip $ZIP
cd $folder
unzip $image
cp boot.img $savedir/${device}-boot-$(date +%b-%Y)
cp vendor.img $savedir/${device}-vendor-$(date +%b-%Y)
cp radio-${device}*.img $savedir/${device}-radio-$(date +%b-%Y)
cp bootloader-${device}*.img $savedir/${device}-bootloader-$(date +%b-%Y)
rm -rf $dir/$folder
rm -rf $dir/$ZIP
