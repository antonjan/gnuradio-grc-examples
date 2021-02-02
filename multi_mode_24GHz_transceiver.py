#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: 24 GHz Multi-mode transceiver ver7
# Author: John Petrich, W7FU 7-15-17
# Description: multi-mode single band transceiver
# Generated: Mon Jan 11 22:08:08 2021
##################################################


if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from gnuradio.wxgui import forms
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import threading
import time
import wx


class multi_mode_24GHz_transceiver(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="24 GHz Multi-mode transceiver ver7")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.pre_set = pre_set = ((144.240e6)*0+144.299e6)*0+125.250e6
        self.tune = tune = 0
        self.rit = rit = 0
        self.lo_freq_ssb = lo_freq_ssb = (144.1e6,144.2e6,222.100e6,432.100e6-200,902.100e6-271,1296.100e6-300,pre_set)
        self.fine_tune = fine_tune = 0
        self.chooser_ssb = chooser_ssb = 0
        self.variable_static_text_1 = variable_static_text_1 = '{:.0f}'.format(lo_freq_ssb[chooser_ssb]+tune+fine_tune+rit)
        self.variable_function_probe_0 = variable_function_probe_0 = 0
        self.var_text = var_text = pre_set
        self.var_bw = var_bw = 1
        self.tx_rx = tx_rx = 0,1
        self.tx_mode = tx_mode = 0,0,1,1
        self.tx_gain = tx_gain = 0.825
        self.tx_corr = tx_corr = 0,0,580,580
        self.sq = sq = -120
        self.side_band = side_band = 2
        self.sb_t = sb_t = 1,-1,1,1
        self.sb_r = sb_r = -1,1,1,-1
        self.rx_corr = rx_corr = 0,0,580,0
        self.rate = rate = 1500000
        self.mode = mode = 1,1,1,1
        self.mic_gain = mic_gain = 1.5
        self.fft_corr = fft_corr = 0,0,580,0
        self.cw_corr = cw_corr = 0,0,580,0
        self.corr = corr = -348
        self.chooser = chooser = 1
        self.bpf_low = bpf_low = 100,100,380,480
        self.bpf_high = bpf_high = 3900,2700,880,680
        self.af_gain = af_gain = 210
        self.RX_power_offset_dB = RX_power_offset_dB = -104
        self.B200_gain = B200_gain = .1

        ##################################################
        # Blocks
        ##################################################
        _tx_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tx_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tx_gain_sizer,
        	value=self.tx_gain,
        	callback=self.set_tx_gain,
        	label='TX Gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tx_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tx_gain_sizer,
        	value=self.tx_gain,
        	callback=self.set_tx_gain,
        	minimum=.0,
        	maximum=1.0,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_tx_gain_sizer, 6, 0, 1, 1)
        self._side_band_chooser = forms.radio_buttons(
        	parent=self.GetWin(),
        	value=self.side_band,
        	callback=self.set_side_band,
        	label='   MODE',
        	choices=[0,1,2,3],
        	labels=['USB','LSB','CW','USB/CW'],
        	style=wx.RA_HORIZONTAL,
        )
        self.GridAdd(self._side_band_chooser, 3, 2, 1, 1)
        _mic_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._mic_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_mic_gain_sizer,
        	value=self.mic_gain,
        	callback=self.set_mic_gain,
        	label='   MIC Gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._mic_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_mic_gain_sizer,
        	value=self.mic_gain,
        	callback=self.set_mic_gain,
        	minimum=0,
        	maximum=4,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_mic_gain_sizer, 6, 1, 1, 1)
        self._chooser_chooser = forms.button(
        	parent=self.GetWin(),
        	value=self.chooser,
        	callback=self.set_chooser,
        	label='   TX-RX',
        	choices=[1,0],
        	labels=["RECEIVE ","TRANSMIT"],
        )
        self.GridAdd(self._chooser_chooser, 2, 2, 1, 1)
        self._variable_static_text_1_static_text = forms.static_text(
        	parent=self.GetWin(),
        	value=self.variable_static_text_1,
        	callback=self.set_variable_static_text_1,
        	label='                                       IF TRANSCEIVE FREQUENCY',
        	converter=forms.str_converter(),
        )
        self.GridAdd(self._variable_static_text_1_static_text, 1, 1, 1, 1)

        def _variable_function_probe_0_probe():
            while True:
                val = self.blocks_probe_signal_x_0.level()
                try:
                    self.set_variable_function_probe_0(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (35))
        _variable_function_probe_0_thread = threading.Thread(target=_variable_function_probe_0_probe)
        _variable_function_probe_0_thread.daemon = True
        _variable_function_probe_0_thread.start()

        self._var_text_static_text = forms.static_text(
        	parent=self.GetWin(),
        	value=self.var_text,
        	callback=self.set_var_text,
        	label='     IF PRESET FREQUENCY',
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._var_text_static_text, 1, 2, 1, 1)
        self._var_bw_chooser = forms.radio_buttons(
        	parent=self.GetWin(),
        	value=self.var_bw,
        	callback=self.set_var_bw,
        	label='   RECEIVER BANDWIDTH - kHz',
        	choices=[0,1,2,3],
        	labels=['3.9','2.7','0.5','0.2'],
        	style=wx.RA_HORIZONTAL,
        )
        self.GridAdd(self._var_bw_chooser, 4, 2, 1, 1)
        _tune_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tune_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tune_sizer,
        	value=self.tune,
        	callback=self.set_tune,
        	label='  TUNE',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tune_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tune_sizer,
        	value=self.tune,
        	callback=self.set_tune,
        	minimum=-20000,
        	maximum=20000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_tune_sizer, 2, 0, 1, 2)
        _sq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._sq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_sq_sizer,
        	value=self.sq,
        	callback=self.set_sq,
        	label='   SQUELCH',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._sq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_sq_sizer,
        	value=self.sq,
        	callback=self.set_sq,
        	minimum=-120,
        	maximum=-58,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_sq_sizer, 4, 1, 1, 1)
        _rit_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rit_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rit_sizer,
        	value=self.rit,
        	callback=self.set_rit,
        	label='   RIT',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rit_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rit_sizer,
        	value=self.rit,
        	callback=self.set_rit,
        	minimum=-500,
        	maximum=500,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_rit_sizer, 4, 0, 1, 1)
        self.pfb_interpolator_ccf_0 = pfb.interpolator_ccf(
        	  8,
        	  (),
        	  100)
        self.pfb_interpolator_ccf_0.declare_sample_delay(0)

        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + 'hackrf' )
        self.osmosdr_sink_0.set_sample_rate(1000000)
        self.osmosdr_sink_0.set_center_freq(2.40049e9, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(10, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)

        _fine_tune_sizer = wx.BoxSizer(wx.VERTICAL)
        self._fine_tune_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_fine_tune_sizer,
        	value=self.fine_tune,
        	callback=self.set_fine_tune,
        	label='  FINE TUNE',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._fine_tune_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_fine_tune_sizer,
        	value=self.fine_tune,
        	callback=self.set_fine_tune,
        	minimum=-1200,
        	maximum=1200,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_fine_tune_sizer, 3, 0, 1, 2)
        self._chooser_ssb_chooser = forms.radio_buttons(
        	parent=self.GetWin(),
        	value=self.chooser_ssb,
        	callback=self.set_chooser_ssb,
        	label='SSB - CW   FREQUENCY SELECT',
        	choices=[0,1],
        	labels=['24.191','IF PRESET FREQUENCY'],
        	style=wx.RA_HORIZONTAL,
        )
        self.GridAdd(self._chooser_ssb_chooser, 1, 0, 1, 1)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, 48000,True)
        self.blocks_multiply_const_vxx_2_0 = blocks.multiply_const_vcc((tx_gain, ))
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vcc((.78, ))
        self.blocks_multiply_const_vxx_1_0_0 = blocks.multiply_const_vff((mic_gain, ))
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vff((sb_t[side_band], ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((sb_t[side_band], ))
        self.blocks_float_to_complex_0_2 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blks2_selector_0_0 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=tx_mode[side_band],
        	output_index=0,
        )
        self.blks2_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=1*0+1,
        	num_outputs=1,
        	input_index=tx_rx[chooser],
        	output_index=0,
        )
        self.band_pass_filter_0 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	20, 48000, 200, 3000, 100, firdes.WIN_BLACKMAN, 6.76))
        self.audio_source_0_0 = audio.source(48000, 'hw:0,1', True)
        self.analog_const_source_x_0_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, .950)
        _af_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._af_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_af_gain_sizer,
        	value=self.af_gain,
        	callback=self.set_af_gain,
        	label='  AF GAIN',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._af_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_af_gain_sizer,
        	value=self.af_gain,
        	callback=self.set_af_gain,
        	minimum=.1,
        	maximum=1000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_af_gain_sizer, 5, 0, 1, 1)
        _B200_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._B200_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_B200_gain_sizer,
        	value=self.B200_gain,
        	callback=self.set_B200_gain,
        	label='   RF GAIN',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._B200_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_B200_gain_sizer,
        	value=self.B200_gain,
        	callback=self.set_B200_gain,
        	minimum=.1,
        	maximum=.69,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_B200_gain_sizer, 5, 1, 1, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.audio_source_0_0, 0), (self.blocks_multiply_const_vxx_1_0_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_complex_to_float_0_0, 0))
        self.connect((self.blks2_selector_0, 0), (self.pfb_interpolator_ccf_0, 0))
        self.connect((self.blks2_selector_0_0, 0), (self.blocks_multiply_const_vxx_2_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_complex_0_2, 1))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.blocks_float_to_complex_0_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 1), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.blocks_multiply_const_vxx_2, 0))
        self.connect((self.blocks_float_to_complex_0_2, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_float_to_complex_0_2, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_float_to_complex_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blks2_selector_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_2_0, 0), (self.blks2_selector_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.blks2_selector_0_0, 1))
        self.connect((self.pfb_interpolator_ccf_0, 0), (self.osmosdr_sink_0, 0))

    def get_pre_set(self):
        return self.pre_set

    def set_pre_set(self, pre_set):
        self.pre_set = pre_set
        self.set_var_text(self.pre_set)
        self.set_lo_freq_ssb((144.1e6,144.2e6,222.100e6,432.100e6-200,902.100e6-271,1296.100e6-300,self.pre_set))

    def get_tune(self):
        return self.tune

    def set_tune(self, tune):
        self.tune = tune
        self.set_variable_static_text_1('{:.0f}'.format(self.lo_freq_ssb[self.chooser_ssb]+self.tune+self.fine_tune+self.rit))
        self._tune_slider.set_value(self.tune)
        self._tune_text_box.set_value(self.tune)

    def get_rit(self):
        return self.rit

    def set_rit(self, rit):
        self.rit = rit
        self.set_variable_static_text_1('{:.0f}'.format(self.lo_freq_ssb[self.chooser_ssb]+self.tune+self.fine_tune+self.rit))
        self._rit_slider.set_value(self.rit)
        self._rit_text_box.set_value(self.rit)

    def get_lo_freq_ssb(self):
        return self.lo_freq_ssb

    def set_lo_freq_ssb(self, lo_freq_ssb):
        self.lo_freq_ssb = lo_freq_ssb
        self.set_variable_static_text_1('{:.0f}'.format(self.lo_freq_ssb[self.chooser_ssb]+self.tune+self.fine_tune+self.rit))

    def get_fine_tune(self):
        return self.fine_tune

    def set_fine_tune(self, fine_tune):
        self.fine_tune = fine_tune
        self.set_variable_static_text_1('{:.0f}'.format(self.lo_freq_ssb[self.chooser_ssb]+self.tune+self.fine_tune+self.rit))
        self._fine_tune_slider.set_value(self.fine_tune)
        self._fine_tune_text_box.set_value(self.fine_tune)

    def get_chooser_ssb(self):
        return self.chooser_ssb

    def set_chooser_ssb(self, chooser_ssb):
        self.chooser_ssb = chooser_ssb
        self.set_variable_static_text_1('{:.0f}'.format(self.lo_freq_ssb[self.chooser_ssb]+self.tune+self.fine_tune+self.rit))
        self._chooser_ssb_chooser.set_value(self.chooser_ssb)

    def get_variable_static_text_1(self):
        return self.variable_static_text_1

    def set_variable_static_text_1(self, variable_static_text_1):
        self.variable_static_text_1 = variable_static_text_1
        self._variable_static_text_1_static_text.set_value(self.variable_static_text_1)

    def get_variable_function_probe_0(self):
        return self.variable_function_probe_0

    def set_variable_function_probe_0(self, variable_function_probe_0):
        self.variable_function_probe_0 = variable_function_probe_0

    def get_var_text(self):
        return self.var_text

    def set_var_text(self, var_text):
        self.var_text = var_text
        self._var_text_static_text.set_value(self.var_text)

    def get_var_bw(self):
        return self.var_bw

    def set_var_bw(self, var_bw):
        self.var_bw = var_bw
        self._var_bw_chooser.set_value(self.var_bw)

    def get_tx_rx(self):
        return self.tx_rx

    def set_tx_rx(self, tx_rx):
        self.tx_rx = tx_rx
        self.blks2_selector_0.set_input_index(int(self.tx_rx[self.chooser]))

    def get_tx_mode(self):
        return self.tx_mode

    def set_tx_mode(self, tx_mode):
        self.tx_mode = tx_mode
        self.blks2_selector_0_0.set_input_index(int(self.tx_mode[self.side_band]))

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self._tx_gain_slider.set_value(self.tx_gain)
        self._tx_gain_text_box.set_value(self.tx_gain)
        self.blocks_multiply_const_vxx_2_0.set_k((self.tx_gain, ))

    def get_tx_corr(self):
        return self.tx_corr

    def set_tx_corr(self, tx_corr):
        self.tx_corr = tx_corr

    def get_sq(self):
        return self.sq

    def set_sq(self, sq):
        self.sq = sq
        self._sq_slider.set_value(self.sq)
        self._sq_text_box.set_value(self.sq)

    def get_side_band(self):
        return self.side_band

    def set_side_band(self, side_band):
        self.side_band = side_band
        self._side_band_chooser.set_value(self.side_band)
        self.blocks_multiply_const_vxx_0_0_0.set_k((self.sb_t[self.side_band], ))
        self.blocks_multiply_const_vxx_0_0.set_k((self.sb_t[self.side_band], ))
        self.blks2_selector_0_0.set_input_index(int(self.tx_mode[self.side_band]))

    def get_sb_t(self):
        return self.sb_t

    def set_sb_t(self, sb_t):
        self.sb_t = sb_t
        self.blocks_multiply_const_vxx_0_0_0.set_k((self.sb_t[self.side_band], ))
        self.blocks_multiply_const_vxx_0_0.set_k((self.sb_t[self.side_band], ))

    def get_sb_r(self):
        return self.sb_r

    def set_sb_r(self, sb_r):
        self.sb_r = sb_r

    def get_rx_corr(self):
        return self.rx_corr

    def set_rx_corr(self, rx_corr):
        self.rx_corr = rx_corr

    def get_rate(self):
        return self.rate

    def set_rate(self, rate):
        self.rate = rate

    def get_mode(self):
        return self.mode

    def set_mode(self, mode):
        self.mode = mode

    def get_mic_gain(self):
        return self.mic_gain

    def set_mic_gain(self, mic_gain):
        self.mic_gain = mic_gain
        self._mic_gain_slider.set_value(self.mic_gain)
        self._mic_gain_text_box.set_value(self.mic_gain)
        self.blocks_multiply_const_vxx_1_0_0.set_k((self.mic_gain, ))

    def get_fft_corr(self):
        return self.fft_corr

    def set_fft_corr(self, fft_corr):
        self.fft_corr = fft_corr

    def get_cw_corr(self):
        return self.cw_corr

    def set_cw_corr(self, cw_corr):
        self.cw_corr = cw_corr

    def get_corr(self):
        return self.corr

    def set_corr(self, corr):
        self.corr = corr

    def get_chooser(self):
        return self.chooser

    def set_chooser(self, chooser):
        self.chooser = chooser
        self._chooser_chooser.set_value(self.chooser)
        self.blks2_selector_0.set_input_index(int(self.tx_rx[self.chooser]))

    def get_bpf_low(self):
        return self.bpf_low

    def set_bpf_low(self, bpf_low):
        self.bpf_low = bpf_low

    def get_bpf_high(self):
        return self.bpf_high

    def set_bpf_high(self, bpf_high):
        self.bpf_high = bpf_high

    def get_af_gain(self):
        return self.af_gain

    def set_af_gain(self, af_gain):
        self.af_gain = af_gain
        self._af_gain_slider.set_value(self.af_gain)
        self._af_gain_text_box.set_value(self.af_gain)

    def get_RX_power_offset_dB(self):
        return self.RX_power_offset_dB

    def set_RX_power_offset_dB(self, RX_power_offset_dB):
        self.RX_power_offset_dB = RX_power_offset_dB

    def get_B200_gain(self):
        return self.B200_gain

    def set_B200_gain(self, B200_gain):
        self.B200_gain = B200_gain
        self._B200_gain_slider.set_value(self.B200_gain)
        self._B200_gain_text_box.set_value(self.B200_gain)


def main(top_block_cls=multi_mode_24GHz_transceiver, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
