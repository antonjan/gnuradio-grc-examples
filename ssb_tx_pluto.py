#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: ssbtx
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
import iio
from gnuradio import qtgui

class ssb_tx_pluto(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "ssbtx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("ssbtx")
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

        self.settings = Qt.QSettings("GNU Radio", "ssb_tx_pluto")

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
        self.variable_qtgui_range_0_0_0_1_0_0 = variable_qtgui_range_0_0_0_1_0_0 = 60
        self.variable_qtgui_range_0_0_0_1_0 = variable_qtgui_range_0_0_0_1_0 = 60
        self.variable_qtgui_range_0_0_0_1 = variable_qtgui_range_0_0_0_1 = 1
        self.variable_qtgui_range_0_0_0_0 = variable_qtgui_range_0_0_0_0 = 2400000
        self.variable_qtgui_range_0_0_0 = variable_qtgui_range_0_0_0 = 1
        self.variable_qtgui_range_0_0 = variable_qtgui_range_0_0 = 1
        self.variable_qtgui_range_0 = variable_qtgui_range_0 = 1
        self.samp_rate = samp_rate = 4e6

        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_range_0_0_0_range = Range(0, 4, 0.1, 1, 200)
        self._variable_qtgui_range_0_0_0_win = RangeWidget(self._variable_qtgui_range_0_0_0_range, self.set_variable_qtgui_range_0_0_0, 'RF Output Level', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_0_0_0_win)
        self._variable_qtgui_range_0_0_range = Range(0, 4, 0.1, 1, 200)
        self._variable_qtgui_range_0_0_win = RangeWidget(self._variable_qtgui_range_0_0_range, self.set_variable_qtgui_range_0_0, 'Mixer Aplitude', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_0_0_win)
        self._variable_qtgui_range_0_range = Range(0, 4, 0.1, 1, 200)
        self._variable_qtgui_range_0_win = RangeWidget(self._variable_qtgui_range_0_range, self.set_variable_qtgui_range_0, 'Modulator amp', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_0_win)
        self._variable_qtgui_range_0_0_0_1_0_0_range = Range(0, 80, 0.1, 60, 200)
        self._variable_qtgui_range_0_0_0_1_0_0_win = RangeWidget(self._variable_qtgui_range_0_0_0_1_0_0_range, self.set_variable_qtgui_range_0_0_0_1_0_0, 'IF Output Level hackrf', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_0_0_0_1_0_0_win)
        self._variable_qtgui_range_0_0_0_1_0_range = Range(0, 80, 0.1, 60, 200)
        self._variable_qtgui_range_0_0_0_1_0_win = RangeWidget(self._variable_qtgui_range_0_0_0_1_0_range, self.set_variable_qtgui_range_0_0_0_1_0, 'RF Output Level hackrf', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_0_0_0_1_0_win)
        self._variable_qtgui_range_0_0_0_1_range = Range(0, 4, 0.1, 1, 200)
        self._variable_qtgui_range_0_0_0_1_win = RangeWidget(self._variable_qtgui_range_0_0_0_1_range, self.set_variable_qtgui_range_0_0_0_1, 'RF Output Level', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_0_0_0_1_win)
        self._variable_qtgui_range_0_0_0_0_range = Range(2400000, 2410000, 1, 2400000, 200)
        self._variable_qtgui_range_0_0_0_0_win = RangeWidget(self._variable_qtgui_range_0_0_0_0_range, self.set_variable_qtgui_range_0_0_0_0, 'TX Frequency', "counter_slider", int)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_0_0_0_0_win)
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=4000000,
                decimation=192000,
                taps=None,
                fractional_bw=None)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=24,
                decimation=6,
                taps=None,
                fractional_bw=None)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.iio_pluto_sink_0 = iio.pluto_sink('ip:pluto.local', 2400000000, 2084000, 20000000, 32768, False, 10.0, '', True)
        self.hilbert_fc_0 = filter.hilbert_fc(256, firdes.WIN_HAMMING, 6.76)
        self.hilbert_fc_0.set_min_output_buffer(10)
        self.hilbert_fc_0.set_max_output_buffer(10)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/anton/gnuradio-grc-examples/test_audio.wav', True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, 48e3,True)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_cc(variable_qtgui_range_0_0_0)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(variable_qtgui_range_0)
        self.band_pass_filter_0_0 = filter.fir_filter_ccc(
            1,
            firdes.complex_band_pass(
                1,
                48000,
                200,
                2500,
                100,
                firdes.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                48000,
                200,
                2500,
                100,
                firdes.WIN_HAMMING,
                6.76))
        self.analog_sig_source_x_0 = analog.sig_source_c(192000, analog.GR_COS_WAVE, 1, variable_qtgui_range_0_0, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.band_pass_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.iio_pluto_sink_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.hilbert_fc_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.hilbert_fc_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.qtgui_time_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ssb_tx_pluto")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_variable_qtgui_range_0_0_0_1_0_0(self):
        return self.variable_qtgui_range_0_0_0_1_0_0

    def set_variable_qtgui_range_0_0_0_1_0_0(self, variable_qtgui_range_0_0_0_1_0_0):
        self.variable_qtgui_range_0_0_0_1_0_0 = variable_qtgui_range_0_0_0_1_0_0

    def get_variable_qtgui_range_0_0_0_1_0(self):
        return self.variable_qtgui_range_0_0_0_1_0

    def set_variable_qtgui_range_0_0_0_1_0(self, variable_qtgui_range_0_0_0_1_0):
        self.variable_qtgui_range_0_0_0_1_0 = variable_qtgui_range_0_0_0_1_0

    def get_variable_qtgui_range_0_0_0_1(self):
        return self.variable_qtgui_range_0_0_0_1

    def set_variable_qtgui_range_0_0_0_1(self, variable_qtgui_range_0_0_0_1):
        self.variable_qtgui_range_0_0_0_1 = variable_qtgui_range_0_0_0_1

    def get_variable_qtgui_range_0_0_0_0(self):
        return self.variable_qtgui_range_0_0_0_0

    def set_variable_qtgui_range_0_0_0_0(self, variable_qtgui_range_0_0_0_0):
        self.variable_qtgui_range_0_0_0_0 = variable_qtgui_range_0_0_0_0

    def get_variable_qtgui_range_0_0_0(self):
        return self.variable_qtgui_range_0_0_0

    def set_variable_qtgui_range_0_0_0(self, variable_qtgui_range_0_0_0):
        self.variable_qtgui_range_0_0_0 = variable_qtgui_range_0_0_0
        self.blocks_multiply_const_vxx_0_0.set_k(self.variable_qtgui_range_0_0_0)

    def get_variable_qtgui_range_0_0(self):
        return self.variable_qtgui_range_0_0

    def set_variable_qtgui_range_0_0(self, variable_qtgui_range_0_0):
        self.variable_qtgui_range_0_0 = variable_qtgui_range_0_0
        self.analog_sig_source_x_0.set_amplitude(self.variable_qtgui_range_0_0)

    def get_variable_qtgui_range_0(self):
        return self.variable_qtgui_range_0

    def set_variable_qtgui_range_0(self, variable_qtgui_range_0):
        self.variable_qtgui_range_0 = variable_qtgui_range_0
        self.blocks_multiply_const_vxx_0.set_k(self.variable_qtgui_range_0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)



def main(top_block_cls=ssb_tx_pluto, options=None):

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
