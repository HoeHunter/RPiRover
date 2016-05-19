#!/bin/bash
echo Starting wifi session
screen -dm -S wifi sudo /usr/sbin/hostapd /etc/hostapd/hostapd.conf
screen -ls
