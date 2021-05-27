#! /bin/bash

# 
# Version 1.0 / 2017-05-01
# 
# Hamradio 2017 - DATV FORUM
#
# All-in-ONE
# A DATV SDR Experimental TX/RX solution
# HB9DUG Michel
#
#
# SDR DVB-S receiver
#
# script file to to decode and display a DVB-S signal at a symbol rate of :
# 125, 250, 500, 1000 or 2000 at a fix FEC = 5/6 and fix frequency = 1280 MHz
# 
# requirements :
#
# - USB SDR dongle (demo was done with a NooElec NESDR Nano2+)
# - the rtl-sdr library (https://osmocom.org/projects/sdr/wiki/rtl-sdr)
# - the leandvb software (http://www.pabr.org/radio/leandvb/leandvb.en.html)
# - VLC media player (https://www.videolan.org/vlc/download-ubuntu.html)
# - a little bit of pugnacity...
#


SAMPLE_RATE="2400e3"
SYMBOL_RATE=""
FEC='5/6'
FREQ="1280e6"


clear
echo "LeanDVB tuner"
echo
echo -n "Symbol rate [KS/s]: "
read SR
echo

let SYMBOL_RATE=SR*1000

echo "-----------------------------------"
echo "Symbol rate [KS/s]: $SR  FEC: $FEC "
echo "-----------------------------------"
echo


rtl_sdr -g 0 -f $FREQ  -s $SAMPLE_RATE - | ./leandvb --gui --sr $SYMBOL_RATE --cr $FEC | vlc - &


sleep 1
echo ""
echo ""
echo -n "*** Press enter to stop receiving at any time ***"
read var_n

killall vlc
killall leandvb
killall rtl_sdr
sleep 1

echo ""
echo "Stopped receiving."
echo ""
