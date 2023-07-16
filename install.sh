#!/bin/bash

apt install xclip
apt install python3-tk -y

pip install db-sqlite3
pip install pyperclip
pip install customtkinter

cp -r PassMan/ /usr/lib/passman/
chmod 700 /usr/lib/passman/passman.db
rm -rf PassMan
cp passman /usr/bin/
rm passman
chmod +x /usr/bin/passman
cd ..
rm -rf password-manager-gui-main
