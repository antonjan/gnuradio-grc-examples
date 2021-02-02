#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Eshail-2 QO-100 Satellite recever.
# Author: Anton Janovsky ZR6AIC
# Description: This is an SSB Recever of the Ehail-2 QO-100 Satellite
# Generated: Sun Apr 26 18:51:54 2020
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
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class Eshail_QO_100_Recever_rtl(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Eshail-2 QO-100 Satellite recever.")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.tuner = tuner = -1300
        self.filter_width = filter_width = 1.2e3
        self.volume = volume = .8
        self.variable_static_text_0 = variable_static_text_0 = int((14.2e6+tuner-(2*filter_width))/1e3)
        self.variable_slider_RX_freq = variable_slider_RX_freq = 739.739e6
        self.variable_slider_1 = variable_slider_1 = 0.01
        self.variable_chooser_1 = variable_chooser_1 = 1
        self.variable_chooser_0 = variable_chooser_0 = 0
        self.samp_rate_0 = samp_rate_0 = 250000
        self.samp_rate = samp_rate = 300000
        self.gain = gain = 10000
        self.decimate = decimate = 5
        self.center_freq = center_freq = 14.2e6
        self.agc_decay = agc_decay = 65e-6
        self.agc_attack = agc_attack = .1

        ##################################################
        # Blocks
        ##################################################
        _volume_sizer = wx.BoxSizer(wx.VERTICAL)
        self._volume_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	label='volume',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._volume_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_volume_sizer, 0, 0, 1, 4)
        _variable_slider_RX_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._variable_slider_RX_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_variable_slider_RX_freq_sizer,
        	value=self.variable_slider_RX_freq,
        	callback=self.set_variable_slider_RX_freq,
        	label='RX Frequency',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._variable_slider_RX_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_variable_slider_RX_freq_sizer,
        	value=self.variable_slider_RX_freq,
        	callback=self.set_variable_slider_RX_freq,
        	minimum=739.600e6,
        	maximum=739.800e6,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_variable_slider_RX_freq_sizer)
        self._variable_chooser_1_chooser = forms.radio_buttons(
        	parent=self.GetWin(),
        	value=self.variable_chooser_1,
        	callback=self.set_variable_chooser_1,
        	label='CW Filter',
        	choices=[0,1, 2,3],
        	labels=["900","500","200","SSB"],
        	style=wx.RA_HORIZONTAL,
        )
        self.Add(self._variable_chooser_1_chooser)
        self._variable_chooser_0_chooser = forms.radio_buttons(
        	parent=self.GetWin(),
        	value=self.variable_chooser_0,
        	callback=self.set_variable_chooser_0,
        	label='Modelation',
        	choices=[0, 1],
        	labels=["SSB","AM"],
        	style=wx.RA_HORIZONTAL,
        )
        self.Add(self._variable_chooser_0_chooser)
        _tuner_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tuner_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tuner_sizer,
        	value=self.tuner,
        	callback=self.set_tuner,
        	label='Tune',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tuner_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tuner_sizer,
        	value=self.tuner,
        	callback=self.set_tuner,
        	minimum=-25e3,
        	maximum=25e3,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_tuner_sizer)
        _gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_gain_sizer,
        	value=self.gain,
        	callback=self.set_gain,
        	label='gain',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_gain_sizer,
        	value=self.gain,
        	callback=self.set_gain,
        	minimum=0,
        	maximum=30000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.GridAdd(_gain_sizer, 0, 5, 1, 4)
        _agc_decay_sizer = wx.BoxSizer(wx.VERTICAL)
        self._agc_decay_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_agc_decay_sizer,
        	value=self.agc_decay,
        	callback=self.set_agc_decay,
        	label='AGC Decay',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._agc_decay_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_agc_decay_sizer,
        	value=self.agc_decay,
        	callback=self.set_agc_decay,
        	minimum=10e-6,
        	maximum=100e-6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_agc_decay_sizer, 0, 32, 1, 10)
        _agc_attack_sizer = wx.BoxSizer(wx.VERTICAL)
        self._agc_attack_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_agc_attack_sizer,
        	value=self.agc_attack,
        	callback=self.set_agc_attack,
        	label='AGC Attack',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._agc_attack_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_agc_attack_sizer,
        	value=self.agc_attack,
        	callback=self.set_agc_attack,
        	minimum=1e-1,
        	maximum=3e-1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_agc_attack_sizer, 0, 20, 1, 10)
        self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_c(
        	self.GetWin(),
        	baseband_freq=variable_slider_RX_freq,
        	dynamic_range=100,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate/decimate,
        	fft_size=512,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='Spectrum',
        )
        self.Add(self.wxgui_waterfallsink2_0.win)
        self.wxgui_fftsink2_1 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=variable_slider_RX_freq+tuner-filter_width,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate/25,
        	fft_size=1024,
        	fft_rate=10,
        	average=False,
        	avg_alpha=None,
        	title='Filtered Signal',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_1.win)
        self._variable_static_text_0_static_text = forms.static_text(
        	parent=self.GetWin(),
        	value=self.variable_static_text_0,
        	callback=self.set_variable_static_text_0,
        	label='Frequency',
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._variable_static_text_0_static_text, 0, 9, 1, 10)
        _variable_slider_1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._variable_slider_1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_variable_slider_1_sizer,
        	value=self.variable_slider_1,
        	callback=self.set_variable_slider_1,
        	label='Audio gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._variable_slider_1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_variable_slider_1_sizer,
        	value=self.variable_slider_1,
        	callback=self.set_variable_slider_1,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_variable_slider_1_sizer)
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=decimate,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=16,
                decimation=10,
                taps=None,
                fractional_bw=None,
        )
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '  rtl=0' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(variable_slider_RX_freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(10, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.freq_xlating_fft_filter_ccc_0 = filter.freq_xlating_fft_filter_ccc(decimate, (firdes.low_pass(1, 50e3 ,filter_width-200, 300)), tuner-filter_width, samp_rate/decimate)
        self.freq_xlating_fft_filter_ccc_0.set_nthreads(1)
        self.freq_xlating_fft_filter_ccc_0.declare_sample_delay(0)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((volume, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((gain, ))
        (self.blocks_multiply_const_vxx_0).set_block_alias("RF Gain")
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blks2_selector_0_0 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=variable_chooser_0,
        	output_index=0,
        )
        self.blks2_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=1,
        	num_outputs=2,
        	input_index=0,
        	output_index=variable_chooser_0,
        )
        self.band_pass_filter_2 = filter.fir_filter_fff(1, firdes.band_pass(
        	1, 12000, 600, 800, 50, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_1 = filter.fir_filter_fff(1, firdes.band_pass(
        	1, 12000, 450, 950, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(1, firdes.band_pass(
        	1, 12000, 300, 1100, 100, firdes.WIN_HAMMING, 6.76))
        self.audio_sink_0 = audio.sink(16000, '', True)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate/(decimate*decimate), analog.GR_COS_WAVE, filter_width, .5, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate/(decimate*decimate), analog.GR_SIN_WAVE, filter_width, .5, 0)
        self.analog_am_demod_cf_0 = analog.am_demod_cf(
        	channel_rate=60000,
        	audio_decim=16000,
        	audio_pass=5000,
        	audio_stop=5500,
        )
        self.analog_agc2_xx_0 = analog.agc2_cc(agc_attack, agc_decay, .3, 1)
        self.analog_agc2_xx_0.set_max_gain(1)
        self.CW_selector_1 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=4,
        	num_outputs=1,
        	input_index=variable_chooser_1,
        	output_index=0,
        )
        self.CW_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=1,
        	num_outputs=4,
        	input_index=0,
        	output_index=variable_chooser_1,
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.CW_selector_0, 3), (self.CW_selector_1, 3))
        self.connect((self.CW_selector_0, 2), (self.band_pass_filter_0, 0))
        self.connect((self.CW_selector_0, 0), (self.band_pass_filter_1, 0))
        self.connect((self.CW_selector_0, 1), (self.band_pass_filter_2, 0))
        self.connect((self.CW_selector_1, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.analog_am_demod_cf_0, 0), (self.blks2_selector_0_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.band_pass_filter_0, 0), (self.CW_selector_1, 2))
        self.connect((self.band_pass_filter_1, 0), (self.CW_selector_1, 0))
        self.connect((self.band_pass_filter_2, 0), (self.CW_selector_1, 1))
        self.connect((self.blks2_selector_0, 1), (self.analog_am_demod_cf_0, 0))
        self.connect((self.blks2_selector_0, 0), (self.freq_xlating_fft_filter_ccc_0, 0))
        self.connect((self.blks2_selector_0_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.CW_selector_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blks2_selector_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.wxgui_waterfallsink2_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blks2_selector_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_throttle_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.freq_xlating_fft_filter_ccc_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.freq_xlating_fft_filter_ccc_0, 0), (self.wxgui_fftsink2_1, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_multiply_const_vxx_0, 0))

    def get_tuner(self):
        return self.tuner

    def set_tuner(self, tuner):
        self.tuner = tuner
        self._tuner_slider.set_value(self.tuner)
        self._tuner_text_box.set_value(self.tuner)
        self.wxgui_fftsink2_1.set_baseband_freq(self.variable_slider_RX_freq+self.tuner-self.filter_width)
        self.set_variable_static_text_0(int((14.2e6+self.tuner-(2*self.filter_width))/1e3))
        self.freq_xlating_fft_filter_ccc_0.set_center_freq(self.tuner-self.filter_width)

    def get_filter_width(self):
        return self.filter_width

    def set_filter_width(self, filter_width):
        self.filter_width = filter_width
        self.wxgui_fftsink2_1.set_baseband_freq(self.variable_slider_RX_freq+self.tuner-self.filter_width)
        self.set_variable_static_text_0(int((14.2e6+self.tuner-(2*self.filter_width))/1e3))
        self.freq_xlating_fft_filter_ccc_0.set_taps((firdes.low_pass(1, 50e3 ,self.filter_width-200, 300)))
        self.freq_xlating_fft_filter_ccc_0.set_center_freq(self.tuner-self.filter_width)
        self.analog_sig_source_x_1.set_frequency(self.filter_width)
        self.analog_sig_source_x_0.set_frequency(self.filter_width)

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self._volume_slider.set_value(self.volume)
        self._volume_text_box.set_value(self.volume)
        self.blocks_multiply_const_vxx_1.set_k((self.volume, ))

    def get_variable_static_text_0(self):
        return self.variable_static_text_0

    def set_variable_static_text_0(self, variable_static_text_0):
        self.variable_static_text_0 = variable_static_text_0
        self._variable_static_text_0_static_text.set_value(self.variable_static_text_0)

    def get_variable_slider_RX_freq(self):
        return self.variable_slider_RX_freq

    def set_variable_slider_RX_freq(self, variable_slider_RX_freq):
        self.variable_slider_RX_freq = variable_slider_RX_freq
        self._variable_slider_RX_freq_slider.set_value(self.variable_slider_RX_freq)
        self._variable_slider_RX_freq_text_box.set_value(self.variable_slider_RX_freq)
        self.wxgui_waterfallsink2_0.set_baseband_freq(self.variable_slider_RX_freq)
        self.wxgui_fftsink2_1.set_baseband_freq(self.variable_slider_RX_freq+self.tuner-self.filter_width)
        self.osmosdr_source_0.set_center_freq(self.variable_slider_RX_freq, 0)

    def get_variable_slider_1(self):
        return self.variable_slider_1

    def set_variable_slider_1(self, variable_slider_1):
        self.variable_slider_1 = variable_slider_1
        self._variable_slider_1_slider.set_value(self.variable_slider_1)
        self._variable_slider_1_text_box.set_value(self.variable_slider_1)

    def get_variable_chooser_1(self):
        return self.variable_chooser_1

    def set_variable_chooser_1(self, variable_chooser_1):
        self.variable_chooser_1 = variable_chooser_1
        self._variable_chooser_1_chooser.set_value(self.variable_chooser_1)
        self.CW_selector_1.set_input_index(int(self.variable_chooser_1))
        self.CW_selector_0.set_output_index(int(self.variable_chooser_1))

    def get_variable_chooser_0(self):
        return self.variable_chooser_0

    def set_variable_chooser_0(self, variable_chooser_0):
        self.variable_chooser_0 = variable_chooser_0
        self._variable_chooser_0_chooser.set_value(self.variable_chooser_0)
        self.blks2_selector_0_0.set_input_index(int(self.variable_chooser_0))
        self.blks2_selector_0.set_output_index(int(self.variable_chooser_0))

    def get_samp_rate_0(self):
        return self.samp_rate_0

    def set_samp_rate_0(self, samp_rate_0):
        self.samp_rate_0 = samp_rate_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_waterfallsink2_0.set_sample_rate(self.samp_rate/self.decimate)
        self.wxgui_fftsink2_1.set_sample_rate(self.samp_rate/25)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate/(self.decimate*self.decimate))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate/(self.decimate*self.decimate))

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self._gain_slider.set_value(self.gain)
        self._gain_text_box.set_value(self.gain)
        self.blocks_multiply_const_vxx_0.set_k((self.gain, ))

    def get_decimate(self):
        return self.decimate

    def set_decimate(self, decimate):
        self.decimate = decimate
        self.wxgui_waterfallsink2_0.set_sample_rate(self.samp_rate/self.decimate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate/(self.decimate*self.decimate))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate/(self.decimate*self.decimate))

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq

    def get_agc_decay(self):
        return self.agc_decay

    def set_agc_decay(self, agc_decay):
        self.agc_decay = agc_decay
        self._agc_decay_slider.set_value(self.agc_decay)
        self._agc_decay_text_box.set_value(self.agc_decay)
        self.analog_agc2_xx_0.set_decay_rate(self.agc_decay)

    def get_agc_attack(self):
        return self.agc_attack

    def set_agc_attack(self, agc_attack):
        self.agc_attack = agc_attack
        self._agc_attack_slider.set_value(self.agc_attack)
        self._agc_attack_text_box.set_value(self.agc_attack)
        self.analog_agc2_xx_0.set_attack_rate(self.agc_attack)


def main(top_block_cls=Eshail_QO_100_Recever_rtl, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
