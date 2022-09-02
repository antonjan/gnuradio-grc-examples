#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Signal_gen_70cm
# Author: Anton Janovsky (ZR6AIC)
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
from gnuradio import audio
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

class Signal_gen_70cm(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Signal_gen_70cm ")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Signal_gen_70cm ")
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

        self.settings = Qt.QSettings("GNU Radio", "Signal_gen_70cm")

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
        self.variable_qtgui_range_1 = variable_qtgui_range_1 = 5000
        self.variable_qtgui_range_0_0_0_0_0 = variable_qtgui_range_0_0_0_0_0 = 20
        self.variable_qtgui_range_0_0_0_0 = variable_qtgui_range_0_0_0_0 = 50
        self.variable_qtgui_range_0_0_0 = variable_qtgui_range_0_0_0 = 10
        self.variable_qtgui_range_0_0 = variable_qtgui_range_0_0 = 0.5
        self.variable_qtgui_range_0 = variable_qtgui_range_0 = 435080200
        self.variable_qtgui_chooser_0 = variable_qtgui_chooser_0 = 0
        self.samp_rate_audio = samp_rate_audio = 48000
        self.samp_rate = samp_rate = 96000

        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_range_1_range = Range(1000, 25000, 10, 5000, 200)
        self._variable_qtgui_range_1_win = RangeWidget(self._variable_qtgui_range_1_range, self.set_variable_qtgui_range_1, 'Deviastion', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_1_win)
        self._variable_qtgui_range_0_0_0_0_0_range = Range(1, 50, 1, 20, 200)
        self._variable_qtgui_range_0_0_0_0_0_win = RangeWidget(self._variable_qtgui_range_0_0_0_0_0_range, self.set_variable_qtgui_range_0_0_0_0_0, 'Aplitude rf  BB', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_0_0_0_0_0_win)
        self._variable_qtgui_range_0_0_0_0_range = Range(1, 60, 1, 50, 200)
        self._variable_qtgui_range_0_0_0_0_win = RangeWidget(self._variable_qtgui_range_0_0_0_0_range, self.set_variable_qtgui_range_0_0_0_0, 'Aplitude rf  IF', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_0_0_0_0_win)
        self._variable_qtgui_range_0_0_0_range = Range(1, 60, 1, 10, 200)
        self._variable_qtgui_range_0_0_0_win = RangeWidget(self._variable_qtgui_range_0_0_0_range, self.set_variable_qtgui_range_0_0_0, 'Aplitude rf', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_0_0_0_win)
        self._variable_qtgui_range_0_0_range = Range(0.1, 2, 0.1, 0.5, 200)
        self._variable_qtgui_range_0_0_win = RangeWidget(self._variable_qtgui_range_0_0_range, self.set_variable_qtgui_range_0_0, 'Aplitude audio', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_0_0_win)
        self._variable_qtgui_range_0_range = Range(430000000, 440000000, 100, 435080200, 200)
        self._variable_qtgui_range_0_win = RangeWidget(self._variable_qtgui_range_0_range, self.set_variable_qtgui_range_0, 'Freq', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_0_win)
        # Create the options list
        self._variable_qtgui_chooser_0_options = (0, 1, 2, 3, 4, )
        # Create the labels list
        self._variable_qtgui_chooser_0_labels = ('1 Khz', 'Speaker Audio', 'Play AFSK message Mode 0', 'Play AFSK Message Mod 1', 'Play AFSK Message Mode 2', )
        # Create the combo box
        self._variable_qtgui_chooser_0_tool_bar = Qt.QToolBar(self)
        self._variable_qtgui_chooser_0_tool_bar.addWidget(Qt.QLabel('Select_audio_input' + ": "))
        self._variable_qtgui_chooser_0_combo_box = Qt.QComboBox()
        self._variable_qtgui_chooser_0_tool_bar.addWidget(self._variable_qtgui_chooser_0_combo_box)
        for _label in self._variable_qtgui_chooser_0_labels: self._variable_qtgui_chooser_0_combo_box.addItem(_label)
        self._variable_qtgui_chooser_0_callback = lambda i: Qt.QMetaObject.invokeMethod(self._variable_qtgui_chooser_0_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._variable_qtgui_chooser_0_options.index(i)))
        self._variable_qtgui_chooser_0_callback(self.variable_qtgui_chooser_0)
        self._variable_qtgui_chooser_0_combo_box.currentIndexChanged.connect(
            lambda i: self.set_variable_qtgui_chooser_0(self._variable_qtgui_chooser_0_options[i]))
        # Create the radio buttons
        self.top_grid_layout.addWidget(self._variable_qtgui_chooser_0_tool_bar)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=50,
                decimation=2,
                taps=[1],
                fractional_bw=None)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            2
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + "hackrf=0"
        )
        self.osmosdr_sink_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_sink_0.set_sample_rate(2400000)
        self.osmosdr_sink_0.set_center_freq(variable_qtgui_range_0, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(variable_qtgui_range_0_0_0, 0)
        self.osmosdr_sink_0.set_if_gain(variable_qtgui_range_0_0_0_0, 0)
        self.osmosdr_sink_0.set_bb_gain(variable_qtgui_range_0_0_0_0_0, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                5000,
                2000,
                firdes.WIN_HAMMING,
                6.76))
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/anton/africube_controle/aprs_test.wav', True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, 48000,True)
        self.blocks_selector_0 = blocks.selector(gr.sizeof_float*1,variable_qtgui_chooser_0,0)
        self.blocks_selector_0.set_enabled(True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(variable_qtgui_range_0_0)
        self.audio_source_0 = audio.source(samp_rate_audio, '', True)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate_audio, analog.GR_COS_WAVE, 1000, 1, 0, 0)
        self.analog_nbfm_tx_0 = analog.nbfm_tx(
        	audio_rate=samp_rate_audio,
        	quad_rate=samp_rate,
        	tau=75e-6,
        	max_dev=variable_qtgui_range_1,
        	fh=-1,
                )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_tx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.analog_nbfm_tx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_selector_0, 0))
        self.connect((self.audio_source_0, 0), (self.blocks_selector_0, 1))
        self.connect((self.audio_source_0, 0), (self.blocks_selector_0, 4))
        self.connect((self.audio_source_0, 0), (self.blocks_selector_0, 3))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.analog_nbfm_tx_0, 0))
        self.connect((self.blocks_selector_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_selector_0, 2))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.osmosdr_sink_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Signal_gen_70cm")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_variable_qtgui_range_1(self):
        return self.variable_qtgui_range_1

    def set_variable_qtgui_range_1(self, variable_qtgui_range_1):
        self.variable_qtgui_range_1 = variable_qtgui_range_1
        self.analog_nbfm_tx_0.set_max_deviation(self.variable_qtgui_range_1)

    def get_variable_qtgui_range_0_0_0_0_0(self):
        return self.variable_qtgui_range_0_0_0_0_0

    def set_variable_qtgui_range_0_0_0_0_0(self, variable_qtgui_range_0_0_0_0_0):
        self.variable_qtgui_range_0_0_0_0_0 = variable_qtgui_range_0_0_0_0_0
        self.osmosdr_sink_0.set_bb_gain(self.variable_qtgui_range_0_0_0_0_0, 0)

    def get_variable_qtgui_range_0_0_0_0(self):
        return self.variable_qtgui_range_0_0_0_0

    def set_variable_qtgui_range_0_0_0_0(self, variable_qtgui_range_0_0_0_0):
        self.variable_qtgui_range_0_0_0_0 = variable_qtgui_range_0_0_0_0
        self.osmosdr_sink_0.set_if_gain(self.variable_qtgui_range_0_0_0_0, 0)

    def get_variable_qtgui_range_0_0_0(self):
        return self.variable_qtgui_range_0_0_0

    def set_variable_qtgui_range_0_0_0(self, variable_qtgui_range_0_0_0):
        self.variable_qtgui_range_0_0_0 = variable_qtgui_range_0_0_0
        self.osmosdr_sink_0.set_gain(self.variable_qtgui_range_0_0_0, 0)

    def get_variable_qtgui_range_0_0(self):
        return self.variable_qtgui_range_0_0

    def set_variable_qtgui_range_0_0(self, variable_qtgui_range_0_0):
        self.variable_qtgui_range_0_0 = variable_qtgui_range_0_0
        self.blocks_multiply_const_vxx_0.set_k(self.variable_qtgui_range_0_0)

    def get_variable_qtgui_range_0(self):
        return self.variable_qtgui_range_0

    def set_variable_qtgui_range_0(self, variable_qtgui_range_0):
        self.variable_qtgui_range_0 = variable_qtgui_range_0
        self.osmosdr_sink_0.set_center_freq(self.variable_qtgui_range_0, 0)

    def get_variable_qtgui_chooser_0(self):
        return self.variable_qtgui_chooser_0

    def set_variable_qtgui_chooser_0(self, variable_qtgui_chooser_0):
        self.variable_qtgui_chooser_0 = variable_qtgui_chooser_0
        self._variable_qtgui_chooser_0_callback(self.variable_qtgui_chooser_0)
        self.blocks_selector_0.set_input_index(self.variable_qtgui_chooser_0)

    def get_samp_rate_audio(self):
        return self.samp_rate_audio

    def set_samp_rate_audio(self, samp_rate_audio):
        self.samp_rate_audio = samp_rate_audio
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate_audio)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 5000, 2000, firdes.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)



def main(top_block_cls=Signal_gen_70cm, options=None):

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
