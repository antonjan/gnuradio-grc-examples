#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: DVB-S B200 Transmitter
# Generated: Sun Jun  4 22:13:26 2017
##################################################

# Hamradio 2017 - DATV FORUM
#
# All-in-ONE
# A DATV SDR Experimental TX/RX solution
# HB9DUG Michel
#


if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import dtv
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from gnuradio import qtgui
# removed 'from optparse import OptionParser' and added 'import argparse'
# from optparse import OptionParser
import argparse
import sip
import sys
import time
import os


class dvbs_tx_var_v4(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "DVB-S B200 Transmitter")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("DVB-S B200 Transmitter")
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

        self.settings = Qt.QSettings("GNU Radio", "dvbs_tx_var_v4")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        #self.symbol_rate = symbol_rate = 1000000
        self.symbol_rate = symbol_rate
        self.variable_qtgui_push_button_0 = variable_qtgui_push_button_0 = 1
        self.tx_gain = tx_gain = 45
        self.symbol_rate_display = symbol_rate_display = symbol_rate/1000
        self.samp_rate = samp_rate = symbol_rate * 2
        self.rrc_taps = rrc_taps = 100
        #self.fec_display = fec_display = "7/8"
        self.fec_display = fec_display
        self.center_freq = center_freq = 1280e6

        ##################################################
        # Blocks
        ##################################################
        self._tx_gain_range = Range(0, 89, 1, 65, 200)
        self._tx_gain_win = RangeWidget(self._tx_gain_range, self.set_tx_gain, 'Tx Gain [dB]', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tx_gain_win, 9,0,1,5)
        self._center_freq_options = (50e6, 437e6, 1280e6, 2400.0e6, )
        self._center_freq_labels = ('50 MHz', '437 MHz', "1'280 MHz", "10'400 MHz", )
        self._center_freq_group_box = Qt.QGroupBox('TX Frequency')
        self._center_freq_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._center_freq_button_group = variable_chooser_button_group()
        self._center_freq_group_box.setLayout(self._center_freq_box)
        for i, label in enumerate(self._center_freq_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._center_freq_box.addWidget(radio_button)
        	self._center_freq_button_group.addButton(radio_button, i)
        self._center_freq_callback = lambda i: Qt.QMetaObject.invokeMethod(self._center_freq_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._center_freq_options.index(i)))
        self._center_freq_callback(self.center_freq)
        self._center_freq_button_group.buttonClicked[int].connect(
        	lambda i: self.set_center_freq(self._center_freq_options[i]))
        self.top_grid_layout.addWidget(self._center_freq_group_box, 0,0, 1,5)
        _variable_qtgui_push_button_0_push_button = Qt.QPushButton('TRANSMIT')
        self._variable_qtgui_push_button_0_choices = {'Pressed': 0, 'Released': 1}
        _variable_qtgui_push_button_0_push_button.pressed.connect(lambda: self.set_variable_qtgui_push_button_0(self._variable_qtgui_push_button_0_choices['Pressed']))
        _variable_qtgui_push_button_0_push_button.released.connect(lambda: self.set_variable_qtgui_push_button_0(self._variable_qtgui_push_button_0_choices['Released']))
        self.top_grid_layout.addWidget(_variable_qtgui_push_button_0_push_button, 10,0,1,5)
        self.uhd_usrp_sink_0_0 = uhd.usrp_sink(
        	",".join(("send_frame_size=65536,num_send_frames=256,master_clock_rate=" + str(samp_rate*2), "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0_0.set_clock_source('external', 0)
        self.uhd_usrp_sink_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0_0.set_center_freq(uhd.tune_request(center_freq, ((symbol_rate * 1.35) / 2 ) + 1e5), 0)
        self.uhd_usrp_sink_0_0.set_gain(tx_gain, 0)
        self.uhd_usrp_sink_0_0.set_antenna('TX/RX', 0)
        self._symbol_rate_display_tool_bar = Qt.QToolBar(self)

        if "{0:,}".format:
          self._symbol_rate_display_formatter = "{0:,}".format
        else:
          self._symbol_rate_display_formatter = lambda x: x

        self._symbol_rate_display_tool_bar.addWidget(Qt.QLabel('              Symbol Rate [ks/s] '+": "))
        self._symbol_rate_display_label = Qt.QLabel(str(self._symbol_rate_display_formatter(self.symbol_rate_display)))
        self._symbol_rate_display_tool_bar.addWidget(self._symbol_rate_display_label)
        self.top_grid_layout.addWidget(self._symbol_rate_display_tool_bar, 1,1,1,1)

        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	center_freq, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, -20)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.1)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not False:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 3,0,6,5)
        self.fft_filter_xxx_0 = filter.fft_filter_ccc(1, (firdes.root_raised_cosine(1.0, samp_rate, samp_rate/2, 0.35, rrc_taps)), 1)
        self.fft_filter_xxx_0.declare_sample_delay(0)
        self._fec_display_tool_bar = Qt.QToolBar(self)

        if "":
          self._fec_display_formatter = ""
        else:
          self._fec_display_formatter = lambda x: x

        self._fec_display_tool_bar.addWidget(Qt.QLabel('FEC '+": "))
        self._fec_display_label = Qt.QLabel(str(self._fec_display_formatter(self.fec_display)))
        self._fec_display_tool_bar.addWidget(self._fec_display_label)
        self.top_grid_layout.addWidget(self._fec_display_tool_bar, 1,3,1,2)

        self.dtv_dvbt_reed_solomon_enc_0 = dtv.dvbt_reed_solomon_enc(2, 8, 0x11d, 255, 239, 8, 51, 8)
        self.dtv_dvbt_inner_coder_0 = dtv.dvbt_inner_coder(1, 1512, dtv.MOD_QPSK, dtv.NH, dtv.C5_6)
        self.dtv_dvbt_energy_dispersal_0 = dtv.dvbt_energy_dispersal(1)
        self.dtv_dvbt_convolutional_interleaver_0 = dtv.dvbt_convolutional_interleaver(136, 12, 17)
        self.dtv_dvbs2_modulator_bc_0 = dtv.dvbs2_modulator_bc(dtv.FECFRAME_NORMAL,
        dtv.C5_6, dtv.MOD_QPSK, dtv.INTERPOLATION_ON)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_char*1, 1512)
	fifo_path = os.path.dirname(os.path.realpath(__file__)) + '/fifo.ts'
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_char*1, fifo_path, True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0_0, 0), (self.dtv_dvbt_energy_dispersal_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.dtv_dvbs2_modulator_bc_0, 0))
        self.connect((self.dtv_dvbs2_modulator_bc_0, 0), (self.fft_filter_xxx_0, 0))
        self.connect((self.dtv_dvbt_convolutional_interleaver_0, 0), (self.dtv_dvbt_inner_coder_0, 0))
        self.connect((self.dtv_dvbt_energy_dispersal_0, 0), (self.dtv_dvbt_reed_solomon_enc_0, 0))
        self.connect((self.dtv_dvbt_inner_coder_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.dtv_dvbt_reed_solomon_enc_0, 0), (self.dtv_dvbt_convolutional_interleaver_0, 0))
        self.connect((self.fft_filter_xxx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.fft_filter_xxx_0, 0), (self.uhd_usrp_sink_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "dvbs_tx_var_v4")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate
        self.set_samp_rate(self.symbol_rate * 2)
        self.uhd_usrp_sink_0_0.set_center_freq(uhd.tune_request(self.center_freq, ((self.symbol_rate * 1.35) / 2 ) + 1e5), 0)
        self.set_symbol_rate_display(self._symbol_rate_display_formatter(self.symbol_rate/1000))

    def get_variable_qtgui_push_button_0(self):
        return self.variable_qtgui_push_button_0

    def set_variable_qtgui_push_button_0(self, variable_qtgui_push_button_0):
        self.variable_qtgui_push_button_0 = variable_qtgui_push_button_0

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.uhd_usrp_sink_0_0.set_gain(self.tx_gain, 0)


    def get_symbol_rate_display(self):
        return self.symbol_rate_display

    def set_symbol_rate_display(self, symbol_rate_display):
        self.symbol_rate_display = symbol_rate_display
        Qt.QMetaObject.invokeMethod(self._symbol_rate_display_label, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.symbol_rate_display)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)
        self.fft_filter_xxx_0.set_taps((firdes.root_raised_cosine(1.0, self.samp_rate, self.samp_rate/2, 0.35, self.rrc_taps)))

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.fft_filter_xxx_0.set_taps((firdes.root_raised_cosine(1.0, self.samp_rate, self.samp_rate/2, 0.35, self.rrc_taps)))

    def get_fec_display(self):
        return self.fec_display

    def set_fec_display(self, fec_display):
        self.fec_display = fec_display
        Qt.QMetaObject.invokeMethod(self._fec_display_label, "setText", Qt.Q_ARG("QString", str(self.fec_display)))

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self._center_freq_callback(self.center_freq)
        self.uhd_usrp_sink_0_0.set_center_freq(uhd.tune_request(self.center_freq, ((self.symbol_rate * 1.35) / 2 ) + 1e5), 0)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)


