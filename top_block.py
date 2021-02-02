#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Feb  2 17:12:04 2021
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import osmosdr
import sys
import time
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Variables
        ##################################################
        self.variable_qtgui_range_rf_sine_amp_0 = variable_qtgui_range_rf_sine_amp_0 = 1
        self.variable_qtgui_range_rf_hackrf_BB = variable_qtgui_range_rf_hackrf_BB = 50
        self.variable_qtgui_range_rf_hackrf = variable_qtgui_range_rf_hackrf = 4.8
        self.variable_qtgui_range_rf_cosine_amp = variable_qtgui_range_rf_cosine_amp = 1
        self.variable_qtgui_range_rf_baseband_0 = variable_qtgui_range_rf_baseband_0 = 1
        self.variable_qtgui_range_freq = variable_qtgui_range_freq = 2.40041e9
        self.variable_qtgui_range_Audio_in = variable_qtgui_range_Audio_in = 1
        self.variable_qtgui_chooser_1 = variable_qtgui_chooser_1 = 0
        self.variable_qtgui_chooser_0 = variable_qtgui_chooser_0 = 1
        self.samp_rate_Baseband = samp_rate_Baseband = 50000
        self.samp_rate = samp_rate = 48000

        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_range_rf_sine_amp_0_range = Range(0, 2, 0.1, 1, 200)
        self._variable_qtgui_range_rf_sine_amp_0_win = RangeWidget(self._variable_qtgui_range_rf_sine_amp_0_range, self.set_variable_qtgui_range_rf_sine_amp_0, 'sine amplitude', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_rf_sine_amp_0_win)
        self._variable_qtgui_range_rf_hackrf_BB_range = Range(0, 100, 0.1, 50, 200)
        self._variable_qtgui_range_rf_hackrf_BB_win = RangeWidget(self._variable_qtgui_range_rf_hackrf_BB_range, self.set_variable_qtgui_range_rf_hackrf_BB, 'hackrf rf BB level', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_rf_hackrf_BB_win)
        self._variable_qtgui_range_rf_hackrf_range = Range(0, 120, 0.1, 4.8, 200)
        self._variable_qtgui_range_rf_hackrf_win = RangeWidget(self._variable_qtgui_range_rf_hackrf_range, self.set_variable_qtgui_range_rf_hackrf, 'hackrf rf level', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_rf_hackrf_win)
        self._variable_qtgui_range_rf_cosine_amp_range = Range(0, 2, 0.1, 1, 200)
        self._variable_qtgui_range_rf_cosine_amp_win = RangeWidget(self._variable_qtgui_range_rf_cosine_amp_range, self.set_variable_qtgui_range_rf_cosine_amp, 'Cosine amplitude', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_rf_cosine_amp_win)
        self._variable_qtgui_range_rf_baseband_0_range = Range(0, 5, 0.1, 1, 200)
        self._variable_qtgui_range_rf_baseband_0_win = RangeWidget(self._variable_qtgui_range_rf_baseband_0_range, self.set_variable_qtgui_range_rf_baseband_0, 'baseband rf level', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_rf_baseband_0_win)
        self._variable_qtgui_range_freq_range = Range(2.4e9, 2.4006e9, 1, 2.40041e9, 200)
        self._variable_qtgui_range_freq_win = RangeWidget(self._variable_qtgui_range_freq_range, self.set_variable_qtgui_range_freq, 'Frequency', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_freq_win)
        self._variable_qtgui_range_Audio_in_range = Range(0, 20, 0.01, 1, 200)
        self._variable_qtgui_range_Audio_in_win = RangeWidget(self._variable_qtgui_range_Audio_in_range, self.set_variable_qtgui_range_Audio_in, 'Audio Input', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_Audio_in_win)
        self._variable_qtgui_chooser_1_options = (0, 1, 2, )
        self._variable_qtgui_chooser_1_labels = ('Echolink', '1Kz', 'Wav File', )
        self._variable_qtgui_chooser_1_tool_bar = Qt.QToolBar(self)
        self._variable_qtgui_chooser_1_tool_bar.addWidget(Qt.QLabel('Moselation Input'+": "))
        self._variable_qtgui_chooser_1_combo_box = Qt.QComboBox()
        self._variable_qtgui_chooser_1_tool_bar.addWidget(self._variable_qtgui_chooser_1_combo_box)
        for label in self._variable_qtgui_chooser_1_labels: self._variable_qtgui_chooser_1_combo_box.addItem(label)
        self._variable_qtgui_chooser_1_callback = lambda i: Qt.QMetaObject.invokeMethod(self._variable_qtgui_chooser_1_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._variable_qtgui_chooser_1_options.index(i)))
        self._variable_qtgui_chooser_1_callback(self.variable_qtgui_chooser_1)
        self._variable_qtgui_chooser_1_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_variable_qtgui_chooser_1(self._variable_qtgui_chooser_1_options[i]))
        self.top_grid_layout.addWidget(self._variable_qtgui_chooser_1_tool_bar)
        self._variable_qtgui_chooser_0_options = (0, 1, )
        self._variable_qtgui_chooser_0_labels = ('TX', 'RX', )
        self._variable_qtgui_chooser_0_group_box = Qt.QGroupBox('PTT')
        self._variable_qtgui_chooser_0_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._variable_qtgui_chooser_0_button_group = variable_chooser_button_group()
        self._variable_qtgui_chooser_0_group_box.setLayout(self._variable_qtgui_chooser_0_box)
        for i, label in enumerate(self._variable_qtgui_chooser_0_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._variable_qtgui_chooser_0_box.addWidget(radio_button)
        	self._variable_qtgui_chooser_0_button_group.addButton(radio_button, i)
        self._variable_qtgui_chooser_0_callback = lambda i: Qt.QMetaObject.invokeMethod(self._variable_qtgui_chooser_0_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._variable_qtgui_chooser_0_options.index(i)))
        self._variable_qtgui_chooser_0_callback(self.variable_qtgui_chooser_0)
        self._variable_qtgui_chooser_0_button_group.buttonClicked[int].connect(
        	lambda i: self.set_variable_qtgui_chooser_0(self._variable_qtgui_chooser_0_options[i]))
        self.top_grid_layout.addWidget(self._variable_qtgui_chooser_0_group_box)
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=40,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=25,
                decimation=24,
                taps=None,
                fractional_bw=None,
        )
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + 'hackrf' )
        self.osmosdr_sink_0.set_sample_rate(2e6)
        self.osmosdr_sink_0.set_center_freq(variable_qtgui_range_freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(variable_qtgui_range_rf_hackrf, 0)
        self.osmosdr_sink_0.set_if_gain(100, 0)
        self.osmosdr_sink_0.set_bb_gain(variable_qtgui_range_rf_hackrf_BB, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)

        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/pi/gnuradio-grc-examples/test_audio.wav', True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((variable_qtgui_range_rf_baseband_0, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((variable_qtgui_range_Audio_in, ))
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blks2_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=variable_qtgui_chooser_0,
        	output_index=0,
        )
        self.band_pass_filter_0 = filter.fir_filter_ccf(1, firdes.band_pass(
        	1, samp_rate_Baseband, 16.2e3, 19e3, 200, firdes.WIN_HAMMING, 6.76))
        self.audio_source_0 = audio.source(48000, 'hw:0,1', True)
        self.analog_sig_source_x_1_0 = analog.sig_source_f(48000, analog.GR_SIN_WAVE, 1000, 0.6, 0)
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate_Baseband, analog.GR_COS_WAVE, 0, variable_qtgui_range_rf_cosine_amp, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate_Baseband, analog.GR_SIN_WAVE, 16e3, variable_qtgui_range_rf_sine_amp_0, 0)
        self.analog_const_source_x_1 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.Mic_1khz_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=3,
        	num_outputs=1,
        	input_index=variable_qtgui_chooser_1,
        	output_index=0,
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.Mic_1khz_selector_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.analog_const_source_x_1, 0), (self.blks2_selector_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_1_0, 0), (self.Mic_1khz_selector_0, 1))
        self.connect((self.audio_source_0, 0), (self.Mic_1khz_selector_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blks2_selector_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blks2_selector_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.Mic_1khz_selector_0, 2))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_multiply_const_vxx_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_variable_qtgui_range_rf_sine_amp_0(self):
        return self.variable_qtgui_range_rf_sine_amp_0

    def set_variable_qtgui_range_rf_sine_amp_0(self, variable_qtgui_range_rf_sine_amp_0):
        self.variable_qtgui_range_rf_sine_amp_0 = variable_qtgui_range_rf_sine_amp_0
        self.analog_sig_source_x_0.set_amplitude(self.variable_qtgui_range_rf_sine_amp_0)

    def get_variable_qtgui_range_rf_hackrf_BB(self):
        return self.variable_qtgui_range_rf_hackrf_BB

    def set_variable_qtgui_range_rf_hackrf_BB(self, variable_qtgui_range_rf_hackrf_BB):
        self.variable_qtgui_range_rf_hackrf_BB = variable_qtgui_range_rf_hackrf_BB
        self.osmosdr_sink_0.set_bb_gain(self.variable_qtgui_range_rf_hackrf_BB, 0)

    def get_variable_qtgui_range_rf_hackrf(self):
        return self.variable_qtgui_range_rf_hackrf

    def set_variable_qtgui_range_rf_hackrf(self, variable_qtgui_range_rf_hackrf):
        self.variable_qtgui_range_rf_hackrf = variable_qtgui_range_rf_hackrf
        self.osmosdr_sink_0.set_gain(self.variable_qtgui_range_rf_hackrf, 0)

    def get_variable_qtgui_range_rf_cosine_amp(self):
        return self.variable_qtgui_range_rf_cosine_amp

    def set_variable_qtgui_range_rf_cosine_amp(self, variable_qtgui_range_rf_cosine_amp):
        self.variable_qtgui_range_rf_cosine_amp = variable_qtgui_range_rf_cosine_amp
        self.analog_sig_source_x_1.set_amplitude(self.variable_qtgui_range_rf_cosine_amp)

    def get_variable_qtgui_range_rf_baseband_0(self):
        return self.variable_qtgui_range_rf_baseband_0

    def set_variable_qtgui_range_rf_baseband_0(self, variable_qtgui_range_rf_baseband_0):
        self.variable_qtgui_range_rf_baseband_0 = variable_qtgui_range_rf_baseband_0
        self.blocks_multiply_const_vxx_1.set_k((self.variable_qtgui_range_rf_baseband_0, ))

    def get_variable_qtgui_range_freq(self):
        return self.variable_qtgui_range_freq

    def set_variable_qtgui_range_freq(self, variable_qtgui_range_freq):
        self.variable_qtgui_range_freq = variable_qtgui_range_freq
        self.osmosdr_sink_0.set_center_freq(self.variable_qtgui_range_freq, 0)

    def get_variable_qtgui_range_Audio_in(self):
        return self.variable_qtgui_range_Audio_in

    def set_variable_qtgui_range_Audio_in(self, variable_qtgui_range_Audio_in):
        self.variable_qtgui_range_Audio_in = variable_qtgui_range_Audio_in
        self.blocks_multiply_const_vxx_0.set_k((self.variable_qtgui_range_Audio_in, ))

    def get_variable_qtgui_chooser_1(self):
        return self.variable_qtgui_chooser_1

    def set_variable_qtgui_chooser_1(self, variable_qtgui_chooser_1):
        self.variable_qtgui_chooser_1 = variable_qtgui_chooser_1
        self._variable_qtgui_chooser_1_callback(self.variable_qtgui_chooser_1)
        self.Mic_1khz_selector_0.set_input_index(int(self.variable_qtgui_chooser_1))

    def get_variable_qtgui_chooser_0(self):
        return self.variable_qtgui_chooser_0

    def set_variable_qtgui_chooser_0(self, variable_qtgui_chooser_0):
        self.variable_qtgui_chooser_0 = variable_qtgui_chooser_0
        self._variable_qtgui_chooser_0_callback(self.variable_qtgui_chooser_0)
        self.blks2_selector_0.set_input_index(int(self.variable_qtgui_chooser_0))

    def get_samp_rate_Baseband(self):
        return self.samp_rate_Baseband

    def set_samp_rate_Baseband(self, samp_rate_Baseband):
        self.samp_rate_Baseband = samp_rate_Baseband
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate_Baseband, 16.2e3, 19e3, 200, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate_Baseband)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate_Baseband)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)


def main(top_block_cls=top_block, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
