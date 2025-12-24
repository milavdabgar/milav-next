---
title: "KDE પ્લાઝમા સાથે આર્ચ લિનક્સ મિનિમલ ઇન્સ્ટોલેશન"
date: 2023-03-05
description: "KDE પ્લાઝમા ડેસ્કટોપ એન્વાયરમેન્ટ સાથે આર્ચ લિનક્સ ઇન્સ્ટોલ કરવા માટેની વિસ્તૃત માર્ગદર્શિકા"
summary: "શૂન્યથી શરૂ કરીને સંપૂર્ણ KDE પ્લાઝમા ડેસ્કટોપ એન્વાયરમેન્ટ સાથે આર્ચ લિનક્સ કેવી રીતે ઇન્સ્ટોલ અને કોન્ફિગર કરવું તે શીખો."
tags: ["linux", "arch", "kde", "installation", "tutorial"]
---

આ ગાઈડ તમને KDE પ્લાઝમા ડેસ્કટોપ એન્વાયરમેન્ટ સાથે આર્ચ લિનક્સના સંપૂર્ણ ઇન્સ્ટોલેશન દ્વારા લઈ જશે. તે પાર્ટિશનિંગથી લઈને સંપૂર્ણ કાર્યક્ષમ ડેસ્કટોપ સિસ્ટમને કોન્ફિગર કરવા સુધીના બધા પગલાંઓને આવરી લે છે.

## પ્રી-ઇન્સ્ટોલેશન સ્ટેપ્સ

### 1. ઈન્ટરનેટ કનેક્શન ચકાસો

સૌપ્રથમ, તમારું ડિવાઇસ ઈન્ટરનેટ સાથે કનેક્ટ છે કે નહીં તે ચકાસો. જો તમે વાઈ-ફાઈનો ઉપયોગ કરી રહ્યાં છો, તો તમારે `wifi-menu` યુટિલિટીનો ઉપયોગ કરીને કનેક્ટ કરવાની જરૂર પડશે:

```bash
# ઈન્ટરનેટ કનેક્શન ટેસ્ટ કરો
ping -c 3 google.com

# જરૂર હોય તો વાઈ-ફાઈ થી કનેક્ટ થાઓ
wifi-menu

# કનેક્ટ થયા પછી કનેક્શન ચકાસો
ping -c 3 google.com
```

### 2. ડિસ્ક પાર્ટિશનિંગ

તમે GParted દ્વારા તમારી ડિસ્કને પહેલેથી પાર્ટિશન કરી શકો છો અથવા આર્ચ બૂટ મીડિયા પરથી `cfdisk`નો ઉપયોગ કરી શકો છો. અહીં એક સૂચિત પાર્ટિશન સ્કીમ છે:

- `/dev/sda1` - EFI બૂટ પાર્ટિશન (512MB)
- `/dev/sda2` - BIOS બૂટ પાર્ટિશન (1MB)
- `/dev/sda3` - લિનક્સ સ્વેપ પાર્ટિશન (સાઇઝ તમારા RAM પર આધારિત રહેશે)
- તમારા રૂટ ફાઇલસિસ્ટમ અને અન્ય જરૂરિયાતો માટે વધારાના પાર્ટિશન

આ ઉદાહરણમાં, હું આર્ચ લિનક્સ રૂટ પાર્ટિશન માટે `/dev/sda12`નો ઉપયોગ કરી રહ્યો છું.

```bash
# ડિસ્ક પાર્ટિશનિંગ ટૂલ લોન્ચ કરો
cfdisk

# પાર્ટિશન માઉન્ટ કરો
mount /dev/sda12 /mnt
mkdir -p /mnt/boot
mount /dev/sda2 /mnt/boot
mkdir -p /mnt/boot/efi
mount /dev/sda1 /mnt/boot/efi

# સ્વેપ સેટઅપ કરો
mkswap /dev/sda3
swapon /dev/sda3
```

### 3. પેકેજ રિપોઝિટરીઝ ઓપ્ટિમાઇઝ કરો

ઇન્સ્ટોલેશનને ઝડપી બનાવવા માટે પેકેજ રિપોઝિટરીઝને સિંક્રોનાઇઝ કરો અને મિરર સર્વરોને કોન્ફિગર કરો:

