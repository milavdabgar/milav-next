---
title: "Arch Linux Minimal Installation with KDE Plasma"
date: 2023-03-05
description: "A comprehensive guide for installing Arch Linux with KDE Plasma desktop environment"
summary: "Learn how to install and configure Arch Linux with a complete KDE Plasma desktop environment from scratch."
tags: ["linux", "arch", "kde", "installation", "tutorial"]
---

This guide walks you through a complete Arch Linux installation with KDE Plasma desktop environment. It covers everything from partitioning to configuring a fully functional desktop system.

## Pre-installation Steps

### 1. Verify Internet Connection

First, check if your device is connected to the internet. If you're using Wi-Fi, you'll need to connect using the `wifi-menu` utility:

```bash
# Test internet connection
ping -c 3 google.com

# Connect to Wi-Fi if needed
wifi-menu

# Verify connection after connecting
ping -c 3 google.com
```

### 2. Disk Partitioning

You can either pre-partition your disk with GParted or use `cfdisk` from the Arch boot media. Here's a recommended partition scheme:

- `/dev/sda1` - EFI Boot Partition (512MB)
- `/dev/sda2` - BIOS Boot Partition (1MB)
- `/dev/sda3` - Linux Swap Partition (size depends on your RAM)
- Additional partitions for your root filesystem and other needs

In this example, I'm using `/dev/sda12` for the Arch Linux root partition.

```bash
# Launch disk partitioning tool
cfdisk

# Mount partitions
mount /dev/sda12 /mnt
mkdir -p /mnt/boot
mount /dev/sda2 /mnt/boot
mkdir -p /mnt/boot/efi
mount /dev/sda1 /mnt/boot/efi

# Set up swap
mkswap /dev/sda3
swapon /dev/sda3
```

### 3. Optimize Package Repositories

Synchronize package repositories and configure mirror servers to speed up the installation:

```bash
# Update package databases
pacman -Syy

# Install reflector for mirror management
pacman -S reflector

# Find and save the 5 fastest mirrors
reflector --verbose -l 5 --sort rate --save /etc/pacman.d/mirrorlist

# Enable the multilib repository
nano /etc/pacman.conf
```

Add or uncomment these lines in `/etc/pacman.conf`:

```
[multilib]
Include = /etc/pacman.d/mirrorlist
```

Then resynchronize:

```bash
pacman -Syy
```

## Base System Installation

### 1. Install Base System

Install the core Arch Linux packages and generate the filesystem table:

```bash
# Install base packages
pacstrap /mnt base base-devel

# Generate fstab
genfstab -U -p /mnt >> /mnt/etc/fstab
```

### 2. System Configuration

Now, enter the newly installed system with `arch-chroot` and configure it:

```bash
# Change root into the new system
arch-chroot /mnt
```

#### Locale and Time Settings

```bash
# Configure locales
nano /etc/locale.gen
# Uncomment en_US.UTF-8 UTF-8 and other needed locales

# Generate locales
locale-gen

# Set default language
echo LANG=en_US.UTF-8 > /etc/locale.conf
export LANG=en_US.UTF-8

# Set timezone (replace ASIA/KOLKATA with your timezone)
ln -sf /usr/share/zoneinfo/Asia/Kolkata /etc/localtime

# Set hardware clock
hwclock --systohc --utc
```

#### Network Configuration

```bash
# Set hostname
echo planetMilavArch > /etc/hostname
```

#### Package Repositories

Edit `/etc/pacman.conf` to enable multilib and Arch User Repository (AUR):

```bash
nano /etc/pacman.conf
```

Add or uncomment:

```
[multilib]
Include = /etc/pacman.d/mirrorlist
```

Then update package databases:

```bash
pacman -Sy
```

#### User Configuration

Set passwords and create a new user with administrative privileges:

```bash
# Set root password
passwd

# Create a new user
useradd -m -g users -G wheel,storage,power -s /bin/bash milav

# Set user password
passwd milav

# Install sudo
pacman -S sudo

# Configure sudo access
EDITOR=nano visudo
# Uncomment %wheel ALL=(ALL) ALL
```

#### Bootloader Installation

Install and configure GRUB bootloader:

```bash
# Install GRUB
pacman -S grub efibootmgr

# Install GRUB to ESP
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB --recheck

# Generate GRUB configuration
grub-mkconfig -o /boot/grub/grub.cfg
```

#### Network Tools

Install necessary network tools for connectivity after reboot:

```bash
# Install network tools
pacman -S wpa_supplicant dialog networkmanager

# Enable NetworkManager service
systemctl enable NetworkManager

# Test network connection
ping -c 3 google.com
```

## Desktop Environment Installation

Now, let's install the KDE Plasma desktop environment and essential applications:

```bash
# Install Xorg server and applications
pacman -S xorg-server xorg-apps mesa

# Install graphics drivers (adjust for your hardware)
pacman -S xf86-video-intel xf86-video-vesa

# Install display manager
pacman -S sddm

# Install KDE Plasma and applications
pacman -S plasma kde-applications

# Enable display manager service
systemctl enable sddm

# Reboot to apply changes
reboot
```

## Post-Installation Configuration

After rebooting, perform these additional steps to enhance your system:

```bash
# Install bash completion
sudo pacman -S bash-completion

# Enable touchpad support
sudo pacman -S xf86-input-synaptics

# Fix Discover package manager
sudo pacman -S packagekit-qt5

# Install Git for AUR access
sudo pacman -S git

# Install Google Chrome from AUR
git clone https://aur.archlinux.org/google-chrome.git
cd google-chrome/
makepkg -s
sudo pacman -U google-chrome-*.pkg.tar.zst

# Install additional fonts
sudo pacman -S ttf-dejavu noto-fonts
```

## Troubleshooting

If you encounter issues, check the [Arch Wiki](https://wiki.archlinux.org/) for detailed information on specific topics.

For beginners, consider installing an AUR helper like `yay` for easier package management:

```bash
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```

That's it! You now have a fully functional Arch Linux system with KDE Plasma desktop environment. Enjoy the customization and flexibility of Arch Linux!