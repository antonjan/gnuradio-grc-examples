#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: SSB Transmitter
# Author: Anton Janovsky ZR6AIC
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
import osmosdr
import time
from gnuradio import qtgui

class SSB_transmitter(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "SSB Transmitter")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("SSB Transmitter")
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

        self.settings = Qt.QSettings("GNU Radio", "SSB_transmitter")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.variable_qtgui_range_RF_out_gain = variable_qtgui_range_RF_out_gain = 10
        self.variable_qtgui_range_Cut_off_freq = variable_qtgui_range_Cut_off_freq = 16000
        self.variable_qtgui_range_Audio_in = variable_qtgui_range_Audio_in = 0.1
        self.variable_qtgui_range_0_1_0 = variable_qtgui_range_0_1_0 = 10352560000
        self.variable_qtgui_range_0_1 = variable_qtgui_range_0_1 = 145500000
        self.variable_qtgui_push_button_CW = variable_qtgui_push_button_CW = 0
        self.variable_qtgui_chooser_PTT_0 = variable_qtgui_chooser_PTT_0 = 0
        self.variable_qtgui_chooser_PTT = variable_qtgui_chooser_PTT = 0
        self.samp_rate_Baseband_Hackrf = samp_rate_Baseband_Hackrf = 2112000
        self.samp_rate_Baseband = samp_rate_Baseband = 192e3
        self.samp_rate_Audio = samp_rate_Audio = 48000

        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_range_RF_out_gain_range = Range(0, 15000, 1, 10, 200)
        self._variable_qtgui_range_RF_out_gain_win = RangeWidget(self._variable_qtgui_range_RF_out_gain_range, self.set_variable_qtgui_range_RF_out_gain, 'RF Out Gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_RF_out_gain_win)
        self._variable_qtgui_range_Cut_off_freq_range = Range(0, 50000, 1, 16000, 200)
        self._variable_qtgui_range_Cut_off_freq_win = RangeWidget(self._variable_qtgui_range_Cut_off_freq_range, self.set_variable_qtgui_range_Cut_off_freq, 'Cut off Freq', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_Cut_off_freq_win)
        self._variable_qtgui_range_Audio_in_range = Range(0, 2, 0.1, 0.1, 200)
        self._variable_qtgui_range_Audio_in_win = RangeWidget(self._variable_qtgui_range_Audio_in_range, self.set_variable_qtgui_range_Audio_in, 'Audio Input Gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_Audio_in_win)
        self._variable_qtgui_range_0_1_range = Range(144000000, 440000000, 1, 145500000, 200)
        self._variable_qtgui_range_0_1_win = RangeWidget(self._variable_qtgui_range_0_1_range, self.set_variable_qtgui_range_0_1, 'Frequency', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_0_1_win)
        _variable_qtgui_push_button_CW_push_button = Qt.QPushButton('cw Key')
        _variable_qtgui_push_button_CW_push_button = Qt.QPushButton('cw Key')
        self._variable_qtgui_push_button_CW_choices = {'Pressed': 1, 'Released': 0}
        _variable_qtgui_push_button_CW_push_button.pressed.connect(lambda: self.set_variable_qtgui_push_button_CW(self._variable_qtgui_push_button_CW_choices['Pressed']))
        _variable_qtgui_push_button_CW_push_button.released.connect(lambda: self.set_variable_qtgui_push_button_CW(self._variable_qtgui_push_button_CW_choices['Released']))
        self.top_grid_layout.addWidget(_variable_qtgui_push_button_CW_push_button)
        # Create the options list
        self._variable_qtgui_chooser_PTT_options = (0, 1, )
        # Create the labels list
        self._variable_qtgui_chooser_PTT_labels = ('TX', 'RX', )
        # Create the combo box
        self._variable_qtgui_chooser_PTT_tool_bar = Qt.QToolBar(self)
        self._variable_qtgui_chooser_PTT_tool_bar.addWidget(Qt.QLabel('PTT' + ": "))
        self._variable_qtgui_chooser_PTT_combo_box = Qt.QComboBox()
        self._variable_qtgui_chooser_PTT_tool_bar.addWidget(self._variable_qtgui_chooser_PTT_combo_box)
        for _label in self._variable_qtgui_chooser_PTT_labels: self._variable_qtgui_chooser_PTT_combo_box.addItem(_label)
        self._variable_qtgui_chooser_PTT_callback = lambda i: Qt.QMetaObject.invokeMethod(self._variable_qtgui_chooser_PTT_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._variable_qtgui_chooser_PTT_options.index(i)))
        self._variable_qtgui_chooser_PTT_callback(self.variable_qtgui_chooser_PTT)
        self._variable_qtgui_chooser_PTT_combo_box.currentIndexChanged.connect(
            lambda i: self.set_variable_qtgui_chooser_PTT(self._variable_qtgui_chooser_PTT_options[i]))
        # Create the radio buttons
        self.top_grid_layout.addWidget(self._variable_qtgui_chooser_PTT_tool_bar)
        self._variable_qtgui_range_0_1_0_range = Range(10338000000, 10702000000, 1, 10352560000, 200)
        self._variable_qtgui_range_0_1_0_win = RangeWidget(self._variable_qtgui_range_0_1_0_range, self.set_variable_qtgui_range_0_1_0, 'Frequency', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_0_1_0_win)
        # Create the options list
        self._variable_qtgui_chooser_PTT_0_options = (0, 1, )
        # Create the labels list
        self._variable_qtgui_chooser_PTT_0_labels = ('TX', 'RX', )
        # Create the combo box
        self._variable_qtgui_chooser_PTT_0_tool_bar = Qt.QToolBar(self)
        self._variable_qtgui_chooser_PTT_0_tool_bar.addWidget(Qt.QLabel('PTT' + ": "))
        self._variable_qtgui_chooser_PTT_0_combo_box = Qt.QComboBox()
        self._variable_qtgui_chooser_PTT_0_tool_bar.addWidget(self._variable_qtgui_chooser_PTT_0_combo_box)
        for _label in self._variable_qtgui_chooser_PTT_0_labels: self._variable_qtgui_chooser_PTT_0_combo_box.addItem(_label)
        self._variable_qtgui_chooser_PTT_0_callback = lambda i: Qt.QMetaObject.invokeMethod(self._variable_qtgui_chooser_PTT_0_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._variable_qtgui_chooser_PTT_0_options.index(i)))
        self._variable_qtgui_chooser_PTT_0_callback(self.variable_qtgui_chooser_PTT_0)
        self._variable_qtgui_chooser_PTT_0_combo_box.currentIndexChanged.connect(
            lambda i: self.set_variable_qtgui_chooser_PTT_0(self._variable_qtgui_chooser_PTT_0_options[i]))
        # Create the radio buttons
        self.top_grid_layout.addWidget(self._variable_qtgui_chooser_PTT_0_tool_bar)
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=11,
                decimation=1,
                taps=None,
                fractional_bw=None)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate_Baseband, #bw
            'RF Out', #name
            1
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + "hackrf"
        )
        self.osmosdr_sink_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_sink_0.set_sample_rate(samp_rate_Baseband_Hackrf)
        self.osmosdr_sink_0.set_center_freq(variable_qtgui_range_0_1 , 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(10, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/anton/gnuradio-grc-examples/test_audio.wav', True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate_Audio,True)
        self.blocks_selector_0_0 = blocks.selector(gr.sizeof_gr_complex*1,variable_qtgui_push_button_CW,0)
        self.blocks_selector_0_0.set_enabled(True)
        self.blocks_selector_0 = blocks.selector(gr.sizeof_gr_complex*1,variable_qtgui_chooser_PTT,0)
        self.blocks_selector_0.set_enabled(True)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_cc(variable_qtgui_range_RF_out_gain)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(variable_qtgui_range_Audio_in)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.band_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.band_pass(
                1,
                samp_rate_Baseband,
                16.3e3,
                19e3,
                200,
                firdes.WIN_HAMMING,
                6.76))
        self.analog_sig_source_x_2 = analog.sig_source_c(samp_rate_Baseband_Hackrf, analog.GR_SIN_WAVE, 800, 1, 0, 0)
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate_Baseband, analog.GR_COS_WAVE, 0, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate_Baseband, analog.GR_SIN_WAVE, variable_qtgui_range_Cut_off_freq, 1, 0, 0)
        self.analog_const_source_x_0_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_selector_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_2, 0), (self.blocks_selector_0_0, 1))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_selector_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_selector_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_selector_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.blocks_selector_0_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_selector_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "SSB_transmitter")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_variable_qtgui_range_RF_out_gain(self):
        return self.variable_qtgui_range_RF_out_gain

    def set_variable_qtgui_range_RF_out_gain(self, variable_qtgui_range_RF_out_gain):
        self.variable_qtgui_range_RF_out_gain = variable_qtgui_range_RF_out_gain
        self.blocks_multiply_const_vxx_1.set_k(self.variable_qtgui_range_RF_out_gain)

    def get_variable_qtgui_range_Cut_off_freq(self):
        return self.variable_qtgui_range_Cut_off_freq

    def set_variable_qtgui_range_Cut_off_freq(self, variable_qtgui_range_Cut_off_freq):
        self.variable_qtgui_range_Cut_off_freq = variable_qtgui_range_Cut_off_freq
        self.analog_sig_source_x_0.set_frequency(self.variable_qtgui_range_Cut_off_freq)

    def get_variable_qtgui_range_Audio_in(self):
        return self.variable_qtgui_range_Audio_in

    def set_variable_qtgui_range_Audio_in(self, variable_qtgui_range_Audio_in):
        self.variable_qtgui_range_Audio_in = variable_qtgui_range_Audio_in
        self.blocks_multiply_const_vxx_0.set_k(self.variable_qtgui_range_Audio_in)

    def get_variable_qtgui_range_0_1_0(self):
        return self.variable_qtgui_range_0_1_0

    def set_variable_qtgui_range_0_1_0(self, variable_qtgui_range_0_1_0):
        self.variable_qtgui_range_0_1_0 = variable_qtgui_range_0_1_0

    def get_variable_qtgui_range_0_1(self):
        return self.variable_qtgui_range_0_1

    def set_variable_qtgui_range_0_1(self, variable_qtgui_range_0_1):
        self.variable_qtgui_range_0_1 = variable_qtgui_range_0_1
        self.osmosdr_sink_0.set_center_freq(self.variable_qtgui_range_0_1 , 0)

    def get_variable_qtgui_push_button_CW(self):
        return self.variable_qtgui_push_button_CW

    def set_variable_qtgui_push_button_CW(self, variable_qtgui_push_button_CW):
        self.variable_qtgui_push_button_CW = variable_qtgui_push_button_CW
        self.blocks_selector_0_0.set_input_index(self.variable_qtgui_push_button_CW)

    def get_variable_qtgui_chooser_PTT_0(self):
        return self.variable_qtgui_chooser_PTT_0

    def set_variable_qtgui_chooser_PTT_0(self, variable_qtgui_chooser_PTT_0):
        self.variable_qtgui_chooser_PTT_0 = variable_qtgui_chooser_PTT_0
        self._variable_qtgui_chooser_PTT_0_callback(self.variable_qtgui_chooser_PTT_0)

    def get_variable_qtgui_chooser_PTT(self):
        return self.variable_qtgui_chooser_PTT

    def set_variable_qtgui_chooser_PTT(self, variable_qtgui_chooser_PTT):
        self.variable_qtgui_chooser_PTT = variable_qtgui_chooser_PTT
        self._variable_qtgui_chooser_PTT_callback(self.variable_qtgui_chooser_PTT)
        self.blocks_selector_0.set_input_index(self.variable_qtgui_chooser_PTT)

    def get_samp_rate_Baseband_Hackrf(self):
        return self.samp_rate_Baseband_Hackrf

    def set_samp_rate_Baseband_Hackrf(self, samp_rate_Baseband_Hackrf):
        self.samp_rate_Baseband_Hackrf = samp_rate_Baseband_Hackrf
        self.analog_sig_source_x_2.set_sampling_freq(self.samp_rate_Baseband_Hackrf)
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate_Baseband_Hackrf)

    def get_samp_rate_Baseband(self):
        return self.samp_rate_Baseband

    def set_samp_rate_Baseband(self, samp_rate_Baseband):
        self.samp_rate_Baseband = samp_rate_Baseband
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate_Baseband)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate_Baseband)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate_Baseband, 16.3e3, 19e3, 200, firdes.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate_Baseband)

    def get_samp_rate_Audio(self):
        return self.samp_rate_Audio

    def set_samp_rate_Audio(self, samp_rate_Audio):
        self.samp_rate_Audio = samp_rate_Audio
        self.blocks_throttle_0.set_sample_rate(self.samp_rate_Audio)



def main(top_block_cls=SSB_transmitter, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
