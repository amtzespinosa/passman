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

> **⚠️ WARNING:**
>
> **Remember this credentials!** If you forget them you may not be able to recover the passwords you saved. *I say **may** because I haven't tested the program for security, bugs and workarounds... Yet!*

![register showcase](/img/register-showcase.png)

After you register your master user you'll get logged into the main screen which is the **#passgen** screen. Here you can generate a secure random password between 5 and 50 characters. In the panel at the bottom you'll find the password characters and length settings. 

> **EASTER EGG:**
>
> I couldn't help myself and end up hiding an easter egg here!

![passgen showcase](/img/passgen-showcase.png)

By clicking the *Generate* button a new password will be generated and you'll be able to copy it. **I'm having problems with the *Copy* button - I hope I solve it soon. I made it work in *Kali Linux* but not in *Ubuntu*.** You can select and then `Ctrl + C` to copy and `Ctrl + V` to paste it.

Once you have the password in the clipboard you can head to the **Add New** tab.

![add new showcase](/img/add-new-showcase.png)

Once you have filled the fields with the credentials, you can hit *Add* to store the them - you can check them heading to the **List** tab.

And to remove any of the stored passwords you can head to the **Delete** tab. Once there you only need to select the credentials you want to remove and hit the *Delete* button. Regarding the pictures below:

![delete showcase](/img/delete-showcase.png)

The one on the left shows the **customtkinter** *mod* I mentioned at the beginning of this repo in action. Little *mod* but pretty cool in my opinion. And the one on the right shows the dropdown menu. Credentials are removed as soon as you hit *Delete* **BUT** don't worry if you remove one by mistake, due to a coding error, credentials don't get removed straight away - they are completely removed after restarting the program.

And next time you execute it again you'll be prompted with the **#login** screen. Use your master user credentials!

![login showcase](/img/login-showcase.png)

## Known Errors

There are plenty of them for sure but here are some of the most anoying ones I will focus on:

- [ ] **Copy button not working** - pyperclip issue
- [ ] **Dirty code - made to work** but unstable and not properly implemented
- [ ] **Stored password and refreshing issues** - dynamical CTk frames issue
- [ ] **General security issues**

## Future Improvements and Features

- [ ] Add keyboard support - hit `Enter` to login and so on...
- [ ] Confirmation message before credentials deletion
- [ ] Add multiple master users support
- [ ] Add stronger cryptographic security
- [ ] Make it Windows and other OS compatible
- [ ] Cloud-based storage
- [ ] Make it cross-platform - Computer, Android, Web...

## Support or Join the Project!

If you like **#passman** please share it with the community, share your issues and ideas on join me in this project and help me improve it! Anyone interested in this project can join!
