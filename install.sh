#!/bin/bash

apt install xclip
apt install python3-tk -y

pip install db-sqlite3
pip install pyperclip
pip install customtkinter

cp -r PassMan/ /usr/lib/passman/
chmod 700 /usr/lib/passman/passman.db
cp passman /usr/bin/
chmod +x /usr/bin/passman
cp passman-uninstall /usr/bin/
chmod +x /usr/bin/passman-uninstall
cd ..
rm -rf password-manager-gui-main
