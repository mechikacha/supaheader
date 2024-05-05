#!/usr/bin/env python3

from argparse import ArgumentParser
import os

header_size = (21, 1, 1, 1, 1, 1, 1, 1, 2, 2)
HEADER_ADDRESS = 0x7fc0


def open_rom(file):
    rom = open(file, "rb")
    rom.seek(HEADER_ADDRESS)
    if file.endswith('.smc'):
        rom.seek(0x200, os.SEEK_CUR)

    rom_name = rom.read(header_size[0]).decode("utf-8")

    print('CARTRIDGE TITLE: ', rom_name)


parser = ArgumentParser()
parser.add_argument('ROM_FILE')
rom_file = parser.parse_args().ROM_FILE

open_rom(rom_file)
