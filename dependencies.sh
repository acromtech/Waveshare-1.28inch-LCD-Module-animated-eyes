#!/bin/bash

# Vérification des droits super-utilisateur
if [ "$(id -u)" -ne 0 ]; then
    echo "Ce script doit être exécuté avec les privilèges root. Utilisez sudo."
    exit 1
fi

echo "Mise à jour des paquets..."
apt update && apt upgrade -y

echo "Installation des dépendances nécessaires..."
# Python et pip
apt install -y python3 python3-pip python3-dev

# Bibliothèques pour SPI et GPIO
apt install -y python3-spidev python3-rpi.gpio

# Pillow pour la manipulation des images
pip3 install --upgrade pip
pip3 install pillow

# Installation de spidev
if ! python3 -c "import spidev" &>/dev/null; then
    echo "spidev non détecté, installation via pip."
    pip3 install spidev
else
    echo "spidev est déjà installé."
fi

# Configuration SPI (activation si non activé)
if ! grep -q "dtparam=spi=on" /boot/config.txt; then
    echo "Activation de l'interface SPI..."
    echo "dtparam=spi=on" >> /boot/config.txt
    echo "Veuillez redémarrer pour activer SPI si ce n'est pas encore fait."
else
    echo "SPI est déjà activé dans /boot/config.txt."
fi

echo "Téléchargement des fichiers de la librairie Waveshare..."
LIB_DIR="Waveshare-1.28inch-LCD-Module-animated-eyes"
if [ ! -d "$LIB_DIR" ]; then
    git clone https://github.com/waveshare/Waveshare-1.28inch-LCD-Module.git "$LIB_DIR"
    echo "Librairie téléchargée dans $LIB_DIR."
else
    echo "La librairie $LIB_DIR existe déjà."
fi

echo "Nettoyage des fichiers inutiles..."
apt autoremove -y

echo "Installation terminée. Si vous avez activé SPI, pensez à redémarrer le système."
