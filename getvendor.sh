#!/usr/bin/env bash
pas=$(cat /media/shagbag913/Roms/.pas)
pushd /tmp
wget $1
mv sailfish*.zip factimg.zip
unzip factimg.zip
cd sailfish*
unzip image*.zip
mv vendor.img /media/shagbag913/Roms/vendorimgs/Sailfish-Vendor-$(date +%b-%Y).img
curl -T /media/shagbag913/Roms/vendorimgs/Sailfish-Vendor-*.img ftp://shagbag913:$pas@uploads.androidfilehost.com
popd
