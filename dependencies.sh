#!/bin/bash

# Check for root privileges
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run with root privileges. Please use sudo."
    exit 1
fi

echo "Updating package list and upgrading existing packages..."
apt update && apt upgrade -y

echo "Installing required dependencies..."

# Libraries and tools
apt install -y python3 python3-pip python3-dev python3-pil python3-numpy python3-rpi.gpio
pip3 install --upgrade pip
pip3 install spidev RPi.GPIO pillow

# SPI configuration (enable if not already active)
if ! grep -q "dtparam=spi=on" /boot/config.txt; then
    echo "Enabling SPI0 interface..."
    echo "dtparam=spi=on" >> /boot/config.txt
fi

if ! grep -q "dtoverlay=spi1-3cs" /boot/config.txt; then
    echo "Enabling SPI1 with 3 Chip Selects..."
    echo "dtoverlay=spi1-3cs" >> /boot/config.txt
fi

echo "Configuration completed."

# Check if a reboot is required
if [ -f /var/run/reboot-required ]; then
    echo "A reboot is required to apply the changes. Rebooting now..."
    reboot
else
    echo "No reboot required. Your Raspberry Pi is ready to use."
fi

