# gnuradio-grc-exsamples

This project will have all my gnuradio grc files<br>
Here is my files for rtl-sdr Lime sdr and hackrf<br>
<br>
If you want a radio design for your application then contact me.
# prerequisite
If you want to decode afsk you need to install https://github.com/dl1ksv/gr-ax25<br>
Restart gnuradio-companion<br>
compile detectmarkspace.grc<br>
close gnuradio-companion<br>
Start gnuradio-companion and open the exsample APRS.grc<br>
your afsk decoder should now work<br>
# if you upgrade your Gnuradio to higer vertion 
run the following command if ou upgrade or downgrade from previose verion of gnuradio before starting gnuradio 3.8 to .3.9 <br>
rm -rf ~/.cache/grc_gnuradio/cache.json<br>
