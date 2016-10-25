# coding: utf-8
# Copyright (c) 2016 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


import codecs
from pycoin.tx import Tx
from pycoin.serialize import b2h
from pycoin.serialize import h2b
from pycoin.serialize import b2h_rev
from pycoin.encoding import hash160
from pycoin.tx.pay_to import address_for_pay_to_script


def gettxid(rawtx):
    return b2h_rev(Tx.from_hex(rawtx).hash())


def script_address(script_hex, netcode="BTC"):
    return address_for_pay_to_script(h2b(script_hex), netcode=netcode)


def hash160hex(hexdata):
    return b2h(hash160(h2b(hexdata)))


def to_satoshis(btc_quantity):
    return int(btc_quantity * 100000000)


def bytestoint(data):
    return int(codecs.encode(data, 'hex_codec'), 16)