```bash
# પેકેજ ડેટાબેસ અપડેટ કરો
pacman -Syy

# મિરર મેનેજમેન્ટ માટે રિફ્લેક્ટર ઇન્સ્ટોલ કરો
pacman -S reflector

# 5 સૌથી ઝડપી મિરર શોધો અને સેવ કરો
reflector --verbose -l 5 --sort rate --save /etc/pacman.d/mirrorlist

# મલ્ટીલિબ રિપોઝિટરી સક્ષમ કરો
nano /etc/pacman.conf
```

`/etc/pacman.conf` માં આ લાઇન્સ ઉમેરો અથવા અનકમેન્ટ કરો:

```
[multilib]
Include = /etc/pacman.d/mirrorlist
```

પછી ફરીથી સિંક્રોનાઇઝ કરો:

```bash
pacman -Syy
```

## બેઝ સિસ્ટમ ઇન્સ્ટોલેશન

### 1. બેઝ સિસ્ટમ ઇન્સ્ટોલ કરો

કોર આર્ચ લિનક્સ પેકેજ ઇન્સ્ટોલ કરો અને ફાઇલસિસ્ટમ ટેબલ જનરેટ કરો:

```bash
# બેઝ પેકેજ ઇન્સ્ટોલ કરો
pacstrap /mnt base base-devel

# ફાઇલસિસ્ટમ ટેબલ (fstab) જનરેટ કરો
genfstab -U -p /mnt >> /mnt/etc/fstab
```

### 2. સિસ્ટમ કોન્ફિગરેશન

હવે, `arch-chroot` સાથે નવી ઇન્સ્ટોલ કરેલી સિસ્ટમમાં પ્રવેશ કરો અને તેને કોન્ફિગર કરો:

```bash
# નવી સિસ્ટમમાં ચેન્જ રૂટ કરો
arch-chroot /mnt
```

#### લોકેલ અને ટાઇમ સેટિંગ્સ

```bash
# લોકેલ કોન્ફિગર કરો
nano /etc/locale.gen
# en_US.UTF-8 UTF-8 અને અન્ય જરૂરી લોકેલ અનકમેન્ટ કરો

# લોકેલ જનરેટ કરો
locale-gen

# ડિફોલ્ટ ભાષા સેટ કરો
echo LANG=en_US.UTF-8 > /etc/locale.conf
export LANG=en_US.UTF-8

# ટાઇમઝોન સેટ કરો (ASIA/KOLKATA ને તમારા ટાઇમઝોન સાથે બદલો)
ln -sf /usr/share/zoneinfo/Asia/Kolkata /etc/localtime

# હાર્ડવેર ક્લોક સેટ કરો
hwclock --systohc --utc
```

#### નેટવર્ક કોન્ફિગરેશન

```bash
# હોસ્ટનેમ સેટ કરો
echo planetMilavArch > /etc/hostname
```

#### પેકેજ રિપોઝિટરીઝ

મલ્ટીલિબ અને આર્ચ યુઝર રિપોઝિટરી (AUR) સક્ષમ કરવા માટે `/etc/pacman.conf` સંપાદિત કરો:

```bash
nano /etc/pacman.conf
```

ઉમેરો અથવા અનકમેન્ટ કરો:

```
[multilib]
Include = /etc/pacman.d/mirrorlist
```

પછી પેકેજ ડેટાબેસ અપડેટ કરો:

```bash
pacman -Sy
```

#### યુઝર કોન્ફિગરેશન

પાસવર્ડ સેટ કરો અને એડમિનિસ્ટ્રેટિવ અધિકારો સાથે નવો યુઝર બનાવો:

```bash
# રૂટ પાસવર્ડ સેટ કરો
passwd

# નવો યુઝર બનાવો
useradd -m -g users -G wheel,storage,power -s /bin/bash milav

# યુઝર પાસવર્ડ સેટ કરો
passwd milav

# સુડો ઇન્સ્ટોલ કરો
pacman -S sudo

# સુડો એક્સેસ કોન્ફિગર કરો
EDITOR=nano visudo
# %wheel ALL=(ALL) ALL અનકમેન્ટ કરો
```

#### બૂટલોડર ઇન્સ્ટોલેશન

