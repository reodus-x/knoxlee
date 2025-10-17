#!/usr/bin/env python3

# Author: Arvin Gonzales
# Author ID: reodus.x
# EMail: argon@reodus.dev
# Date Created: 2025/10/16
# Purpose: INSTALL Guest Additions to Ubuntu or other linux  distros
# Use case: For vm screen resize, and activate the clipboard/drag-drop enabled VMs

# install dependencies
sudo apt install build-essential dkms linux-headers-$(uname -r)

# Ubuntu should auto-mount the disc as /media//VBox_GAs_* - after doing below: 
Click: Devices > Insert Guest Additions CD image...   ### In VBox menu

cd /media/$USER/VBox_GAs_*/       # go to the media directory

sudo ./VBoxLinuxAdditions.run     # install 
sudo usermod -aG vboxsf $USER     

### then reboot

### With this, we now can adjust screen resolution/size
### Make sure to enable clipboard and drag/drop settings in vbox
