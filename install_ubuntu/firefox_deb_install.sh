#!/bin/bash

set -e

echo "🔧 Rimozione Firefox Snap (se presente)..."
sudo snap remove firefox || echo "Firefox Snap non trovato o già rimosso."

echo "🧹 Rimozione pacchetti snap e stub..."
sudo apt purge -y firefox
sudo rm -f /etc/apt/preferences.d/mozilla-firefox

echo "🚫 Blocco del pacchetto Snap..."
echo 'Package: snapd
Pin: release a=*
Pin-Priority: -10
' | sudo tee /etc/apt/preferences.d/nosnap.pref

echo "📦 Rimozione Snapd (facoltativa ma consigliata)..."
sudo apt purge -y snapd

echo "📦 Aggiunta del PPA di Mozilla..."
sudo add-apt-repository -y ppa:mozillateam/ppa
sudo apt update

echo "📌 Impostazione priorità al PPA Mozilla..."
echo '
Package: firefox*
Pin: release o=LP-PPA-mozillateam
Pin-Priority: 501
' | sudo tee /etc/apt/preferences.d/mozillateam-firefox

echo "✅ Installazione di Firefox classico (deb)..."
sudo apt install -y firefox

echo "🔍 Verifica: Firefox installato da:"
readlink -f $(which firefox)

echo "🎉 Installazione completata!"
