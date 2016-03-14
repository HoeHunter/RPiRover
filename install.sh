#!/bin/bash
chmod +x rover.sh

echo "Updating the Raspberry Pi"
sudo apt-get update && sudo apt-get upgrade && sudo rpi-update

echo ""
echo "Installing Motor Hat Drivers..."
sudo apt-get install python-smbus git
cd ~/
git clone https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library.git
cd Adafruit-Motor-HAT-Python-Library
sudo apt-get install python-dev
sudo python setup.py install

echo ""
echo "Installing Camera Software"
cd ~/
git clone https://github.com/silvanmelchior/RPi_Cam_Web_Interface.git
cd RPi_Cam_Web_Interface
chmod u+x *.sh
bash /home/pi/RPi_Cam_Web_Interface/install.sh

echo "'
echo "Installation Complete. Run rover.sh to initalize the software."
