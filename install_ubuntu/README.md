Use balena etcher
After install, disable lid close suspend on laptop

  sudo nano /etc/systemd/logind.conf

Inside the file uncomment or add

  HandleLidSwitch=ignore

Exit the file and restart logind

  sudo service systemd-logind restart
