# Waveshare 1.28inch LCD Module Animated Eyes Powered by Raspberry Pi 4

**Ubuntu Server 22.10 (32bit) on Raspberry Pi 4**

This project uses two displays for "eyes" and an additional display for an animated "mouth," all controlled by a Raspberry Pi 4. The displays are connected to SPI0 and SPI1 interfaces.

---

## **Run the Program Automatically**

To run the program automatically when the Raspberry Pi starts, follow this guide: 
[Launch a Python Script at Startup](https://www.raspberrypi-france.fr/lancer-un-script-python-au-demarrage-du-raspberry-pi/)

---

## **Install Dependencies**

Use the `dependencies.sh` script to automatically install all necessary dependencies.

### **Installation Steps**
1. Execute the script:
   ```bash
   sudo chmod +x dependencies.sh
   sudo ./dependencies.sh
   ```

2. If SPI is being activated for the first time, reboot the Raspberry Pi:
   ```bash
   sudo reboot
   ```

---

## **Hardware Components**

- **Displays**: Waveshare 1.28-inch Round LCD Module x 3 
- **Controller**: Raspberry Pi 4 (Ubuntu Server 22.10, 32-bit) 
- **Power Supply**: 5V/3A USB-C 
- **Cables**: 40-pin GPIO wires 

---

## **Pin Connection**

### **Left Eye Display (SPI0 - Left Eye)**

| Signal | Raspberry Pi Pin | Description          |
|--------|-------------------|----------------------|
| VCC    | Pin 2 (5V)        | Power Supply         |
| GND    | Pin 6 (GND)       | Ground               |
| DIN    | Pin 19 (SPI0 MOSI)| SPI0 Data            |
| CLK    | Pin 23 (SPI0 SCLK)| SPI0 Clock           |
| CS     | Pin 24 (SPI0 CE0) | SPI0 Chip Select 0   |
| DC     | GPIO 25           | Data/Command Select  |
| RST    | GPIO 23           | Reset                |
| BL     | GPIO 18           | Backlight Control    |

### **Right Eye Display (SPI0 - Right Eye)**

| Signal | Raspberry Pi Pin | Description          |
|--------|-------------------|----------------------|
| VCC    | Pin 2 (5V)        | Power Supply         |
| GND    | Pin 6 (GND)       | Ground               |
| DIN    | Pin 19 (SPI0 MOSI)| SPI0 Data            |
| CLK    | Pin 23 (SPI0 SCLK)| SPI0 Clock           |
| CS     | Pin 26 (SPI0 CE1) | SPI0 Chip Select 1   |
| DC     | GPIO 22           | Data/Command Select  |
| RST    | GPIO 27           | Reset                |
| BL     | GPIO 17           | Backlight Control    |

### **Mouth Display (SPI1)**

(Your SPI1 is already activated during dependencies installation)

| Signal | Raspberry Pi Pin | Description          |
|--------|-------------------|----------------------|
| VCC    | Pin 4 (5V)        | Power Supply         |
| GND    | Pin 9 (GND)       | Ground               |
| DIN    | Pin 38 (SPI1 MOSI)| SPI1 Data            |
| CLK    | Pin 40 (SPI1 SCLK)| SPI1 Clock           |
| CS     | Pin 36 (SPI1 CE0) | SPI1 Chip Select 0   |
| DC     | GPIO 35           | Data/Command Select  |
| RST    | GPIO 33           | Reset                |
| BL     | GPIO 31           | Backlight Control    |

---

## **Run the Program**

Once the dependencies are installed and the displays are wired correctly, run the program using:

```bash
sudo python3 main.py
```

---

## **Troubleshooting**

If a display does not work as expected: 
1. Verify the wiring matches the above tables. 
2. Test each display individually with its SPI interface. 
3. Check if SPI interfaces are enabled:
   ```bash
   ls /dev/spi*
   ```
   This should show available SPI interfaces (e.g., `/dev/spidev0.0` and `/dev/spidev1.0`).

---

**Warning:** 
- **Double-check wire colors**, as they may differ from standard expectations. 
- Ensure GPIO pins are available and not used by other devices.
