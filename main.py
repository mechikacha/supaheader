#!/usr/bin/env python3

from argparse import ArgumentParser
import os
import hashlib


HEADER_ADDRESS = 0x7fc0
header_size: tuple[int] = (21, 1, 1, 1, 1, 1, 1, 1, 2, 2)
header_contents: list[int] = []
content_labels: list[str] = [
    'CARTRIDGE NAME',
    'MAP MODE',
    'CHIPSET',
    'ROM SIZE',
    'RAM SIZE',
    'REGION',
    'DEVELOPER ID',
    'VERSION',
    'CHECKSUM 1',
    'CHECKSUM 2',
   ]


def main(file_path):
    rom = open(file_path, "rb")
    rdat = rom.read()
    rom.seek(HEADER_ADDRESS)
    if file_path.endswith('.smc'):
        rom.seek(0x200, os.SEEK_CUR)

    for size in header_size:
        rom_info = rom.read(size)
        header_contents.append(rom_info)

    for index, (content, label)\
            in enumerate(zip(header_contents, content_labels)):
        if index == 0:
            print(label+':', str(content, 'utf-8'))
        else:
            print(label+':', content.hex())

    hash_md5 = hashlib.md5(rdat).hexdigest()
    print('MD5:', hash_md5)


parser = ArgumentParser()
parser.add_argument('ROM_FILE')
rom_file = parser.parse_args().ROM_FILE

main(rom_file)
