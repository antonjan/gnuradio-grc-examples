#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: QO-100 ssb and CW resever
# Author: Anton Janovsky ZR6AIC
# Description: QO-100 SSB and CW recever
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

class qo_100_ssb_cw_rx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "QO-100 ssb and CW resever")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("QO-100 ssb and CW resever")
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

        self.settings = Qt.QSettings("GNU Radio", "qo_100_ssb_cw_rx")

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
        self.variable_slider_1 = variable_slider_1 = 0.01
        self.variable_slider_0 = variable_slider_0 = 11.5e3
        self.variable_chooser_0 = variable_chooser_0 = 0
        self.samp_rate = samp_rate = 1.2e6

        ##################################################
        # Blocks
        ##################################################
        self._variable_slider_1_range = Range(0, 1, 0.1, 0.01, 200)
        self._variable_slider_1_win = RangeWidget(self._variable_slider_1_range, self.set_variable_slider_1, 'Audio gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_slider_1_win)
        self._variable_slider_0_range = Range(-24e3, 24e3, 1, 11.5e3, 200)
        self._variable_slider_0_win = RangeWidget(self._variable_slider_0_range, self.set_variable_slider_0, 'Frequency', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_slider_0_win)
        # Create the options list
        self._variable_chooser_0_options = (0, 1, 2, 3, )
        # Create the labels list
        self._variable_chooser_0_labels = ('900', '500', '200', 'SSB (2.7khz)', )
        # Create the combo box
        # Create the radio buttons
        self._variable_chooser_0_group_box = Qt.QGroupBox('Filter - CW' + ": ")
        self._variable_chooser_0_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._variable_chooser_0_button_group = variable_chooser_button_group()
        self._variable_chooser_0_group_box.setLayout(self._variable_chooser_0_box)
        for i, _label in enumerate(self._variable_chooser_0_labels):
            radio_button = Qt.QRadioButton(_label)
            self._variable_chooser_0_box.addWidget(radio_button)
            self._variable_chooser_0_button_group.addButton(radio_button, i)
        self._variable_chooser_0_callback = lambda i: Qt.QMetaObject.invokeMethod(self._variable_chooser_0_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._variable_chooser_0_options.index(i)))
        self._variable_chooser_0_callback(self.variable_chooser_0)
        self._variable_chooser_0_button_group.buttonClicked[int].connect(
            lambda i: self.set_variable_chooser_0(self._variable_chooser_0_options[i]))
        self.top_grid_layout.addWidget(self._variable_chooser_0_group_box)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=8,
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
        self.qtgui_sink_x_0 = qtgui.sink_f(
            1024, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            48000, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_win)
        self.osmosdr_source_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + 'rtl=0'
        )
        self.osmosdr_source_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(145.825e6, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_gain(10, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(25, firdes.low_pass(1,48000,500,50), variable_slider_0, 1.2e6)
        self.blocks_selector_0 = blocks.selector(gr.sizeof_float*1,variable_chooser_0,0)
        self.blocks_selector_0.set_enabled(True)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(variable_slider_1)
        self.blocks_complex_to_float_1 = blocks.complex_to_float(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_2_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                48000,
                100,
                2700,
                50,
                firdes.WIN_HAMMING,
                6.76))
        self.band_pass_filter_2 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                48000,
                600,
                800,
                50,
                firdes.WIN_HAMMING,
                6.76))
        self.band_pass_filter_1 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                48000,
                450,
                950,
                100,
                firdes.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                48000,
                300,
                1100,
                100,
                firdes.WIN_HAMMING,
                6.76))
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_sig_source_x_1 = analog.sig_source_f(48000, analog.GR_COS_WAVE, 700, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(48000, analog.GR_SIN_WAVE, 700, 1, 0, 0)
        self.analog_agc2_xx_0 = analog.agc2_ff(1e-3, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_selector_0, 0))
        self.connect((self.band_pass_filter_1, 0), (self.blocks_selector_0, 1))
        self.connect((self.band_pass_filter_2, 0), (self.blocks_selector_0, 2))
        self.connect((self.band_pass_filter_2_0, 0), (self.blocks_selector_0, 3))
        self.connect((self.blocks_add_xx_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.band_pass_filter_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.band_pass_filter_2, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.band_pass_filter_2_0, 0))
        self.connect((self.blocks_complex_to_float_1, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_complex_to_float_1, 1), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_selector_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.blocks_selector_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.blocks_complex_to_float_1, 0))
        self.connect((self.osmosdr_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "qo_100_ssb_cw_rx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_variable_slider_1(self):
        return self.variable_slider_1

    def set_variable_slider_1(self, variable_slider_1):
        self.variable_slider_1 = variable_slider_1
        self.blocks_multiply_const_vxx_0.set_k(self.variable_slider_1)

    def get_variable_slider_0(self):
        return self.variable_slider_0

    def set_variable_slider_0(self, variable_slider_0):
        self.variable_slider_0 = variable_slider_0
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.variable_slider_0)

    def get_variable_chooser_0(self):
        return self.variable_chooser_0

    def set_variable_chooser_0(self, variable_chooser_0):
        self.variable_chooser_0 = variable_chooser_0
        self._variable_chooser_0_callback(self.variable_chooser_0)
        self.blocks_selector_0.set_input_index(self.variable_chooser_0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)



def main(top_block_cls=qo_100_ssb_cw_rx, options=None):

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
