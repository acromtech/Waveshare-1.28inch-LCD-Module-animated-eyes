# Animated-eyes-Waveshare-1.28inch-LCD-Module-with-RaspberryPi-3B

**Ubuntu Server 22.10 (32bit) on RaspberryPi 3B+**

**Basic information**

You can easly run the program with the command below :

```
sudo python3 animatedEyes.py
```

**Pin connection**

```
EPD  	=>	RPI(BCM)
VCC    	->    	5V
GND    	->    	GND
DIN    	->    	10(SPI0_MOSI)
CLK    	->    	11(SPI0_SCK)
CS     	->    	8(CE0)
DC     	->    	25
RST    	->    	27
BL  	->    	18
```

**Installation library**

```
sudo apt-get update
sudo apt-get install python3-pip
sudo apt-get install python3-pil
sudo apt-get install python3-numpy
sudo pip3 install RPi.GPIO
```
