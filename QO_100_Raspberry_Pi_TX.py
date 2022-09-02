#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: QO-100-Raspberry-Pi
# Author: Anton Janovsky (ZR6AIC)
# Description: This is a working QO-100 Transmitter
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

class QO_100_Raspberry_Pi_TX(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "QO-100-Raspberry-Pi")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("QO-100-Raspberry-Pi")
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

        self.settings = Qt.QSettings("GNU Radio", "QO_100_Raspberry_Pi_TX")

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
        self.variable_slider_0 = variable_slider_0 = 2.40029e9
        self.variable_slider_Audio_level_0 = variable_slider_Audio_level_0 = 0.6
        self.variable_slider_Audio_level = variable_slider_Audio_level = 1
        self.samp_rate = samp_rate = 1e6
        self.rx_tx_sel = rx_tx_sel = 0
        self.rf_gain = rf_gain = 100
        self.modelation_amp = modelation_amp = 1
        self.mixer_level = mixer_level = 1
        self.if_gain = if_gain = 100
        self.bb_gain = bb_gain = 59
        self.base_freq = base_freq = 739.200e6
        self.Tx_freq_0 = Tx_freq_0 = variable_slider_0
        self.Audio_sel_1 = Audio_sel_1 = 0
        self.Audio_freq = Audio_freq = 1000

        ##################################################
        # Blocks
        ##################################################
        self._variable_slider_Audio_level_0_range = Range(0, 2, 0.05, 0.6, 200)
        self._variable_slider_Audio_level_0_win = RangeWidget(self._variable_slider_Audio_level_0_range, self.set_variable_slider_Audio_level_0, 'Modelation audio input', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_slider_Audio_level_0_win)
        self._variable_slider_Audio_level_range = Range(0, 2, 0.1, 1, 200)
        self._variable_slider_Audio_level_win = RangeWidget(self._variable_slider_Audio_level_range, self.set_variable_slider_Audio_level, '1Khz Audio Level', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_slider_Audio_level_win)
        self._rf_gain_range = Range(1, 100, .1, 100, 200)
        self._rf_gain_win = RangeWidget(self._rf_gain_range, self.set_rf_gain, 'rf_gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rf_gain_win)
        self._mixer_level_range = Range(0.1, 5, 0.1, 1, 200)
        self._mixer_level_win = RangeWidget(self._mixer_level_range, self.set_mixer_level, 'Cosinde Mixer Level', "counter_slider", float)
        self.top_grid_layout.addWidget(self._mixer_level_win)
        self._if_gain_range = Range(1, 100, 0.1, 100, 200)
        self._if_gain_win = RangeWidget(self._if_gain_range, self.set_if_gain, 'if Gain hackrf', "counter_slider", float)
        self.top_grid_layout.addWidget(self._if_gain_win)
        self._Audio_freq_range = Range(10, 5000, 1, 1000, 200)
        self._Audio_freq_win = RangeWidget(self._Audio_freq_range, self.set_Audio_freq, 'Audio Oselator Freq', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Audio_freq_win)
        self._variable_slider_0_range = Range(2.4e9, 2.40060e9, 100, 2.40029e9, 200)
        self._variable_slider_0_win = RangeWidget(self._variable_slider_0_range, self.set_variable_slider_0, 'TX Frequency', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_slider_0_win)
        # Create the options list
        self._rx_tx_sel_options = (0, 1, )
        # Create the labels list
        self._rx_tx_sel_labels = ('TX', 'RX', )
        # Create the combo box
        # Create the radio buttons
        self._rx_tx_sel_group_box = Qt.QGroupBox('PTT' + ": ")
        self._rx_tx_sel_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._rx_tx_sel_button_group = variable_chooser_button_group()
        self._rx_tx_sel_group_box.setLayout(self._rx_tx_sel_box)
        for i, _label in enumerate(self._rx_tx_sel_labels):
            radio_button = Qt.QRadioButton(_label)
            self._rx_tx_sel_box.addWidget(radio_button)
            self._rx_tx_sel_button_group.addButton(radio_button, i)
        self._rx_tx_sel_callback = lambda i: Qt.QMetaObject.invokeMethod(self._rx_tx_sel_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._rx_tx_sel_options.index(i)))
        self._rx_tx_sel_callback(self.rx_tx_sel)
        self._rx_tx_sel_button_group.buttonClicked[int].connect(
            lambda i: self.set_rx_tx_sel(self._rx_tx_sel_options[i]))
        self.top_grid_layout.addWidget(self._rx_tx_sel_group_box)
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=1000000,
                decimation=192000,
                taps=None,
                fractional_bw=None)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=24,
                decimation=6,
                taps=None,
                fractional_bw=None)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1
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

        for i in range(1):
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
            args="numchan=" + str(1) + " " + 'hackrf'
        )
        self.osmosdr_sink_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_sink_0.set_sample_rate(1000000)
        self.osmosdr_sink_0.set_center_freq(435.1e6, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(rf_gain, 0)
        self.osmosdr_sink_0.set_if_gain(if_gain, 0)
        self.osmosdr_sink_0.set_bb_gain(40, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
        self._modelation_amp_range = Range(0, 10, 0.1, 1, 200)
        self._modelation_amp_win = RangeWidget(self._modelation_amp_range, self.set_modelation_amp, 'RF output to hackrf', "counter_slider", float)
        self.top_grid_layout.addWidget(self._modelation_amp_win)
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                192000,
                4500,
                1004,
                firdes.WIN_HAMMING,
                6.76))
        self.hilbert_fc_0 = filter.hilbert_fc(128, firdes.WIN_HAMMING, 6.76)
        self.hilbert_fc_0.set_min_output_buffer(10)
        self.hilbert_fc_0.set_max_output_buffer(10)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_cc(variable_slider_Audio_level_0)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(variable_slider_Audio_level_0)
        self._bb_gain_range = Range(1, 59, 0.1, 59, 200)
        self._bb_gain_win = RangeWidget(self._bb_gain_range, self.set_bb_gain, 'bb Gain Hackrf', "counter_slider", float)
        self.top_grid_layout.addWidget(self._bb_gain_win)
        self.analog_sig_source_x_1 = analog.sig_source_f(48000, analog.GR_SIN_WAVE, Audio_freq, variable_slider_Audio_level, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(192e3, analog.GR_COS_WAVE, 50e3, mixer_level, 0, 0)
        # Create the options list
        self._Audio_sel_1_options = (0, 1, 2, )
        # Create the labels list
        self._Audio_sel_1_labels = ('Echolink', '1Khz', 'Play Audio File', )
        # Create the combo box
        # Create the radio buttons
        self._Audio_sel_1_group_box = Qt.QGroupBox('Audio input' + ": ")
        self._Audio_sel_1_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._Audio_sel_1_button_group = variable_chooser_button_group()
        self._Audio_sel_1_group_box.setLayout(self._Audio_sel_1_box)
        for i, _label in enumerate(self._Audio_sel_1_labels):
            radio_button = Qt.QRadioButton(_label)
            self._Audio_sel_1_box.addWidget(radio_button)
            self._Audio_sel_1_button_group.addButton(radio_button, i)
        self._Audio_sel_1_callback = lambda i: Qt.QMetaObject.invokeMethod(self._Audio_sel_1_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._Audio_sel_1_options.index(i)))
        self._Audio_sel_1_callback(self.Audio_sel_1)
        self._Audio_sel_1_button_group.buttonClicked[int].connect(
            lambda i: self.set_Audio_sel_1(self._Audio_sel_1_options[i]))
        self.top_grid_layout.addWidget(self._Audio_sel_1_group_box)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.hilbert_fc_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.rational_resampler_xxx_0, 0), (self.hilbert_fc_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_multiply_const_vxx_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "QO_100_Raspberry_Pi_TX")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_variable_slider_0(self):
        return self.variable_slider_0

    def set_variable_slider_0(self, variable_slider_0):
        self.variable_slider_0 = variable_slider_0
        self.set_Tx_freq_0(self.variable_slider_0)

    def get_variable_slider_Audio_level_0(self):
        return self.variable_slider_Audio_level_0

    def set_variable_slider_Audio_level_0(self, variable_slider_Audio_level_0):
        self.variable_slider_Audio_level_0 = variable_slider_Audio_level_0
        self.blocks_multiply_const_vxx_0.set_k(self.variable_slider_Audio_level_0)
        self.blocks_multiply_const_vxx_0_0.set_k(self.variable_slider_Audio_level_0)

    def get_variable_slider_Audio_level(self):
        return self.variable_slider_Audio_level

    def set_variable_slider_Audio_level(self, variable_slider_Audio_level):
        self.variable_slider_Audio_level = variable_slider_Audio_level
        self.analog_sig_source_x_1.set_amplitude(self.variable_slider_Audio_level)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_rx_tx_sel(self):
        return self.rx_tx_sel

    def set_rx_tx_sel(self, rx_tx_sel):
        self.rx_tx_sel = rx_tx_sel
        self._rx_tx_sel_callback(self.rx_tx_sel)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self.osmosdr_sink_0.set_gain(self.rf_gain, 0)

    def get_modelation_amp(self):
        return self.modelation_amp

    def set_modelation_amp(self, modelation_amp):
        self.modelation_amp = modelation_amp

    def get_mixer_level(self):
        return self.mixer_level

    def set_mixer_level(self, mixer_level):
        self.mixer_level = mixer_level
        self.analog_sig_source_x_0.set_amplitude(self.mixer_level)

    def get_if_gain(self):
        return self.if_gain

    def set_if_gain(self, if_gain):
        self.if_gain = if_gain
        self.osmosdr_sink_0.set_if_gain(self.if_gain, 0)

    def get_bb_gain(self):
        return self.bb_gain

    def set_bb_gain(self, bb_gain):
        self.bb_gain = bb_gain

    def get_base_freq(self):
        return self.base_freq

    def set_base_freq(self, base_freq):
        self.base_freq = base_freq

    def get_Tx_freq_0(self):
        return self.Tx_freq_0

    def set_Tx_freq_0(self, Tx_freq_0):
        self.Tx_freq_0 = Tx_freq_0

    def get_Audio_sel_1(self):
        return self.Audio_sel_1

    def set_Audio_sel_1(self, Audio_sel_1):
        self.Audio_sel_1 = Audio_sel_1
        self._Audio_sel_1_callback(self.Audio_sel_1)

    def get_Audio_freq(self):
        return self.Audio_freq

    def set_Audio_freq(self, Audio_freq):
        self.Audio_freq = Audio_freq
        self.analog_sig_source_x_1.set_frequency(self.Audio_freq)



def main(top_block_cls=QO_100_Raspberry_Pi_TX, options=None):

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