def main(top_block_cls=dvbs_tx_var_v4, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

    global symbol_rate
    global code_rate
    global fec_display
    global dvb

    parser = argparse.ArgumentParser()
    
    srate_help = 'symbol rate (ks/s): 125, 250, 500, 1000, 2000 (default).'
    parser.add_argument('-sr', '--symbole-rate', dest='srate', default='1000',
                        type=str, help=srate_help)

    rate_help = 'Viterbi rate. 1/2, 2/3, 3/4, 5/6, 7/8 (default).'
    parser.add_argument('-vr', '--viterbi-rate', dest='rate', default='7/8',
                        type=str, help=rate_help)


    args = parser.parse_args()
    
    if args.srate == '125':
        symbol_rate = 125000.0
    elif args.srate == '250':
        symbol_rate = 250000.0
    elif args.srate == '500':
        symbol_rate = 500000.0
    elif args.srate == '1000':
        symbol_rate = 1000000.0
    elif args.srate == '2000':
        symbol_rate = 2000000.0
    else:
        sys.stderr.write('*******************************************' + '\n')
        sys.stderr.write('Invalid symbol rate: ' + (args.srate) + '\n')
        sys.stderr.write('*******************************************' + '\n')
        sys.exit(1)	
    
    if args.rate == '1/2':
        code_rate = dtv.C1_2
    elif args.rate == '2/3':
        code_rate = dtv.C2_3
    elif args.rate == '3/4':
        code_rate = dtv.C3_4
    elif args.rate == '5/6':
        code_rate = dtv.C5_6
    elif args.rate == '7/8':
        code_rate = dtv.C7_8
    else:
        sys.stderr.write('*******************************************' + '\n')
        sys.stderr.write('Invalid Viterbi rate: ' + args.rate + '\n')
        sys.stderr.write('*******************************************' + '\n')
        sys.exit(1)

    fec_display = args.rate



    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
