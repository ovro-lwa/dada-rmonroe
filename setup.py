#!/usr/bin/env python

"""
setup.py file for CUWARPs uvfits data.
"""

from distutils.core import setup, Extension

setup (name = 'dada',
       version = '0.1',
       author      = "Stephen Bourke",
       description = """Python interface to DADA routines""",
       ext_modules = [Extension('_cDada',
                                sources=['Dada.i', 'DadaHeader.cc','DadaReorder.cc','SortedDada.cc'],
				swig_opts=['-c++'],
                                )],
       py_modules = ["cDada"]
       )
