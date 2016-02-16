#!/bin/bash
echo "########  ########  ####    ########   #######  ##     ## ######## ########"  
echo "##     ## ##     ##  ##     ##     ## ##     ## ##     ## ##       ##     ##"
echo "##     ## ##     ##  ##     ##     ## ##     ## ##     ## ##       ##     ##" 
echo "########  ########   ##     ########  ##     ## ##     ## ######   ########"  
echo "##   ##   ##         ##     ##   ##   ##     ##  ##   ##  ##       ##   ##"   
echo "##    ##  ##         ##     ##    ##  ##     ##   ## ##   ##       ##    ##"  
echo "##     ## ##        ####    ##     ##  #######     ###    ######## ##     ##" 
echo "Starting camera interface"
bash /home/pi/RPi_Cam_Web_Interface/start.sh
echo "Done"
echo "Starting Motor Control interface"
sudo python ./MotorControl.py
