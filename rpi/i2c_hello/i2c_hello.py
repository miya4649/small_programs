#!/usr/bin/python
# -*- coding: utf-8 -*-

#Copyright (c) 2017, miya
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
#
#1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#
#2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
#IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


import smbus
import time


def str2ascii(string):
    out = []
    for char in string:
        out.append(ord(char))
    return out


def i2c_out(i2c_if, addr, reg, data, wait):
    for value in data:
        i2c_if.write_byte_data(addr, reg, value)
        time.sleep(wait)


def i2c_in(i2c_if, addr, reg):
    return i2c_if.read_byte_data(addr, reg)


I2C_IF = 1
ADDR_OLED = 0x3c
REG_COMMAND = 0x00
REG_DATA = 0x40

# OLED COMMAND:
# 0x01: Clear Display
# 0x02: Return Cursor to Home
# 0x0f: Display On
# 0x08: Display Off
# 0x80 + n: Set Cursor Position
#   1st line: 0x00 <= n <= 0x0f
#   2nd line: 0x20 <= n <= 0x2f

i2c = smbus.SMBus(I2C_IF)
while True:
    i2c_out(i2c, ADDR_OLED, REG_COMMAND, [0x01, 0x02, 0x0f], 0)
    i2c_out(i2c, ADDR_OLED, REG_DATA, str2ascii('Raspberry Pi'), 0.1)
    i2c_out(i2c, ADDR_OLED, REG_COMMAND, [0x80 + 0x20], 0)
    i2c_out(i2c, ADDR_OLED, REG_DATA, str2ascii('Zero'), 0.1)
    time.sleep(2)
    i2c_out(i2c, ADDR_OLED, REG_COMMAND, [0x01], 0)
    i2c_out(i2c, ADDR_OLED, REG_DATA, str2ascii('Hello, world!'), 0.1)
    time.sleep(2)
    i2c_out(i2c, ADDR_OLED, REG_COMMAND, [0x01, 0x02, 0x08], 0)
    time.sleep(1)
