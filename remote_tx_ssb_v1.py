#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: SSB Transmitter V1 - F1ATB - MAY 2020
# Author: F1ATB - BUHART
# Description: TX SSB
# GNU Radio version: 3.8.1.0

from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation

class remote_tx_ssb_v1(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "SSB Transmitter V1 - F1ATB - MAY 2020")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2400000
        self.LSB_USB = LSB_USB = 1
        self.GainRF_TX = GainRF_TX = 100
        self.GainIF_TX = GainIF_TX = 300
        self.GainBB_TX = GainBB_TX = 40
        self.Fr_TX = Fr_TX = 145100000

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=240,
                decimation=1,
                taps=None,
                fractional_bw=None)
        self.hilbert_fc_0 = filter.hilbert_fc(64, firdes.WIN_HAMMING, 6.76)
        self.hilbert_fc_0.set_min_output_buffer(10)
        self.hilbert_fc_0.set_max_output_buffer(10)
        self.blocks_udp_source_0 = blocks.udp_source(gr.sizeof_short*1, '127.0.0.1', 9005, 512, True)
        self.blocks_udp_source_0.set_max_output_buffer(2048)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 32767)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(LSB_USB)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.band_pass_filter_0 = filter.fir_filter_ccc(
            1,
            firdes.complex_band_pass(
                1,
                samp_rate/240,
                -1300+LSB_USB*1500,
                1300+LSB_USB*1500,
                200,
                firdes.WIN_HAMMING,
                6.76))



        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_short_to_float_0, 0), (self.hilbert_fc_0, 0))
        self.connect((self.blocks_udp_source_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.hilbert_fc_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_null_sink_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/240, -1300+self.LSB_USB*1500, 1300+self.LSB_USB*1500, 200, firdes.WIN_HAMMING, 6.76))

    def get_LSB_USB(self):
        return self.LSB_USB

    def set_LSB_USB(self, LSB_USB):
        self.LSB_USB = LSB_USB
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.samp_rate/240, -1300+self.LSB_USB*1500, 1300+self.LSB_USB*1500, 200, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_const_vxx_0.set_k(self.LSB_USB)

    def get_GainRF_TX(self):
        return self.GainRF_TX

    def set_GainRF_TX(self, GainRF_TX):
        self.GainRF_TX = GainRF_TX

    def get_GainIF_TX(self):
        return self.GainIF_TX

    def set_GainIF_TX(self, GainIF_TX):
        self.GainIF_TX = GainIF_TX

    def get_GainBB_TX(self):
        return self.GainBB_TX

    def set_GainBB_TX(self, GainBB_TX):
        self.GainBB_TX = GainBB_TX

    def get_Fr_TX(self):
        return self.Fr_TX

    def set_Fr_TX(self, Fr_TX):
        self.Fr_TX = Fr_TX



def main(top_block_cls=remote_tx_ssb_v1, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()
        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
