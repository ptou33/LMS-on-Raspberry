Use balena etcher to burn and install Ubuntu on USB disk
After the installation, first thing to do open a terminal:
## Install sshd

    sudo apt install openssh-server
    sudo service ssh start

From now on you can perfrom the other configurations from remote ssh from Mobaxterm for example


## Disable lid suspend
After install, disable lid close suspend on laptop

    sudo nano /etc/systemd/logind.conf

Inside the file uncomment or add

    HandleLidSwitch=ignore
    HandleLidSwitchExternalPower=ignore
    HandleLidSwitchDocked=ignore


Exit the file and restart logind

    sudo service systemd-logind restart



## Enable smbd

    sudo apt install samba samba-common-bin
    sudo nano /etc/samba/smb.conf



At the end of the file, add:
**smb.conf**

    [DellMedia]
        path = /home/pietro/Media
        read only = no
        public = no
        writable = yes

add share password to existing user

    sudo smbpasswd -a pietro

From now the share is visible on windows

## Install docker
from convenience script

    sudo apt install curl
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
