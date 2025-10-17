#!/usr/bin/env python3

# Author: Arvin Gonzales
# Author ID: reodus.x
# Email: argon@reodus.dev
# Date Created: 2025/09/18
# Purpose: Change default boot OS in grub
# Use case: We're in dual boot and we want Linux to be selected first for boot, not Windows - vice-versa

### open grub file
sudo vim /etc/default/grub			

### save then exit after
GRUB_DEFAULT=#				### change the default value to the order# in boot

### to update the /boot/grub/grub.cfg file
sudo update-grub 	
