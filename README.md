![passman header](/img/passman-header.png)
---
<div align="center">

![version](https://img.shields.io/badge/version-Alpha-31A472)
![language](https://img.shields.io/badge/language-Python-404040)
![license](https://img.shields.io/badge/license-MIT-lightgrey)
![build](https://img.shields.io/badge/build-passing-31A472)

</div>

**#passman** is a password generator and manager built using **Python** and **SQLite3**. It has a nice GUI made with **customtkinter** and it features a little *mod* of the *ctk_optionmenu* widget to add a placeholder text. You'll have to add this *mod* to be able to use it. 

Here's my repo with the modification: 

> **NOTE:**
>
> It's not a final version as I coded it as a 24h. straight coding challenge. The installation is a dirty process and it's not correct by any means. The point of this repo is to share it with the community and see how far can it go with other's modifications. **Please, feel free to fork it and share your improvements.**

![passman showcase](/img/showcase.png)

## Instalation
![Tested](https://img.shields.io/badge/Tested_In-Ubuntu-orange)
![Tested](https://img.shields.io/badge/Tested_In-Kali_Linux-blue)

I'd rather say **"installation"** as it only moves files and creates the files for execution ease. By executing the `install.sh` script, it will: 
1. Install the required dependencies and modules
2. Copy the main folder into `/usr/lib/passman/`
3. Grant required permissions to the database
4. Copy the CLI command file into `/usr/bin/`
5. Grant required permissions to the command file
6. Delete files

As you can see it's not a proper installation and this is just a workaround build for this *Alpha* version aimed to be fixed and improved. To install it just run:

**Ubuntu**

`sudo bash install.sh`

**Kali Linux**

`sudo ./install.sh`

## Use

The first time you execute the program you'll be presented with the **#register** page where you have to register your master user. 

> **NOTE:**
>
> Remember this credentials! If you forget them you may not be able to recover the passwords you save. *I say **may** because I haven't tested the program for security, bugs and workarounds... Yet!*

![register showcase](/img/register-showcase.png)
