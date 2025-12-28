"""Compression functions - zlib, Adler-32, CRC32, etc."""

from tzar.compression.adler32 import adler32, func89
from tzar.compression.crc32 import crc32, func43
from tzar.compression.bitflush import flush_bits, func50