GRUB બૂટલોડર ઇન્સ્ટોલ અને કોન્ફિગર કરો:

```bash
# GRUB ઇન્સ્ટોલ કરો
pacman -S grub efibootmgr

# ESP માં GRUB ઇન્સ્ટોલ કરો
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB --recheck

# GRUB કોન્ફિગરેશન જનરેટ કરો
grub-mkconfig -o /boot/grub/grub.cfg
```

#### નેટવર્ક ટૂલ્સ

રિબૂટ પછી કનેક્ટિવિટી માટે જરૂરી નેટવર્ક ટૂલ્સ ઇન્સ્ટોલ કરો:

```bash
# નેટવર્ક ટૂલ્સ ઇન્સ્ટોલ કરો
pacman -S wpa_supplicant dialog networkmanager

# NetworkManager સર્વિસ સક્ષમ કરો
systemctl enable NetworkManager

# નેટવર્ક કનેક્શન ટેસ્ટ કરો
ping -c 3 google.com
```

## ડેસ્કટોપ એન્વાયરમેન્ટ ઇન્સ્ટોલેશન

હવે, KDE પ્લાઝમા ડેસ્કટોપ એન્વાયરમેન્ટ અને અનિવાર્ય એપ્લિકેશન ઇન્સ્ટોલ કરીએ:

```bash
# Xorg સર્વર અને એપ્લિકેશન ઇન્સ્ટોલ કરો
pacman -S xorg-server xorg-apps mesa

# ગ્રાફિક્સ ડ્રાઇવર ઇન્સ્ટોલ કરો (તમારા હાર્ડવેર માટે સમાયોજિત કરો)
pacman -S xf86-video-intel xf86-video-vesa

# ડિસ્પ્લે મેનેજર ઇન્સ્ટોલ કરો
pacman -S sddm

# KDE પ્લાઝમા અને એપ્લિકેશન ઇન્સ્ટોલ કરો
pacman -S plasma kde-applications

# ડિસ્પ્લે મેનેજર સર્વિસ સક્ષમ કરો
systemctl enable sddm

# ફેરફારો લાગુ કરવા માટે રિબૂટ કરો
reboot
```

## પોસ્ટ-ઇન્સ્ટોલેશન કોન્ફિગરેશન

રિબૂટ કર્યા પછી, તમારી સિસ્ટમને વધુ સારી બનાવવા માટે આ વધારાના પગલાં કરો:

```bash
# બેશ કમ્પલીશન ઇન્સ્ટોલ કરો
sudo pacman -S bash-completion

# ટચપેડ સપોર્ટ સક્ષમ કરો
sudo pacman -S xf86-input-synaptics

# ડિસ્કવર પેકેજ મેનેજર ફિક્સ કરો
sudo pacman -S packagekit-qt5

# AUR એક્સેસ માટે Git ઇન્સ્ટોલ કરો
sudo pacman -S git

# AUR માંથી Google Chrome ઇન્સ્ટોલ કરો
git clone https://aur.archlinux.org/google-chrome.git
cd google-chrome/
makepkg -s
sudo pacman -U google-chrome-*.pkg.tar.zst

# વધારાના ફોન્ટ્સ ઇન્સ્ટોલ કરો
sudo pacman -S ttf-dejavu noto-fonts
```

## ટ્રબલશૂટિંગ

જો તમને સમસ્યાઓનો સામનો કરવો પડે, તો ચોક્કસ વિષયો પર વિગતવાર માહિતી માટે [આર્ચ વિકી](https://wiki.archlinux.org/) તપાસો.

શરૂઆતકર્તાઓ માટે, સરળ પેકેજ મેનેજમેન્ટ માટે `yay` જેવા AUR હેલ્પર ઇન્સ્ટોલ કરવાનું વિચારો:

```bash
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```

બસ એટલું જ! તમારી પાસે હવે KDE પ્લાઝમા ડેસ્કટોપ એન્વાયરમેન્ટ સાથે સંપૂર્ણ કાર્યક્ષમ આર્ચ લિનક્સ સિસ્ટમ છે. આર્ચ લિનક્સની કસ્ટમાઇઝેશન અને ફ્લેક્સિબિલિટીનો આનંદ માણો!