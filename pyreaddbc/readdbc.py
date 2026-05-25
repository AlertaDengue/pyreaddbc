"""
Created on 16/08/16
by fccoelho
license: GPL V3 or Later
"""
import os

from pyreaddbc._readdbcmodule import dbc2dbf as _dbc2dbf


def dbc2dbf(infile, outfile):
    """
    Converts a DBC file to a DBF database saving it to `outfile`.
    :param infile: .dbc file name
    :param outfile: name of the .dbf file to be created.
    """
    if isinstance(infile, bytes):
        infile = infile.decode()
    if isinstance(outfile, bytes):
        outfile = outfile.decode()
    infile = os.path.abspath(infile)
    outfile = os.path.abspath(outfile)
    _dbc2dbf(infile, outfile)
