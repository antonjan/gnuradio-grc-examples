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
# SDR DVB-S Transmitter
#
# script file to generate a transport stream with the internal camera at a given symbol rate :
# 125, 250, 500, 1000 or 2000 at a fix FEC = 5/6
# send the SR and FEC parameters to the gnuradio DVB-S Transmitter (dvbs_tx_var_v4.py)
# 
# requirements :
#
# - SDR hardware (demo was done with a Ettus USRP B200)
# - the GNURadio toolkit (https://www.gnuradio.org/)
# - the FFmpeg  toolkit (https://www.ffmpeg.org/about.html)
# - a little bit of pugnacity...
#
 

killall -9 ffmpeg >/dev/null 2>/dev/null
killall python2 >/dev/null 2>/dev/null
rm fifo.ts
mkfifo fifo.ts

TYPE="quiet"

PID_VIDEO="33"
PID_AUDIO="49"
PID_PMT="0x0022"
PID_START="0X0121"
ID_TS="1000"
ID_SERVICE="1"
SERVICE_PROVIDER="GNURadio-DVB-S"
SERVICE_NAME="HB9DUG"


FORMAT_VIDEO=""
RATE_VIDEO=""
AUDIO_ON="0"
RATE_AUDIO=""
RATE_MUX=""
GNURADIO_PROG=""

FEC="5/6"

SYMBOL_RATE=""

clear
echo
echo -n "Symbol rate [KS/s]: "
read SYMBOL_RATE_NUM
echo

SYMBOL_RATE="SR"$SYMBOL_RATE_NUM



case "$SYMBOL_RATE" in
	SR125)
	AUDIO_ON="0" 
	FORMAT_VIDEO="160x120"
	RATE_VIDEO="0.100M"
	RATE_AUDIO=""
	RATE_MUX="191993"
	;;
	SR250) 
	AUDIO_ON="0" 
	FORMAT_VIDEO="320x240"
	RATE_VIDEO="0.320M"
	RATE_AUDIO=""
	RATE_MUX="383987"
	;;
	SR500)
	AUDIO_ON="1" 
	FORMAT_VIDEO="320x240"
	RATE_VIDEO="0.600M"
	RATE_AUDIO=""
	RATE_MUX="767974"
	;;
	SR1000)
	AUDIO_ON="1" 
	FORMAT_VIDEO="640x480"
	RATE_VIDEO="1.250M"
	RATE_AUDIO=""
	RATE_MUX="1535948"
	;;
	SR2000) 
	AUDIO_ON="1" 
	FORMAT_VIDEO="640x480"
	RATE_VIDEO="2.7M"
	RATE_AUDIO=""
	RATE_MUX="3071895"
	;;
	
esac

echo "----------------------------------------------------------------------"
echo "DVB-S - Symbol rate [KS/s]: $SYMBOL_RATE  FEC: $FEC  TS rate [Mb/s]: $RATE_MUX"
echo "----------------------------------------------------------------------"


sleep 2

if [ "$AUDIO_ON" == 1 ]; then
# ******************************* MPEG-2 VIDEO WITH BEEP ************************************
ffmpeg -loglevel $TYPE -analyzeduration 0 -probesize 2048 -ac 1 -f lavfi -thread_queue_size 512 -i "sine=frequency=500:beep_factor=4:sample_rate=48000:duration=3600" \
-r 15 -f v4l2 -s $FORMAT_VIDEO -i /dev/video0 -fflags nobuffer -pix_fmt yuv420p -c:v mpeg2video \
-b:v $RATE_VIDEO -minrate $RATE_VIDEO -maxrate $RATE_VIDEO -bufsize $RATE_VIDEO \
-acodec mp2 -ab 64K -ar 48k -ac 1 \
-f mpegts -blocksize 1880 -strict experimental \
-mpegts_transport_stream_id $ID_TS \
-mpegts_pmt_start_pid $PID_PMT \
-mpegts_start_pid $PID_START \
-streamid 0:$PID_VIDEO \
-streamid 1:$PID_AUDIO \
-metadata service_provider=$SERVICE_PROVIDER \
-metadata service_name=$SERVICE_NAME \
-muxrate $RATE_MUX \
-y fifo.ts &

else

# ******************************* MPEG-2 VIDEO WITHOUT AUDIO ********************************
ffmpeg -loglevel $TYPE -analyzeduration 0 -probesize 2048 -thread_queue_size 512 \
-r 15 -f v4l2 -s $FORMAT_VIDEO -i /dev/video0 -fflags nobuffer -pix_fmt yuv420p -c:v mpeg2video \
-b:v $RATE_VIDEO -minrate $RATE_VIDEO -maxrate $RATE_VIDEO -bufsize $RATE_VIDEO \
-f mpegts -blocksize 1880 -strict experimental \
-mpegts_transport_stream_id $ID_TS \
-mpegts_pmt_start_pid $PID_PMT \
-mpegts_start_pid $PID_START \
-streamid 0:$PID_VIDEO \
-streamid 1:$PID_AUDIO \
-metadata service_provider=$SERVICE_PROVIDER \
-metadata service_name=$SERVICE_NAME \
-muxrate $RATE_MUX \
-y fifo.ts &
#********************************************************************************************
fi

sleep 1

./dvbs_tx_var_v4.py -sr $SYMBOL_RATE_NUM -vr $FEC >/dev/null 2>/dev/null &

sleep 1
echo ""
echo ""
echo -n "*** Press enter to stop transmitting at any time ***"
read var_n

killall -9 ffmpeg >/dev/null 2>/dev/null
killall python2 >/dev/null 2>/dev/null

sleep 1

echo ""
echo "Stopped encoding."
echo ""







